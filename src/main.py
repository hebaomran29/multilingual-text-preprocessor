# ============================================================
# main.py  — updated to serve the GUI
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles     import StaticFiles
from fastapi.responses       import FileResponse
import os

from config.settings    import APP_TITLE, APP_DESCRIPTION, APP_VERSION
from routers.preprocess import router as preprocess_router

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(preprocess_router)

# ── Serve static files ────────────────────────────────────
# Mount the static/ folder so index.html is reachable
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/",)  # tags=["Root"]
# def root():
#     """Serve the GUI."""
#     return FileResponse(os.path.join(static_dir, "index.html"))
def home():
    return FileResponse(os.path.join(static_dir, "index.html"))