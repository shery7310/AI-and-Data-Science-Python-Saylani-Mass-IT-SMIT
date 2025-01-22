
# Running a fastapi server using both virtualenv and poetry (Any Operating System)

##### virtualenv

In case of virtualenv we can use pip to install uvicorn and fastapi i.e. 

```python3
pip install fastapi
pip install uvicorn
```

##### poetry

```python3
poetry add fastapi
poetry add uvicorn
```

Now to run a fast api server in virtualenv or poetry environment we need to paste this code into any python file in my case the file is called randomcode.py 

```python3
from fastapi import FastAPI

    # Create an instance of the FastAPI class
    app = FastAPI()

    # Define a root route
    @app.get("/")
    async def read_root():
        return {"message": "hello, world!"}

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
```

To simply run this code for fast api we need to run this command in IDE's terminal:

<code>uvicorn main:app --reload</code>

As soon as we run this our fastapi server will be up and running at 127.0.0.1 IP which is also known as localhost and the port will be 8000. 
For a more detailed approach to understand this code we can check out [KDNuggets](https://www.kdnuggets.com/beginners-guide-to-fastapi) and it is a better approach to follow fastapi's official [documentation](https://fastapi.tiangolo.com/tutorial/first-steps/) as fastapi is well-known for having a good documentation.  