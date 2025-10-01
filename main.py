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

# Lista de jobs recebidos (mais recente no topo)
jobs = []

@app.post("/job")
async def add_job(data: JobData):
    jobs.insert(0, {
        "jobIdMobile": data.jobIdMobile,
        "moneyPerSec": data.moneyPerSec,
        "petName": data.petName
    })
    # Limite opcional: só guarda os 30 mais recentes
    if len(jobs) > 30:
        jobs.pop()
    print(f"[UPDATE] Dados recebidos: {data}")
    return {"message": "Job adicionado"}

@app.get("/job")
async def get_jobs():
    return jobs
