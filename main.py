from fastapi import FastAPI
from pydantic import BaseModel

class RootOut(BaseModel):
    appStatus: str

# Create FastAPI instance
app = FastAPI(
    title="ASD Management FastAPI",
    version="1.0.0",
)


# ROOT endpoint ========================================================================================================
@app.get("/", response_model=RootOut, tags=["root"])
def read_root():
    return {"appStatus": "ASD Management FastAPI is running"}
# ======================================================================================================================