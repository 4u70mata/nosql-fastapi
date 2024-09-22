# Project Cheat Sheet

## MongoDB Cheat Sheet

| Operation                  | Command                                       | Description                             |
|----------------------------|-----------------------------------------------|-----------------------------------------|
| Connect to MongoDB         | `client = MongoClient('mongodb://localhost:27017')` | Connect to MongoDB server.             |
| Create Database             | `db = client['database_name']`               | Create or switch to a database.        |
| Create Collection           | `collection = db['collection_name']`         | Create or switch to a collection.      |
| Insert Document             | `result = collection.insert_one(data)`       | Insert a single document.               |
| Insert Many Documents       | `result = collection.insert_many(data_list)`  | Insert multiple documents.              |
| Find Document               | `document = collection.find_one(query)`      | Find a single document.                 |
| Find All Documents          | `documents = collection.find()`               | Find all documents in a collection.    |
| Update Document             | `result = collection.update_one(query, update)` | Update a single document.              |
| Delete Document             | `result = collection.delete_one(query)`      | Delete a single document.               |

## Python Cheat Sheet

| Feature                     | Syntax                                       | Description                             |
|-----------------------------|-----------------------------------------------|-----------------------------------------|
| Import Module               | `import module_name`                          | Import a module.                        |
| Function Definition         | `def function_name(params):`                 | Define a function.                      |
| List Comprehension          | `[x for x in iterable if condition]`        | Create a list from an iterable.        |
| Exception Handling          | `try: ... except Exception as e:`            | Handle exceptions.                      |

## FastAPI Cheat Sheet

| Operation                  | Syntax                                       | Description                             |
|----------------------------|-----------------------------------------------|-----------------------------------------|
| Create FastAPI App         | `app = FastAPI()`                            | Initialize a FastAPI application.      |
| Define Route               | `@app.get("/path")`                          | Define a GET endpoint.                 |
| Request Body               | `async def endpoint(body: Model):`          | Define an endpoint with a request body.|
| Query Parameters            | `@app.get("/path")`<br>`def endpoint(param: str):` | Define an endpoint with query parameters. |
| Response Model             | `@app.get("/path", response_model=Model)`   | Specify response model.                 |
| Run Server                 | `uvicorn.run(app, host="0.0.0.0", port=8000)` | Start the FastAPI server.              |

## Additional Resources
- [MongoDB Documentation](https://docs.mongodb.com/manual/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Official Documentation](https://docs.python.org/3/)

Feel free to contribute or reach out if you have any questions!
