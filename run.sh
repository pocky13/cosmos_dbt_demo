#!/bin/bash
export AIRFLOW__CORE__LOAD_EXAMPLES=false
export AIRFLOW_HOME="$(pwd)/airflow"

airflow webserver --port 8080 & 
airflow scheduler
