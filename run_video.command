#!/bin/bash

# Pythonスクリプトのパスを指定
SCRIPT_PATH="$(dirname "$0")/Video.py"

# Pythonインタプリタのパスを指定
PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"

# ffmpegのパスを指定
FFMPEG_PATH="$(dirname "$0")"
export PATH="$FFMPEG_PATH:$PATH"

# カレントディレクトリをスクリプトのある場所に変更
cd "$(dirname "$SCRIPT_PATH")"

# スクリプトを実行
$PYTHON_PATH $SCRIPT_PATH

# 実行が終了したらプロンプトを表示
echo "Press Enter to exit..."
read
