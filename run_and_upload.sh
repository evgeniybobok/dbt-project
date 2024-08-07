#!/bin/bash
if [[ -z "${DBT_COMMAND}" ]]; then
    echo ERROR: Please provide some dbt command
    exit 1
else
    echo Executing ${DBT_COMMAND}
    ${DBT_COMMAND} && python3 upload_to_s3.py
fi
