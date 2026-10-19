import os

from pathlib import Path

from dotenv import load_dotenv

from api_client import get_json


env_path = Path(__file__).parent / "env" / ".env"
load_dotenv(dotenv_path=env_path)

token = os.getenv("GITHUB_TOKEN")

if token is None:
    print("GITHUB_TOKEN was not found in the .env file.")
else:
    username = input("Enter a GitHub username: ").strip()

    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "sort": "pushed",
        "per_page": 5
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    repositories = get_json(
        url,
        params=params,
        headers=headers
    )

    if repositories is not None:
        print("\nLatest pushed repositories:")

        for repository in repositories:
            print(repository["name"])