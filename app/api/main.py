from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "********** SIMPLE FASTAPI **********"

@app.get("/api/health")
def read_health():
    return {"status" : "ok"}

print("Finished!")

