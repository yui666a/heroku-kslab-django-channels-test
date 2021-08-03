# labstudy01

大富豪　つくるよー m9(^^)
大富豪　つくらないよー m9(^^)

## サーバの起動方法

基本これで OK↓

> python manage.py runserver

もっと詳細にしたい場合 ↓

> python manage.py runserver 0:[port 番号]

# 構成

kslab_study  
 &emsp;|─ kslab_study/ ... このプロジェクトの主要部分  
 &emsp;|─ daihugo/ ... 大富豪アプリのメインディレクトリ  
 &emsp;| &emsp;&emsp;&emsp;|─ static/daihugo/ ... 画像や CSS,JS など静的ファイルを入れておく  
 &emsp;| &emsp;&emsp;&emsp;|─ templates/daihugo/ ... html などを入れておく  
 &emsp;| &emsp;&emsp;&emsp;|─ \_\_init\_\_.py ...ディレクトリである事の証明（消さないで！）  
 &emsp;| &emsp;&emsp;&emsp;|─ admin.py ...  
 &emsp;| &emsp;&emsp;&emsp;|─ apps.py ... config が入っている  
 &emsp;| &emsp;&emsp;&emsp;|─ models.py ...  
 &emsp;| &emsp;&emsp;&emsp;|─ tests.py ... テストファイル（必要？）  
 &emsp;| &emsp;&emsp;&emsp;|─ urls.py ... uri と何を表示させるか設定する  
 &emsp;| &emsp;&emsp;&emsp;└─ views.py ... 画面の見える部分を設定  
 &emsp;|─ templates/ ... html の元的なファイルを格納  
 &emsp;|─ static/ ... CSS など静的ファイルを格納  
 &emsp;|─ db.sqlite3 ... 諸設定が詰まった DB ファイル．更新するときは python manage.py migrate で  
 &emsp;└─ manage.py ... 色々してくれる素敵なファイル

# git 関連

- git flow([参考リンク](https://qiita.com/KosukeSone/items/514dd24828b485c69a05))を採用したい
- 初めはローカルに dev ブランチがないと思うので，下のコマンドを試して欲しい
  > git fetch origin dev(リモートのブランチ名)

# 検討事項

- material-design-icons 使うか?

# Q&A

- **python が実行できない（windows の場合）**
  コマンドプロンプトに python と入力すると，windows store が開かれるので python3.9 をインストールしてください．
- **django がないと怒られる**
  下のコマンドでインストール
  > pip install django
  > pip install -U channels
