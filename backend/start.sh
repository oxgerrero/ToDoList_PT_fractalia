#!/bin/bash
echo "⏳ Ejecutando seed..."
python app/seed.py

echo "🚀 Iniciando backend..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
