import sys
import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# This is tutorial of argparse
# https://docs.python.org/3/howto/argparse.html#argparse-tutorial
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("URL", type=str, help="URL to download")
    # the action="store_true" will store True if the option is present, False otherwise
    parser.add_argument("-r", action="store_true", help="Recursive download")
    parser.add_argument("-l", type=int, default=5, help="Recursive download level")
    parser.add_argument("-p", type=str, default="data", help="Path to save files")
    return parser.parse_args()

urls = []
images = []
# Allow image type
allowed_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

def save_image(path: str, soup: any, url: str):
    '''
    path=path to save;
    soup=soup;
    url=current page;
    '''
    imgs = soup.find_all('img', src=True)
    srcs: str = []

    for img in imgs:
        src: str = img.get('src')
        if src and not any(src.endswith(ext) for ext in allowed_ext):
            continue
        srcs.append(src)

    ## save file
    os.makedirs(path, exist_ok=True)

    for src in srcs:
        try:
            img_url = urljoin(url, src)
            img_parse = urlparse(img_url, allow_fragments=False)
            filename = f'{path}/{img_parse.path.split("/")[-1]}'
            if filename in images:
                continue
            
            img_data = requests.get(img_url, timeout=5).content
            with open(filename, 'wb') as f:
                f.write(img_data)
                print(f"Saved {filename}")
            images.append(filename)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            continue


def spider(rec: int, path: str, url: str):
    # base case
    if rec == 0 or url in urls:
        return
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        urls.append(url)

        #test
        print(url)

        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for l in links:
            href = l.get('href')
            url_parse = urlparse(url, allow_fragments=False)
            absolute_url = urljoin(url_parse.geturl(), href)
            
            # call recursive
            spider(rec - 1, path, absolute_url)
            
            # get image and save
            save_image(path, soup, url)             
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        args = parse_args()
        rec = args.l if args.r else 1
        spider(rec, args.p, args.URL)

    except Exception as e:
        print(f"Error: {e}")