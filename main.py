from fastapi import FastAPI, Body
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

# Lista de jobs recebidos
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

# NOVO: Endpoint para descartar/remover jobId da lista
@app.post("/job/discard")
async def discard_job(data: dict = Body(...)):
    job_id = data.get("jobId")
    global jobs
    before = len(jobs)
    jobs = [job for job in jobs if job.get("jobIdMobile") != job_id]
    after = len(jobs)
    print(f"[DISCARD] Removido? {before-after>0} | jobId: {job_id}")
    return {"ok": True, "removed": job_id}
