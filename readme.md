## 📌 README.md – ToDo List Fullstack App Fractalia

# ✅ ToDo List Fullstack App

Aplicación web de gestión de tareas desarrollada con **Angular + FastAPI**, autenticación con **JWT**, base de datos SQLite y contenedores **Docker** para despliegue completo.

---

## 🚀 Funcionalidades

### 🔐 Autenticación
- Registro y login de usuarios
- Token JWT para sesiones seguras
- Validación de contraseña con mayúscula, minúscula y mínimo 8 caracteres

### 📝 Gestión de Tareas
- Crear, leer, actualizar y eliminar tareas
- Cada tarea pertenece a un usuario
- Marcar tareas como completadas
- Interfaz moderna y responsiva

### 🌍 Docker & Seed
- Backend y frontend dockerizados
- Seed automático al iniciar: crea 2 usuarios (`usuario1`, `usuario`) con tareas preasignadas
- claves por defecto `Qwe123as`

---

## 🧱 Tecnologías

- **Frontend**: Angular 17+, SCSS, Bootstrap (sin Tailwind)
- **Backend**: FastAPI, SQLAlchemy, JWT, Pydantic
- **DB**: SQLite (por defecto)
- **Contenedores**: Docker + Docker Compose

---

## ⚙️ Instalación local (sin Docker)

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python app/seed.py
uvicorn app.main:app --reload
````

### Frontend (Angular)

```bash
cd frontend
npm install
npm run start
```

---

## 🐳 Instalación con Docker

```bash
docker-compose build --no-cache
docker-compose up
```

* Frontend: [http://localhost:4200](http://localhost:4200)
* Backend API: [http://localhost:8000](http://localhost:8000)
* Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

> La semilla se ejecuta automáticamente al arrancar el backend.

---

## 👥 Usuarios por defecto

| Usuario | Contraseña |
| ------- | ---------- |
| usuario1| Qwe123as   |
| usuario2| Qwe123as   |

---

## ✅ Validaciones de seguridad

* Contraseña: mínimo 8 caracteres, al menos una mayúscula y una minúscula
* Rutas de tareas protegidas por JWT
* Token almacenado localmente en frontend

---

## 📁 Estructura del proyecto

```
to-do-app/
├── backend/
│   ├── app/
│   ├── seed.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── angular.json
├── docker-compose.yml
└── README.md
```

## 📌 Autor

* 👤 **David Gomez**
* 🌐 **GitHub** - [GitHub](https://github.com/oxgerrero/)
* 📖 Estudiante
* 🏫 Universidad de Cundinamarca
* 🛠️ Ingeniería de Sistemas y Computación + Especialización en Analítica y ciencia de datos

---