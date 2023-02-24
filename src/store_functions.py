# -*- coding: utf-8 -*-
"""
Store: wherever I want to get or upload information
The classes and routines in this folder will deal
with abstracting how and where to get info
"""

from api.aws_interface import build_aws_filter_query
from api.sql_interface import build_sql_filter_query
from backend import (db_stores, get_schema, search_store_column,
                     search_store_data)
from schemas import StoreInfo


class Store:
    """
    Simple class to deal with the different cases of store.
    For search, filtering, presenting results, and more to be added.
    Store.stores is a list of all the sources, from the backend.
    Imported once at class instance
    """

    # here we define all possible stores, to have corresponding methods

    stores = {s['name']: StoreInfo(**s) for s in db_stores}

    def __init__(self, store):
        self.store = self.stores[store]

    @classmethod
    def get_all_stores(cls):
        """ all names for stores -- used internally to call. """
        return [x.name for x in cls.stores.values()]

    @classmethod
    def get_all_labels(cls):
        """ all names for stores -- used internally to call. """
        return [x.label for x in cls.stores.values()]

    @classmethod
    def get_label_store_dict(cls):
        """ convenience call for dictionary label: store. """
        return {item.label: store for store, item in cls.stores.items()}

    def get_schema(self):
        """ Return schema for table. """
        return get_schema(self.store.name)

    def get_data(self, filters=None):
        """
        Returns the data in the form of a dataframe
        Filter is in the form of a list of key,value tuple to filter on columns
        :param column: if selected, filters the data on the column to get
            distinct row values
        :param filters: builds 'WHERE' sql statement to filter data
        :return: data from the database as records (json list of column:value)
        TODO: add sql-like statements using operators to build a query on the database
        """
        if self.store.name == 'AWS':
            query_filter = build_aws_filter_query(filters)
        else:
            query_filter = build_sql_filter_query(filters)
        df = search_store_data(
            self.store.name,
            query_filter=query_filter)
        return df

    def get_column_distinct(self, column, filters=None):
        """
        Returns the data in the form of a dataframe
        Filter is in the form of a list of key,value tuple to filter on columns
        :param column: if selected, filters the data on the column to get
            distinct row values
        :param filters: builds 'WHERE' sql statement to filter data
        :return: list of distinct values
        TODO: add sql-like statements using operators to build a query on the database
        """
        if self.store.name == 'AWS':
            query_filter = build_aws_filter_query(filters)
        else:
            query_filter = build_sql_filter_query(filters)
        values_array = search_store_column(
            self.store.name,
            column=column,
            query_filter=query_filter)
        return values_array


def extract_values_from_context(context):
    """
    Takes the status and returns a list of key:value pairs,
    associating id and value
    what I need to proceed are the:
    - filter name:     dropdown_state_list['id']['index']
    - filter value :   dropdown_state_list['value'])
    for reference: check dash.callback_context.inputs_list
    """
    keys = [item['id']['index'] for item in context]
    vals = [item.get('value', None) for item in context]
    return keys, vals


sql_where_options = ['=', '>', '<', '>=', '<=', '≠', 'Between', 'Like', 'In']
