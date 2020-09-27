import os
import json


def fetch_credentials():
    with open("credentials.json") as f:
        creds = json.loads(f.read())
        return creds["API_KEY"], creds["BASE_URL"]


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "fuck this shit already"
    API_KEY, BASE_URL = fetch_credentials()