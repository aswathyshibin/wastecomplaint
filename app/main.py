from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from app.ai_engine import analyze_complaint
import os

app = FastAPI(title="Waste Complaint AI Analyst")

# Define base directory relative to this file
# This is crucial for hosting on Vercel
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mount static files
static_dir = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Initialize templates with absolute path
templates_dir = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=templates_dir)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze")
async def analyze_web(complaint: str = Form(...)):
    """Handles AJAX requests from the web frontend."""
    result = analyze_complaint(complaint)
    return JSONResponse(content=result)


@app.post("/api/analyze")
async def analyze_api(data: dict):
    """Handles JSON requests from mobile apps or external integrations."""
    complaint = data.get("complaint", "")
    if not complaint:
        return JSONResponse(
            content={"error": "No complaint text provided"}, 
            status_code=400
        )
    
    result = analyze_complaint(complaint)
    return JSONResponse(content=result)