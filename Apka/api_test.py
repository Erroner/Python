from fastapi import FastAPI
app = FastAPI()

@app.get("/abc")
def hello():
  return {"output"}
