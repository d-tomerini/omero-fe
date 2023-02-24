# -*- coding: utf-8 -*-
"""
Subroutine and classes to deal with the ontology objects
"""

import requests
import urllib3

from api.secrets.tokens import CENTREE_TOKEN
from schemas import OntologySummaryVM

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CENTREE_URL = 'https://ontology.cslbehring.com'


class CENtree_object:
    """
    Class to deal with ontology object coming from centree.
    Object is identified from the parent ontology object and by its name.
    """

    headers = {
        'Authorization': f'Bearer {CENTREE_TOKEN}',
        'Content-Type': 'application/json'
    }

    def __init__(
            self,
            primaryLabel: str,
            ontology: str,
            attributes: OntologySummaryVM = None):
        """
        The initialization search data on CENtree if not provided at
        object creation.
        """
        self.primaryLabel = primaryLabel
        self.ontology = ontology
        self.attributes = attributes
        if not self.attributes:
            # as this is is a search, it might be that the label is not unique
            # the search returns an element array
            response = self.exact_search()
            if len(response) != 1 :
                raise Exception(f'found {len(response)} elements, expecting 1')
        self.attributes = OntologySummaryVM(**response[0])

    def exact_search(self):
        """
        search the exact object on the api
        example query:
        GET https://ontology.cslbehring.com/api/search/CSLBDS/exactLabel?label=Location
        """
        params = {
            'label': self.primaryLabel
        }

        endpoint = f'/api/search/{self.ontology}/exactLabel'
        response = requests.get(
            CENTREE_URL + endpoint,
            params=params,
            headers=self.headers,
            timeout=10,
            verify=False
        )
        if response.status_code != 200:
            raise Exception(
                params,
                self.headers,
                endpoint,
                response.status_code,
                response.json())
        return response.json()

    def form_search(self, root, search_value):
        """
        Returns a list of json leaves possibilities to build a form starting from the given subclass
        root is the "shortFormIDs" of a centree item
        """
        params = {
            'ontology': self.ontology,
            'q': search_value,
            'childrenOf': root
        }
        endpoint = '/api/forms/search'
        response = requests.get(
            CENTREE_URL + endpoint,
            params=params,
            headers=self.headers,
            timeout=10,
            verify=False
        )
        if response.status_code != 200:
            raise Exception(response.status_code, response.json())
        return ([item for item in response.json()['elements']])

    def path_from_root(self, uuid):
        """
        Returns a list of elements that goes from the child to its root
        """
        endpoint = f'/api/ontologies/{self.ontology}/classes/{uuid}/paths-from-root'
        response = requests.get(
            CENTREE_URL + endpoint,
            headers=self.headers,
            timeout=10,
            verify=False
        )
        if response.status_code != 200:
            raise Exception(response.status_code, response.json())
        pass
        path = []
        x = response.json()
        while x.get('leaves', None):
            x = x['leaves'][0]
            path.append(x['value'])
            # TODO it should give a warning if more than a path is returned

        return path

    def is_leaf(self):
        """
        Check if the value is a terminal leaf or has branches
        """

    def subclass_search(self):
        """
        search subclass objects within the name and ontology of self
        """
        params = {
            'from': 0,
            'size': 1000
        }
        endpoint = f"/api/ontologies/{self.ontology}/classes/{self.attributes['id']}/children"
        response = requests.get(
            CENTREE_URL + endpoint,
            params=params,
            headers=self.headers,
            timeout=10,
            verify=False
        )
        if response.status_code != 200:
            raise Exception(response.status_code, response.json())
        r = response.json()
        if r['total'] > 0:
            children = []
            for item in r['elements']:
                if item['id'] != self.attributes['id']:
                    children.append(
                        CENtree_object(
                            ontology=self.ontology,
                            primaryLabel=item['primaryLabel'],
                            attributes=OntologySummaryVM(item))
                    )
        return children
