# OOP : Object Oriented Programming (オブジェクト思考)
- python はオブジェクト指向のプログラミング言語
- データとか機能をプログラミングする際の考え方や概念
- 「オブジェクト指向が何なのか」を言語化するのは難しい
- なので習うより慣れろ！！
##
    " Hello world ".split()
- strings のオブジェクト   : " Hello world "
- object が持っている機能 : split( )
### 「 なんの object かが分かれば、使える機能がわかる 」
例）テスラもプリウス = 車
- アクセルを踏めば前に進むし、ブレーキを踏めば止まる
- 多少の仕様の違いはあれ、車というモノの基本的な使い方は変わらない
## Class = 設計図
object が共通で持つ変数や関数を定義する
- 変数 = 属性
- 関数 = メソッド

例）
- 右のペダルを踏めば前に進む = アクセル
- 左のペダルを踏めば止まる = ブレーキ
### class -> から作られモノを instance (インスタンス)
## instance variable(インスタンス変数)
- __ init __ (self, 〇〇)
  - 上記のインスタンスに紐付いた変数をインスタンス変数という
  - self.〇〇 = 〇〇　　print(john.〇〇)
## static method (スタティックメソッド)
- インスタンスに紐づかないメソッド
- @staticmethod デコレーターを使用する
- 主に class 内で便利関数のように使用する
- 引数に self を取らない (インスタンスの情報は使わない)
- class からアクセスして call する (< Class >.< staticmethod( )>)
- class の情報を使う場合は、classmethod を使用する

## class method(クラスメソッド)
- インスタンスに紐づかない
- @classmethod デコレーターを使用する
- 主に class 内で便利関数のように使用する
- 引数に cls を取って class の情報にアクセスできる
- class からアクセスして call する (< class >.< classmethod>)
- class の情報を使わない場合は staticmethod を使用する
- classmethod 内でインスタンスを生成して返すことも可能
 private 変数と名前修飾(name mangling : ネイムマングリング)
- private 変数は、 class 外からアクセスできない変数
- python には 「privateh 変数」はない
- 変数名の接頭辞に「 _  」(アンダースコア)を付けることで nonpublic にする事ができる
  - 慣習であって強制力はない
- 「 __ 」(2つのアンダースコア)を付ける事で名前修飾する
  - 名前修飾された変数名は＿< Class >_＿< attribute >のような形になる
  - 例 : _ Account __balance
  - 結果 private 変数のような役割を付けることができる
# 継承(inheritance)
- オブジェクト指向の要
  - 継承がなければオブジェクト指向とは言わない
- 他の class をベースの class として継承して、別の class を作ることができる
- super class(親クラス、規定クラス)の機能を引き継ぎ、sub class (子クラス、派生クラス)として拡張することができる
  - 例）車クラスをベースにトラッククラスを作成する
  - 車という共通の部分はそのまま継承させる
### 一番上にあるのは object それを継承して次のclass が作成される
- object　継承したものが↓
  - Animal　継承したものが↓
    - Horse(馬)　継承したものが↓
      - Friesian / Thoroughbred / mustang　（馬の種類）
### 継承は is a の関係になっている
#### 「 is-aの関係は、オブジェクトの一般化や特殊化を示し、”A is-a B”は”AはB（の一種）である”ことを示す。 」
- Horse is an Animal
- Friesian is an Horse
  - programing 上どんな class でも継承はできるが、is a の関係になっていないものは作成しない
