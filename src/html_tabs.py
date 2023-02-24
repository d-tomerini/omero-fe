# -*- coding: utf-8 -*-
"""
This file contains the definition of the html elements in the main app.
In here I define the tab elements, further detailed in the html_elements section
"""

import dash_bootstrap_components as dbc
from dash import dash_table, dcc, html

from html_elements import (
    optional_upload, required_upload,
    upload_metadata_store_selector, upload_space)

upload_tab = html.Div(
    style={'paddingLeft': '40px', 'paddingRight': '40px'},
    children=[
        upload_space,
        dbc.Row(
            [
                dbc.Col(upload_metadata_store_selector, md=3),
                dbc.Col(
                    dbc.Accordion([
                        dbc.AccordionItem(
                            required_upload,
                            title='Required metadata',
                            item_id='required-accordion',
                        ),
                        dbc.AccordionItem(
                            optional_upload,
                            title='Optional metadata',
                            item_id='optional-accordion',
                        )],
                        id='meta-accordion',
                        flush=True,
                        # start_collapsed=True,
                    ),
                    md=9),
            ],
            align='start'
        ),
        dcc.ConfirmDialog(
            id='confirm-upload',
            message='File and associated metadata uploaded'
        ),
        html.Div(
            id='uploaded-metadata',
            children=[],
        )
    ],
)

