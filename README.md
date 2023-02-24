Front-end of the datalake application
=====================================

This application is a mock-up for the upload and search capabilities to be implemented
as the entry point of the datalake.

The app has two parts:

  - A search interface, to query the databases for information about the saved metadata.
  - An upload interface, to upload a file with the required metadata and optional metadata expected.
    for the files

Technical details:
  - The *front-end* is developed with python `dash`, a package to develop data science solutions and
    reactive dashboard.
  - The *back-end* is developed using FastApi, using sqlite3 to store local information about metadata,
    and querying an AWS athena data storage.
