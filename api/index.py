from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def upload_form():
    with open("static/form.html", "r") as f:
        return f.read()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), prompt: str = Form(...)):
    content = await file.read()
    return {"filename": file.filename, "prompt": prompt, "size": len(content)}
