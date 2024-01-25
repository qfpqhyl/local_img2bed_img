import argparse
import re
import os
import requests
import chardet
import glob

def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def upload_image(image_path):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.post('https://im.gurl.eu.org/upload', files=files, headers=headers)
        response.raise_for_status()
        data = response.json()
        image_url = 'https://im.gurl.eu.org' + data[0]['src']
        return image_url

def replace_image_links_in_file(file_path, new_file_path):
    print("正在处理文件：" + file_path)
    encoding = get_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    image_links = re.findall(r'!\[.*?\]\(\s*(?!http://|https://)(.*?\.(?:jpg|png|gif|bmp|jpeg))\s*\)', content)
    print("共发现" + str(len(image_links)) + "个图片链接")
    for link in image_links:
        if os.path.isfile(link):
            new_link = upload_image(link)
            content = content.replace(link, new_link)
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file_path', type=str, nargs='?', default='*.md', help='The path of the markdown file to process')
    parser.add_argument('--output', type=str, default='Output', help='The output directory')
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for file_path in glob.glob(args.file_path):
        new_file_path = os.path.join(args.output, os.path.basename(file_path))
        replace_image_links_in_file(file_path, new_file_path)

    print("local2bed任务完成！")