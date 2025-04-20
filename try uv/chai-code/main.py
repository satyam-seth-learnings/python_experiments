from fastapi import FastAPI
import uvicorn

def main():
    print("Hello from chai-code!")
    uvicorn.run(app, host="0.0.0.0", port=8000)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Chai Code!"}

if __name__ == "__main__":
    main()
