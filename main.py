from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Playlist Reliability Service is running"}

