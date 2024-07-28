#!/usr/bin/env python3
import os
import subprocess
import sys

def main(url):
    # 現在のスクリプトのディレクトリを基準にffmpegのパスを設定
    ffmpeg_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffmpeg')
    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "-N", "1",
        "-S", "vcodec:h264",
        "-o", "%(title)s.%(ext)s",
        "--merge-output-format", "mp4",
        "--ffmpeg-location", ffmpeg_location,
        url
    ]
    print("Executing command:", " ".join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        url = input("Enter the URL: ")
        main(url)
