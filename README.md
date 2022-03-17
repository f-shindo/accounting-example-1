# accounting-example-1

経理ラボ用に作成した ERC20 の送信内容を簡易的にチェックするツールです。

## ローカル環境での Test

### 環境設定

ローカルでのテスト時は、それぞれの端末で環境変数をセットしてください。

Linux や Mac

```console
$ export ETH='https://mainnet.infura.io/v3/取得したインフラキー'
$ export POL='https://rpc-mainnet.matic.network'
$ export GNO='https://rpc.xdaichain.com/'
$ export SDN='https://rpc.shiden.astar.network:8545/'
```

Windows

```console
$ set ETH='https://mainnet.infura.io/v3/取得したインフラキー'
$ set POL='https://rpc-mainnet.matic.network'
$ set GNO='https://rpc.xdaichain.com/'
$ set SDN='https://rpc.shiden.astar.network:8545/'
```

### 起動

```console
$ python main.py
```

Docker を使う場合

```console
$ docker build -t example1 .
$ docker run --rm -p 8080:8080 -e PORT=8080 -e ETH -e POL -e GNO -e SDN example1
```

### 動作確認

次の URL にアクセスしてください。

http://localhost:8080/

## Cloud Run へのデプロイ

事前に講師まで Google アカウントをご連絡ください。

### Cloud SDK のインストール

Cloud SDK を次の URL からインストールしてください。

https://cloud.google.com/sdk/docs/install?hl=ja

### GCP への接続

```console
$ gcloud auth login
```

ブラウザが立ち上がるので、内容を確認して承認してください。

### プロジェクトの選択

```console
$ gcloud projects list
$ gcloud config set project <PROJECT_IDを入力>
```

### デプロイ

```console
gcloud run deploy --source .\
    --set-env-vars ETH='https://mainnet.infura.io/v3/取得したインフラキー'\
    --set-env-vars POL='https://rpc-mainnet.matic.network'\
    --set-env-vars GNO='https://rpc.xdaichain.com/'\
    --set-env-vars SDN='https://rpc.shiden.astar.network:8545/'
```

```
Service name (accounting-example-1):自分の名前を入力(例:shindo)
Please specify a region:3(asia-northeast1)を選択
Allow unauthenticated invocations to [accounting-example-1]:yを選択

```

Service URL が出てくるのでアクセスし挙動を確認してください。
