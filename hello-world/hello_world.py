import requests
import argparse

r = requests.get('https://www.google.com/')
print(r.status_code)

parser = argparse.ArgumentParser()
parser.add_argument('--reason', type=str, required=True)
parser.add_argument('--file_name', type=str, required=False)
args = parser.parse_args()
print(args)
print(args.reason)
