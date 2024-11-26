from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello World"}


# === 1 способ ===
# fastapi dev main.py

# === 2 способ ===
# uvicorn main:app

# === 3 способ ===
# if __name__ == "__main__":
#     uvicorn.run("1run_fastapi:app", reload=True)
