from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import app_router

app = FastAPI()

# Enable CORS to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(app_router)
