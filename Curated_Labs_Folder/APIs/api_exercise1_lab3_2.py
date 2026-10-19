# t4:

import os
from pathlib import Path

import requests
from dotenv import load_dotenv


env_path = Path(__file__).parent / "env" / ".env"
load_dotenv(dotenv_path=env_path)

token = os.getenv("GITHUB_TOKEN")

if token is None:
    print("GITHUB_TOKEN was not found.")
else:
    url = "https://api.github.com/rate_limit"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Request with the token
    authenticated_response = requests.get(
        url,
        headers=headers,
        timeout=5
    )
    authenticated_response.raise_for_status()

    # Request without the token
    unauthenticated_response = requests.get(
        url,
        timeout=5
    )
    unauthenticated_response.raise_for_status()

    print(
        "With token:",
        authenticated_response.headers["X-RateLimit-Limit"]
    )
    print(
        "Without token:",
        unauthenticated_response.headers["X-RateLimit-Limit"]
    )



# t5:

""" Why 401 rather than 403?
401 Unauthorized: the supplied authentication credentials are invalid, so GitHub cannot authenticate the request.
403 Forbidden: the request may be understood, but access is refused."""