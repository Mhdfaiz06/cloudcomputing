from fastapi import FastAPI

app = FastAPI
@app.get("/helloworld")
async def read_root():
    return {"Message":"hello world congrats "}
