#! /usr/bin/env python3
import argparse
import yaml
import requests
import os
import time
import tarfile

RED = "\033[91m"
GREEN = "\033[92m"
END = "\033[0m"

def parse_args():
    parser = argparse.ArgumentParser(prog="vaccine", description="Take viccine to website with SQL Injection")
    parser.add_argument("url", help="URL of the website to attack")
    parser.add_argument("-X", "--method", default="GET", help="HTTP method to use")
    parser.add_argument("-o", "--output", default="output.tar", help="Output file to save the response")
    parser.add_argument("-H", "--header", action="append", help="HTTP headers to use")
    options = parser.parse_args()
    method = options.method.upper()
    if method not in ["GET", "POST", "HEAD"]:
        parser.error("Invalid method")
    return parser.parse_args()

def vaccine():
    with open("payload.yml", "r") as f:
        vaccine_list = yaml.safe_load(f)
        for db, values in vaccine_list.items():
            # print(f"actack on database {db}")
            for type, payloads in values.items():
                # print(f"actack type {type}")
                for index, payload in enumerate(payloads):
                    # print(f"{index}: {payload}")
                    query_name = f"{db}_{type}_{index}.txt"
                    response = make_request(payload)
                    save_response(query_name, response)
                    time.sleep(0.5)
            # print()

def make_request_headers():
    headers = {}
    if args.header and len(args.header) > 0:
        for h in args.header:
            key,value = h.split("=")
            headers[key] = value
    return headers

def make_request(query: str):
    try:
        headers = make_request_headers()

        if args.method.upper() == "POST":
            payload = {'username': query}
            res = requests.post(args.url, headers=headers, json=payload)
        elif args.method.upper() == "HEAD":
            res = requests.head(args.url, headers=headers)
        elif args.method.upper() == "GET":
            url = f"{args.url}/{query}"
            res = requests.get(url=url, headers=headers)
        else:
            raise("Invalid method") 

        if res.status_code == 200:
            # print(GREEN, f"Response: {res.text}", END)
            return res.text
        else:
            # print(RED, f"Response: {res.reason}", END)
            return res.reason

    except requests.HTTPError as e:
        print(f'HTTP error occurred: {e}')

    except Exception as e:
        print(e)

def save_response(name: str, result: str):
    try:
        open_dir = 'output'
        if not os.path.exists(open_dir):    
            os.makedirs(open_dir)
        filename = os.path.join(open_dir, name)
        with open(filename, 'w') as f:
            f.write(result)
    except Exception as e:
        print(e)

def make_achive():
    try:
        filename = args.output
        target_dir = 'output'
        with tarfile.open(filename, "w") as tar:
            for root, dirs, files in os.walk(target_dir):
                for f in files:
                    tar.add(os.path.join(root, f))
        print(f'Archive output to {filename}')
    except Exception as e:
        print(e)

def main():
    vaccine()
    make_achive()

if __name__ == "__main__":
    args = parse_args()
    main()
