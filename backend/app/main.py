from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.api import routes
from app.api import auth_routes

# Crear todas las tablas (solo si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestión de Tareas",
    description="""
    Esta API permite a los usuarios autenticados registrar tareas, listarlas, marcarlas como completadas y eliminarlas. 
    Incluye autenticación con JWT para proteger las operaciones y asegurar que cada usuario acceda solo a sus propias tareas.
    """,
    version="1.0.0",
    contact={
        "name": "Tu Nombre o Equipo",
        "email": "tucorreo@example.com",
    }
)

# CORS (ajusta origins en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas principales
app.include_router(auth_routes.router)
app.include_router(routes.router)
