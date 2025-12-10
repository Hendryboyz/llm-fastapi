# LLM-FastAPI
Practice integrate LLM and related frameworks to RESTful API in 30 days.

## Command

```bash
# Start the App
uvicorn src.main:app --reload
```

---

## Notes

### Day 1

#### Why use FastAPI

* Leverage Starlette and Pydantic to make async request and type checking request possible
    * async: FastAPI trust developers not executing block I/O operations in `async` routes
    * sync: run `sync` request to **threadpool** and blocking I/O operations **won't** stop event loop from executing tasks
* Provide easy to learn documents to pick this framework really quick
* Generate Swagger UI automatically
* Simple but not Naive. Allow developers to build from simple personal project to enterprise level application.

#### FastAPI async model

* native async design(not like Flask)
* ASGI
* support `sync` routes to handle blocking I/O operations in different thread. other requests can still be processed.
* async allow FastAPI high concurrency jobs more efficient.

:blub: In conclusion, FastAPI is an quick and suitable framework to develop an FastAPI with LLM

