export AIRFLOW_HOME="$(pwd)/airflow"
airflow db init
airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@admin.com \
    --password admin

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOSの場合
    sed -i '' "s:/path/to/pwd:$(pwd):" dbt_jaffle_shop/profiles.yml
else
    # Linux、BSD、その他のUnixの場合
    sed -i "s:/path/to/pwd:$(pwd):" dbt_jaffle_shop/profiles.yml
fi