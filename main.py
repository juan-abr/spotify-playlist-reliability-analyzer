from fastapi import FastAPI
import auth.token_manager

auth_manager = auth.token_manager.auth_manager
sp = auth.token_manager.sp

print(auth_manager)
print(sp)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Playlist Reliability Service is running"}

# @app.get("/playlist/{playlist_id}/analysis")

# @app.get("/playlist/{playlist_id}/clean")

