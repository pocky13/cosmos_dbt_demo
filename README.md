# cosmos-dbt-demo

[astronomer/astronomer-cosmos](https://github.com/astronomer/astronomer-cosmos)を使ったdbtパイプラインのサンプル

* localでairflowを起動
* cosmosを利用してjaffle_shopを解析しDAGに登録
* duckDBでELT

という感じになっています。

## 実行方法

1. 適当なpython仮想環境を作る(3.10.2で確認済み)

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. ローカルのairflowとdbt_profileの初期化

```
./init.sh
```

3. Airflowサーバ&スケジューラの起動

```
./run.sh
```

user/passwordはadmin/adminで