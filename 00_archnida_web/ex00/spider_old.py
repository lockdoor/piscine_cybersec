import sys
import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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

def spider():
    try:
        args = parse_args()
        r = requests.get(args.URL, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')

        # Allow image type
        allowed_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        urls: str = []

        ## test for error file not found
        # urls.append("https://www.42bank.com/file-not-found.jpg")   

        for image in images:
            src: str = image.get('src')
            if src and not any(src.endswith(ext) for ext in allowed_ext):
                continue
            urls.append(src)

        ## save file
        save_path = args.p
        os.makedirs(save_path, exist_ok=True)  # Create directory if it doesn't exist
        
        ## set recursion
        if not args.r:
            recursion = 1
        else:
            recursion = args.l

        for url in urls:
            if recursion == 0:
                break
            url_parse = urlparse(url, allow_fragments=False)
            filename = f'{save_path}/{url_parse.path.split("/")[-1]}'

            try:
                img_data = requests.get(url_parse.geturl(), timeout=5).content
                with open(filename, 'wb') as f:
                    f.write(img_data)
                    print(f"Saved {filename}")
                recursion -= 1
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}", file=sys.stderr)
                continue
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    spider()

    