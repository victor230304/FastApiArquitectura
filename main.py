from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Movie API")

db_peliculas = {}

class Pelicula(BaseModel):
    titulo: str
    director: str
    genero: str
    en_cartelera: bool = True


@app.get("/peliculas")
def listar_peliculas():
    return db_peliculas


@app.get("/peliculas/{pelicula_id}")
def obtener_pelicula(pelicula_id: int):
    return db_peliculas.get(pelicula_id, {"error": "Película no encontrada"})


@app.post("/peliculas")
def crear_pelicula(pelicula: Pelicula):
    nuevo_id = len(db_peliculas) + 1
    db_peliculas[nuevo_id] = pelicula
    return {"id": nuevo_id, "pelicula": pelicula}


@app.put("/peliculas/{pelicula_id}")
def actualizar_pelicula(pelicula_id: int, pelicula: Pelicula):
    db_peliculas[pelicula_id] = pelicula
    return {"mensaje": "Película actualizada", "id": pelicula_id}


@app.delete("/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    eliminada = db_peliculas.pop(pelicula_id, None)
    return {"eliminada": bool(eliminada)}