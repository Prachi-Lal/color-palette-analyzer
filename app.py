from fastapi import FastAPI, File, UploadFile
from main import *
from http import HTTPStatus
from io import BytesIO
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    formatted_output = ""
    if file:
        content = await file.read()
        image = BytesIO(content)
        output = extract_optimum_colors(image)
        for character in output:
            formatted_output = formatted_output + character
        return {str("Operation Successful:"+str(HTTPStatus.OK)): formatted_output}
    else:
        return {"Error": "No file uploaded!"}