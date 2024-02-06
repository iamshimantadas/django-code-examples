from typing import Union

from fastapi import FastAPI

# imprting required modules
from fastapi import UploadFile, File, status
import shutil, uuid, json
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException


app = FastAPI()

# mounting the 'files' folder
app.mount('/files', StaticFiles(directory='files'),'files')

# upload file into 'files/' folder
@app.post("/upload-file")
def upload_files(uploaded_file: UploadFile = File(...)):
    # will generate a unique file hashname
    unique_filename = str(uuid.uuid4()) + "_" + uploaded_file.filename

    path = f"files/{unique_filename}"
    with open(path, 'w+b') as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return {
        "message": "file uploaded",
        'file': unique_filename,
        'content': uploaded_file.content_type,
        'path': path,
    }