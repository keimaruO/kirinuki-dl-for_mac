#!/bin/bash

# スクリプトのディレクトリを取得
SCRIPT_DIR="$(dirname "$0")"

# Pythonスクリプトのパスを指定
SCRIPT_PATH="$SCRIPT_DIR/Video.py"

# Pythonインタプリタのパスを指定
PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"

# パスにスクリプトのディレクトリを追加
export PATH="$SCRIPT_DIR:$PATH"

# カレントディレクトリをスクリプトのある場所に変更
cd "$SCRIPT_DIR"

# スクリプトを実行
$PYTHON_PATH $SCRIPT_PATH

# 実行が終了したらプロンプトを表示
echo "Press Enter to exit..."
read