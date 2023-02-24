# -*- coding: utf-8 -*-
"""
Here we define the tokens, or take them from environment variables
"""

import os

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Those might alternatively be set here, and not taken from environment

CENTREE_TOKEN = os.getenv('CENTREE_TOKEN')
TETRASCIENCE_TOKEN = os.getenv('TETRASCIENCE_TOKEN')

# AWS catalog
# Not really used it here anymore, moved to backend

AWS_CATALOG = 'AwsDataCatalog'
GLUE_CATALOG = 'rnd-glue-metadata-bdsi-biancatoma'
DATABASE_TABLE = 'rndbdsimetadatalocation'
AWS_REGION = os.getenv('AWS_REGION')
ATHENA_QUERY = f'SELECT * FROM "{GLUE_CATALOG}"."{DATABASE_TABLE}"'
