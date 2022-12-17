import argparse
import requests
from termcolor import colored

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", required=True, help="The host to test")
parser.add_argument("--headers", help="Authorization headers to include in the requests (format: 'key1:value1,key2:value2')")
args = parser.parse_args()

# Build the headers dictionary
headers = {}
if args.headers:
    for header in args.headers.split(","):
        key, value = header.split(":")
        headers[key] = value

# Try each HTTP method
methods = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
for method in methods:
    try:
        resp = requests.request(method, args.host, headers=headers)
        if resp.status_code >= 200 and resp.status_code < 300:
            color = "green"
        elif resp.status_code >= 300 and resp.status_code < 400:
            color = "yellow"
        elif resp.status_code >= 400 and resp.status_code < 500:
            color = "red"
        else:
            color = "grey"
        print(f"{method}: {colored(resp.status_code, color)}")
    except:
        print(f"{method}: {colored('request failed', 'red')}")
