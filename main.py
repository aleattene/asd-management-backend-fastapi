from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(title="ASD Management FastAPI")


# ROOT endpoint ========================================================================================================
@app.get("/")
def read_root():
    return {"appStatus": "ASD Management FastAPI is running"}
# ======================================================================================================================