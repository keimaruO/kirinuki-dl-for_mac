import os
import subprocess
import sys

def main(url):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yt_dlp_location = os.path.join(script_dir, 'yt-dlp_macos')
    ffmpeg_location = os.path.join(script_dir, 'ffmpeg')
    
    # 保存先をユーザーに選択させる
    save_dir = input("Enter the save directory: ")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    cmd = [
        yt_dlp_location,
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "-N", "1",
        "-S", "vcodec:h264",
        "-o", os.path.join(save_dir, "%(title)s.%(ext)s"),
        "--merge-output-format", "mp4",
        "--ffmpeg-location", ffmpeg_location,
        url
    ]
    
    print("Executing command:", " ".join(cmd))
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)
        print("Return code:", e.returncode)
        print("Output:", e.output)
        print("Error output:", e.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        url = input("Enter the URL: ")
        main(url)