import os
import time
import argparse
from datetime import datetime


def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('clean_trash.log', 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {message}\n")
    print(f"{timestamp} - {message}")


def clean_trash_folder(trash_folder_path, age_thr):
    for root, dirs, files in os.walk(trash_folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            if time.time() - os.path.getmtime(file_path) > age_thr:
                os.remove(file_path)
                log(f"Удален файл: {file_path}")

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                log(f"Удалена папка: {dir_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trash_folder_path', required=True)
    parser.add_argument('--age_thr', type=float, required=True)
    args = parser.parse_args()

    while True:
        clean_trash_folder(args.trash_folder_path, args.age_thr)
        time.sleep(1)


if __name__ == "__main__":
    main()