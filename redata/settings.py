import os

GF_SECURITY_ADMIN_USER=os.environ['GF_SECURITY_ADMIN_USER']
GF_SECURITY_ADMIN_PASSWORD=os.environ['GF_SECURITY_ADMIN_PASSWORD']

METRICS_DB_URL = os.environ['REDATA_METRICS_DB_URL']

REDATA_METRICS_DATABASE_HOST = os.environ['REDATA_METRICS_DATABASE_HOST']
REDATA_METRICS_DATABASE_USER = os.environ['REDATA_METRICS_DATABASE_USER']
REDATA_METRICS_DATABASE_PASSWORD = os.environ['REDATA_METRICS_DATABASE_PASSWORD']
REDATA_METRICS_DATABASE_NAME = os.environ['REDATA_METRICS_DATABASE_NAME']

REDATA_GRAFANA_SOURCE = 'redata_metrics_db'

TEMPLATES_DIR_LOCATION = 'redata/grafana/templates/'
HOME_DASHBOARD_LOCATION = TEMPLATES_DIR_LOCATION + 'home.json'
HOME_OVERRIDES_LOCATION = TEMPLATES_DIR_LOCATION + 'overrides.json'
TABLE_DASHBOARD_LOCATION = TEMPLATES_DIR_LOCATION + 'table.json'
TARGETS_DASHBOARD_LOCATION = TEMPLATES_DIR_LOCATION + 'targets.json'

CUSTOM_PANEL_LOCATION = TEMPLATES_DIR_LOCATION + 'panel.json'
CUSTOM_ROW_LOCATION = TEMPLATES_DIR_LOCATION + 'row.json'

VOLUME_INTERVAL = ['1 hour', '1 day', '7 day', '30 day']

REDATA_SOURCE_DBS = [
    {
    'name': el.replace('REDATA_SOURCE_DB_URL_', ''),
    'db_url': os.environ[el]
    } for el in os.environ if el.startswith('REDATA_SOURCE_DB_URL_')
]

REDATA_AIRFLOW_SCHEDULE_INTERVAL = '*/10 * * * *'