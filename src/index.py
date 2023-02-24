# -*- coding: utf-8 -*-
"""
Main entry point for the app.
Introduces the app layout, and how it will be called
"""

import os

from dash import dcc, html

from app import app
from callbacks import upload
from html_tabs import upload_tab

DASH_PORT = os.getenv('DASH_PORT') if os.getenv('DASH_PORT') else 8888
# Set layout
app.layout = upload_tab

# running locally in Debug mode i.e. refreshing on changes
if __name__ == '__main__':
    app.run_server(
        port=DASH_PORT,
        host='0.0.0.0',
        debug=True)
