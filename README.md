# 型アノテーションの設定

## mypy とは

python の型アノテーションの正しさの判定を行う。

## 以下のインストール

```shell
virtualenv env
start env/Scripts/activate.bat
pip install mypy
```

## mypy で型判定を行う

```shell
mypy ~.py
#ディレクトリ以下全てのpythonファイルの型チェックを行う
mypy ディレクトリ名
```

## 型一覧

[型一覧のリンク (mypy 公式ドキュメント)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

### txt ファイルに適応したいディレクトリをまとめて書いておける

#### example

[mypy_files.txt]

```mypy_files.txt
src/main
src/test
```

以下のコマンドで実行

```
mypy @mypy_files.txt
```

## 型判定の無視を強要する

#### example

```python
a: any = 'hello' # type: ignore
```

## mypy のカスタム

1. `mypy.ini`を検証したい python ファイルがあるディレクトリに作成
2. 以下の設定がおすすめ

```mypy.ini
[mypy]
; python version
python_version = 3.8
; importされたpythonファイルの型判断を無視
ignore_missing_imports = True
; modules = []
; packages = []
; 型注釈のある関数から型注釈のない関数を呼び出すことを禁止するかどうか
disallow_untyped_calls = True
; 型宣言していない関数を許さないかどうか
disallow_untyped_defs = True
; disallow_untyped_defs = Trueの時に、型アノテーションが欠落していることを警告するかどうか
warn_incomplete_stub = True
; エラーメッセージの列番号を表示するかどうか
show_column_numbers = True

#以下のオプションは好み
#変数の再定義を許容するかどうか
allow_redefinition = True
; # type: ignore の存在を許すかどうか
; つまり、型定義を無視するように指示した行を許すかどうか
warn_unused_ignores = True
; 1つまたは複数のエラーコードをグローバルに無効にすることができる。
; 型は、エラーコードをstring型でlistとして記述
; エラーコードの解決ができないときの最終手段
; disable_error_code = []
```

実際のファイルに書き込む内容は、コメントアウトがあるとバグるので以下のものを使用

```mypy.ini
[mypy]
python_version = 3.8
ignore_missing_imports = True

disallow_untyped_calls = True
disallow_untyped_defs = True
warn_incomplete_stub = True
show_column_numbers = True

allow_redefinition = True
warn_unused_ignores = True
```

※`[mypy]`は、グローバル設定となる
※`#`は、コメントアウト
※`[hoge.sub-hoge]` ← これ以下に書く設定は、hoge/sub-hoge ディレクトリ以上で適応される
※`[mypy-package名]`← その package 名の設定となる

```mypy.ini
# Global options:
[mypy]

# Seach packge options:
[mypy-numpy]

# Sub directory options:
[]
```

3. 実行は、以下のコマンドになる

```shell
mypy --config-file mypy.ini ~.py
```

# mypy の最終的な実行コマンド

1. `mypy.ini`と`mypy_files.txt`をプロジェクトのルートディレクトリに作成
2. 以下のコマンドで実行をかける

```shell
mypy --config-file mypy.ini @mypy_files.txt
```
