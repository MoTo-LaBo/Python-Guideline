# Python version control
- 自身の python version control
- brew : pyenv
### 1. brew upgrade
    brew upgrade
### 2. install 可能 list　表示
    pyenv install --list
### 3. install　したい version
    pyenv install <version名>
### 4. install 確認
    pyenv versions
### 5. 使用したい version
    pyenv global <version名>
### 6. 切り替えできたか確認
    python --version
# venv（仮想環境）control
- venv
- pyenv version 変更後対応
### 1. 仮想環境構築
    python3 -m venv <venv name>
### 2.  venv 起動
    source <venv name>/bin/activate
### 3. 仮想環境から出る
    deactivate
- 仮想環境に入ると (venv : ベンブ) の表示がされる
  - 基本的に作業は仮想環境内で行う
  - 仮想環境内に入っていないと、python, django が実行されないので（使用できない）ので注意する
#### 仮想環境から抜ける
    　deactivate
## 仮想環境 version　up / 移動・変更(場所を変更する)
> https://teratail.com/questions/99419
- 基本的に venv で作成した仮想環境は、directory の場所を変更した場合、error が表示されて localserver にアクセスできなくなる。 (runserver)ができなくなってしまう
- 理由は venv 作成時に path がしっかりと記述・管理されている為
  - directory を移動してしまうと、 venv 作成時の path と移動先で venv (仮想環境)を立ち上げた時の path が違う為に起こる
#### error code
    ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
-  ImportErrorです。Django をインポートできませんでした。Djangoがインストールされていて、環境変数PYTHONPATHにあることを確認していますか？仮想環境の起動を忘れていませんか？
- これは venv(仮想環境)の中にいて起こった現象。django も install されている。
- venv は立ち上がるが、python manage.py runserver で local 環境への acssece はできない
- **下記の対応をする事で問題は解決できる**
### 1. 現在の venv 環境 data を backup する
    pip freeze > requirements.txt
- ライブラリの情報を pip freezeで書き出す
- requirements.txt -> Pythonの標準ライブラリの記述 file
  - json、random、math、pip、pandas、Pillow、sys、Numpy、datetime、os、dateutil、re、calendar、matplotlib、sklearn
  - 現在 venv 環境で install して使用しているものを書き出してくれる
### 2. 仮想環境から抜ける
    deactivate
### 3. 新しい仮想環境(今回はnewenvという名前)を作る
    python3 -m venv newenv
### 4. 新たな仮想環境に入る
    source newenv/bin/activate
### 5. 2で書き出したライブラリをインストールして復元する
    pip install -r requirements.txt

    # しっかりと復元されているか確認する
    pip freeze
- これで新たな場所での環境復元とpython の version が update & 変更できる。version を変えたくなければ、version の指定を忘れずに行う
### 6. version 指定の場合
    pip install virtualenv

    # version は現在のもの
    virtualenv 環境名
    # version 指定
    virtualenv -p python3.7 環境の名前
