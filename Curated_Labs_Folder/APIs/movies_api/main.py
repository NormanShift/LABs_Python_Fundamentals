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

# e5 (out of order as expected)
def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="No Movie found!")


# Part 2 e1:

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None
    
#changes.model_dump(exclude_unset=True)   # only the fields the client sent


# e4 (exercise out of order as intended)
class Movie(BaseModel): # Pydantic BaseModel
    title: str
    director: str
    year: int


# @app.get("/movies")
# def get_movies():
#     return movies

# ------

# e2:

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)
# def find_movie(movie_id: int):
#     for movie in movies:
#         if movie['id'] == movie_id:
#             return movie
#     raise HTTPException(status_code=404, detail="No Movie found!")

# e3:

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):

    result = movies

    if director:
        result = [movie for movie in result if director.lower() in movie["director"].lower()
        ]
    if year is not None:
        result = [
            movie
            for movie in result if movie["year"] == year
        ]

    return result


# e4 (also see the BaseModel class):

@app.post("/movies",
          status_code=201)
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id,
                 "title": movie.title,
                 "director": movie.director,
                 "year": movie.year}
    movies.append(new_movie)
    return new_movie

# Omitting director and year returns 422 because both fields are required.
# Sending non-numeric text as year also returns 422 because Movie requires year to be an integer.
# The error response shows which field is wrong under "loc" and explains the problem under "msg".

# e5:

# e5:

@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)

    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year

    return existing


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)

# If the same movie is deleted twice, the second request calls find_movie() and receives the 404 response.
# Saving the file restarts the development server. Additions, Replacements, and Deletions disappear because movies is currently stored only in RAM.

# e6 (See the exercise PDF.)

# Part 2 e1:

@app.patch("/movies/{movie_id}")
def patch_movie(movie_id: int, movie_update: MovieUpdate):
    existing = find_movie(movie_id)

    changes = movie_update.model_dump(exclude_unset=True)
    existing.update(changes)

    return existing

# Part 2 e4 answer:
# PUT is used to replace an existing movie, so the client must send all fields.
# PATCH is used to update only selected fields, while all other fields remain unchanged.


