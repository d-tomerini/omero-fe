# -*- coding: utf-8 -*-

"""
Schemas provide the pydantic models used for data validation and ORM
integration in SQLalchemy.
"""
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class StoreInfo(BaseModel):
    """
    Basic info about a store.
    :param name: name of the store, how it is identified in calls
    :param label: how it is called for the outside world
    :param local: if it is a file, where it is
    :param online: if it is a database, how to reach it
    """
    id: Optional[int]
    name: str
    label: str
    local: Optional[str]
    online: Optional[str]

    class Config:
        orm_mode = True


class ClassExpression(BaseModel):
    """ subclass of centree model. """
    classExpression: str
    entities: List[int]


class CENtreeTag(BaseModel):
    """ subclass of centree, for tags. """
    iri: str
    isLiteral: bool
    tagtype: str = Field(alias='type')
    value: str


class PropertyValueVM(BaseModel):
    """ subclass of centree, for property values """
    iri: str
    name: str
    tags: List[CENtreeTag]
    value: str


class typeOfNode(str, Enum):
    """ subclass of centree, for type of node. """
    subClassOf = 'subClassOf'
    partOf = 'partOf'
    derivesFrom = 'derivesFrom'
    developsFrom = 'developsFrom'
    equivalence = 'equivalence'


class OntologySummaryVM(BaseModel):
    """ centree main class to describe node properties. """

    annotationProperties: dict
    anonymousEquivalentClasses: List[ClassExpression]
    anonymousSuperClasses: List[ClassExpression]
    derivesFrom: List[str]
    developsFrom: List[str]
    entityType: str
    entityUniqueID: str
    equivalences: List[str]
    id: str
    mappings: List[str]
    numberOfChildren: int = None
    partOf: List[str]
    primaryID: str
    primaryLabel: str
    propertyValues: List[PropertyValueVM]
    relationalProperties: dict
    schemaVersion: int
    shortDisplayName: str
    shortFormIDs: List[str]
    sourceUniqueID: str
    superClasses: List[str]
    synonyms: List[str]
    textualDefinitions: List[str]
    typeOfNode: typeOfNode


class CentreeModel(BaseModel):
    """
    Info useful to generate a centree object
    """
    primaryLabel: str
    ontology: str


class UploadMeta(BaseModel):
    """
    Basic requirements for a metadatafield
    """
    id: Optional[int]
