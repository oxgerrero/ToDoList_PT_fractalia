from app.db.database import SessionLocal
from app.db.models import Task

def seed():
    db = SessionLocal()
    if db.query(Task).count() == 0:
        db.add_all([
            Task(title="Tarea 1", description="Descripción 1"),
            Task(title="Tarea 2", description="Descripción 2", completed=True)
        ])
        db.commit()
    db.close()

if __name__ == "__main__":
    seed()
