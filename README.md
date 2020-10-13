# smile_practice
GCPのCloudVisionAPIを使って、笑顔練習が出来ます

プログラムを起動すると、PCのカメラが立ち上がるので、カメラにむけて笑顔を作ってください。
10秒毎に写真をとり、機械学習によって笑顔が以下の5段階でランク付けされます

1. VERY_LIKELY
2. LIKELY
3. POSSIBLE
4. UNLIKELY
5. VERY_UNLIKELY


# プログラムの起動方法
1. GCPプロジェクトで[サービスアカウントを作成](https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=ja)  
  roleは何もつけないで大丈夫です
2. 1で作成したサービスアカウントの[サービスアカウントキーを作成](https://cloud.google.com/iam/docs/creating-managing-service-account-keys?hl=ja)
3. サービスアカウントキーの作成で取得したキーファイルのフルパスを環境変数に登録      
　`export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential.json`
4. プログラムを起動(ライブラリのinstallが必要な場合があります)     
　`python smile_practice.py`
 
 
 
