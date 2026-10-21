# APIs - Day2 - Exercises

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


# e1:
app = FastAPI()

@app.get("/") # Route
def home() -> dict[str, str]:
    return {"message": "Movie API by Christian N."} # The Python function returns a dictionary. FastAPI serializes that dictionary into a JSON HTTP response.

movies = [
    {"id": 1, "title": "Prometheus", "director": "Ridley Scott", "year": 2012},
    {"id": 2, "title": "The Life Aquatic with Steve Zissou", "director": "Wes Anderson", "year": 2004},
    {"id": 3, "title": "2001: A Space Odyssey", "director": "Stanley Kubrick", "year": 1968},
    {"id": 4, "title": "Dreamcatcher", "director": "Lawrence Kasdan", "year": 2003}
]

@app.get("/movies")
def get_books():
    return movies

# ------

# e2:

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="No Movie found!")

# e3:

