from app.db.database import SessionLocal, engine, Base
from app.db.models import User, Task
from app.auth import get_password_hash

# Asegura que las tablas existan antes de insertar
Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    clave = "Qwe123as"
    # Evitar duplicados si ya existen
    if db.query(User).count() > 0:
        print("Usuarios ya existen. Seed cancelado.")
        db.close()
        return

    # Crear usuarios
    user1 = User(
        username="usuario1",
        hashed_password=get_password_hash(clave)
    )
    user2 = User(
        username="usuario2",
        hashed_password=get_password_hash(clave)
    )

    db.add_all([user1, user2])
    db.commit()

    # Refrescar para obtener IDs
    db.refresh(user1)
    db.refresh(user2)

    # Crear tareas para cada usuario
    tasks = [
        Task(title="Tarea de Alice 1", description="Descripcion 1", owner_id=user1.id),
        Task(title="Tarea de Alice 2", description="Descripcion 2", completed=True, owner_id=user1.id),
        Task(title="Tarea de Bob 1", description="Descripcion 3", owner_id=user2.id),
    ]

    db.add_all(tasks)
    db.commit()
    db.close()

    print("Se insertaron 2 usuarios y tareas de prueba.")

if __name__ == "__main__":
    seed()
