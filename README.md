Create a new project in Pycharm, set Conda as environment

```bash
pip install fastapi
pip install uvicorn
```
```
uvicorn main:app --reload
```

To upload files, first install `python-multipart`
```
pip install python-multipart
```
The files will be uploaded as "form data".

https://fastapi.tiangolo.com/tutorial/request-files/