# My python package creation memo



# プロジェクトのセットアップ
まずは適当なフォルダに行き、poetry でプロジェクトを作る
```
poetry new my_sample project
cd my_sample_project
poetry install
poetry add pytest --group dev
poetry add sphinx --group doc
poetry add sphinx-rtd-theme --group doc
```
デフォルトで以下のようなフォルダ構造になる。

```
├── my_sample_project
│   └── __init__.py
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```


ソースを src 以下に入れる場合は手動なりコマンドなりで入れるべし
```
├── pyproject.toml
├── README.md
├── src
│   └── my_sample_project
│       └── __init__.py
└── tests
    └── __init__.py

```
ついでに Git の環境も構築
```
git init
touch .gitignore
```

# ドキュメントの作成
Sphinx のセットアップ
```
spinx-apidoc -F -o docs/ src/my_sample_package/
```
conf.py で自分のパッケージのルートディレクトリを sys.path に追加しておく
```
import os
import sys
sys.path.insert(0, 'path/to/my_sample_package/src')

# ドキュメントのテーマも変えておく
html_theme = 'sphinx_rtd_theme'
```
ビルド
```
# make html する前にPython仮想環境に入る
source .venv/bin/activate

cd docs
make html
```















