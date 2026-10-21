# e6:

from api_client import get_json
import requests


BASE = "http://127.0.0.1:8000"

# Get and print every movie
movies = get_json(f"{BASE}/movies")
print(movies)

# Get a movie that does not exist
# get_json(f"{BASE}/movies/99") # Produces error "The server said no: 404"

# # Add a new movie
# new_movie = {
#     "title": "Aliens",
#     "director": "James Cameron",
#     "year": 1986
# }

# response = requests.post(
#     f"{BASE}/movies",
#     json=new_movie,
#     timeout=5
# )

# Part 2 e1:
movie_changes = { }

response = requests.patch(
    f"{BASE}/movies/1",
    json=movie_changes,
    timeout=5
)

print(response.status_code)
print(response.json())