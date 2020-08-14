import os
import pathlib
import shutil

from typing import Optional
from fastapi import FastAPI, File, UploadFile

from pydantic import BaseModel



# class item(BaseModel):
#     category: str
#     hash_id: str


app = FastAPI()

fake_items_db = [{"category": "HairColor", "hash_id": "32eDSS2331!@de1"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
    # print(fake_items_db[item_id])
    # return {fake_items_db[item_id]}



@app.get("/img/{i_hash_id}")
def read_item(i_hash_id: str):
    return {"hash_url": "https://upload.wikimedia.org/wikipedia/en/5/53/" + i_hash_id + ".png"}


@app.post("/uploadfile/")
async def save_upload_file(file: UploadFile = File(...)):
    # global upload_folder
    file_object = file.file
    # Create empty file to copy the file_object to
    if not os.path.exists(os.path.join(pathlib.Path().absolute() / 'uploads')):
        os.makedirs(os.path.join(pathlib.Path().absolute() / 'uploads'))
    upload_folder = open(os.path.join(pathlib.Path().absolute() / 'uploads', file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    # await file.write(file.filename)
    # print(content)
    # extension = os.path.splitext(file.filename[1] _, path)
    return {"filename": file.filename}


