from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def seed_data():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_database"]
    
    # Dados do Curso de Fotografia para as advogadas
    course = {
        "id": "foto-mobile-01",
        "title": "Fotografia Mobile: V8 God Mode",
        "image_url": "https://images.pexels.com/photos/1744790/pexels-photo-1744790.jpeg",
        "lessons": [
            {"id": "aula-1", "title": "Iluminação e Ângulo", "content": "Texto da aula 1..."},
            {"id": "aula-2", "title": "Edição com IA", "content": "Texto da aula 2..."}
        ]
    }
    
    await db.courses.update_one({"id": course["id"]}, {"$set": course}, upsert=True)
    print("Cursos inseridos com sucesso!")

if __name__ == "__main__":
    asyncio.run(seed_data())
