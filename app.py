from fastapi import FastAPI, APIRouter, HTTPException
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# Conecta ao seu banco de dados
mongo_url = "mongodb://localhost:27017"
client = AsyncIOMotorClient(mongo_url)
db = client["test_database"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para listar os cursos no seu Dashboard
@app.get("/api/courses")
async def get_courses():
    courses = await db.courses.find({}, {"_id": 0}).to_list(100)
    return courses

# Rota para buscar uma aula específica
@app.get("/api/courses/{course_id}")
async def get_course(course_id: str):
    course = await db.courses.find_one({"id": course_id}, {"_id": 0})
    if not course:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return course

# Rota para salvar o progresso das advogadas/alunas
@app.post("/api/progress/update")
async def update_progress(data: dict):
    await db.user_progress.update_one(
        {"user_id": data["user_id"], "course_id": data["course_id"]},
        {"$set": {"completed_lessons": data["completed_lessons"]}},
        upsert=True
    )
    return {"success": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
