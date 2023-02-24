# -*- coding: utf-8 -*-
"""
Author: Daniele Tomerini
Version: 0.1
Interface for a metadata search.
Data is stored in a local sqlite3 database, with all the limitation of the case!
"""
import os

import dash
import dash_bootstrap_components as dbc

DBC_CSS = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css'
external_stylesheets = [dbc.themes.SANDSTONE, DBC_CSS]

# Configure Dash to recognize the URL of the container
# Domino settings to expose the app
user = os.environ.get('DOMINO_PROJECT_OWNER')
project = os.environ.get('DOMINO_PROJECT_NAME')
runid = os.environ.get('DOMINO_RUN_ID')
if project:
    runurl = '/' + user + '/' + project + '/r/notebookSession/' + runid + '/'


app = dash.Dash(
    __name__,
    routes_pathname_prefix='/',
    requests_pathname_prefix=runurl,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets
)
