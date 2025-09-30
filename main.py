from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobData(BaseModel):
    jobIdMobile: str
    moneyPerSec: str
    petName: str

current_job = {
    "jobIdMobile": "",
    "moneyPerSec": "",
    "petName": ""
}

@app.post("/job")
async def update_job(data: JobData):
    global current_job
    current_job = {
        "jobIdMobile": data.jobIdMobile,
        "moneyPerSec": data.moneyPerSec,
        "petName": data.petName
    }
    print(f"[UPDATE] Dados recebidos: {current_job}")
    return {"message": "Dados atualizados"}

@app.get("/job")
async def get_job():
    return current_job
