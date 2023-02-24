# -*- coding: utf-8 -*-
"""
Main components of the html_tabs file
"""

import dash_bootstrap_components as dbc
from dash import dcc, html

from store_functions import Store

search_title = html.H3(
    style={'textAlign': 'center'},
    children='Mockup app to search metadata and upload files')

search_description = html.P(
    style={'textAlign': 'center'},
    children="""
    Mockup of a UI for the metastore backend on AWS.
    User might want to select various ontologies, and refine the search by providing various key/value pairs.
    The result is a SQL query to the glue catalog, returning the requested information and download links.
    """)

search_button = dbc.Button(
    'Search',
    id='search-button',
    color='primary',
    n_clicks=0)

download_button = dbc.Button(
    'Download results',
    id='download-button',
    color='primary',
    n_clicks=0,
    disabled=True,
    style={'float': 'right', 'display': 'inline-block'})

search_filter_selector = dcc.Dropdown(
    placeholder='Select one or more filters',
    multi=True,
    id='search_filter_selector')

search_metadata_store_selector = dbc.RadioItems(
    options=[{'label': k, 'value': v} for k, v in Store.get_label_store_dict().items()],
    value=Store.stores['BDSI'].name,
    inline=True,
    id='metadata-store-selector',)


upload_metadata_store_selector = dbc.Card([
    html.H5('Choose a metadata source', className='card-title'),
    dbc.RadioItems(
        options=[{'label': k, 'value': v} for k, v in Store.get_label_store_dict().items()],
        value=Store.stores['BDSI'].name,
        inline=False,
        id='upload-store-selector'
    ),
    html.Hr(),
    dbc.Button(
        'Upload the file',
        id='final-upload',
        disabled=True,
        n_clicks=0
    ),
    dcc.Store(id='metadata_fields')
],
    body=True,
    color='light',)


# Everything related to the search options
search_controls = dbc.Card([
    html.Div([
        html.H5('Choose a metadata source', className='card-title'),
        search_metadata_store_selector,
        search_filter_selector,
        html.Div(
            [],
            id='search-filter-div'
        ),
        html.Div(id='search-filter-info'),
        html.Hr(),
        search_button,
        download_button
    ]
    )],
    body=True,
    color='light',
)

# The div containing the table result
search_results = html.Div(
    [],
    id='results_table_div'
)


# The upload area of the app. Almost all is style
upload_space = dcc.Upload(
    id='upload-data',
    children=html.Div([
        'Drag and Drop or ',
        html.A('Select Files')
    ]),
    style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center',
        'margin': '10px'
    },
    # Allow multiple files to be uploaded
    multiple=False
)

# All the required metadata, from a dropdown option.
# Upload should not be allowed if one of those is None

required_upload = dbc.Card([
    html.Div(
        id='required-metadata-div',
        children = [html.Div('required metadata for the uploaded file')],
        className='dbc'
    )],
    color='light',
    body=True
)

# All the optional metadata, from a dropdown option
optional_upload = dbc.Card([
    html.Div([
        html.Div(
            id='further-metadata-selector',
            children = ['Optional metadata for the uploaded file'],
        ),
        html.Div(
            id='further-metadata',
            children=[],
        )
    ]),
],
    class_name='mb-3',
    body=True,
)
