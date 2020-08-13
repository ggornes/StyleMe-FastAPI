Create a new project in Pycharm, set Conda as environment

install `fastapi` and `uvicorn`
```bash
pip install fastapi
pip install uvicorn
```

Start server:
```
uvicorn main:app --reload
```


To upload files, first install `python-multipart`
```
pip install python-multipart
```

https://fastapi.tiangolo.com/tutorial/request-files/