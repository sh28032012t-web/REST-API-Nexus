from config import app
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api_requests.get_user import router as get_user_router
from api_requests.post_user import router as post_user_router
from api_requests.put_user import router as put_user_router
from api_requests.delete_user import router as delete_user_router
from api_requests.patch_user import router as patch_user_router

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(get_user_router)
app.include_router(post_user_router)
app.include_router(put_user_router)
app.include_router(delete_user_router)
app.include_router(patch_user_router)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/{page}.html")
def pages(page: str):
    return FileResponse(f"static/{page}.html")
