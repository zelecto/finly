#!/bin/bash

echo "Deteniendo contenedor anterior..."
docker stop finly 2>/dev/null
docker rm finly 2>/dev/null

echo "Construyendo imagen..."
docker build -t finly-app .

echo "Iniciando contenedor..."
docker run -d -p 80:80 --name finly finly-app

echo ""
echo "Esperando que los servicios inicien..."
sleep 5

echo ""
echo "=========================================="
echo "✅ APLICACIÓN LISTA"
echo "=========================================="
echo ""
echo "🌐 Frontend (Flask):"
echo "   http://localhost/"
echo ""
echo "🚀 API (FastAPI):"
echo "   http://localhost/api/"
echo ""
echo "=========================================="
echo ""
echo "📋 Comandos útiles:"
echo "   Ver logs:    docker logs -f finly"
echo "   Detener:     docker stop finly"
echo "   Reiniciar:   docker restart finly"
echo "=========================================="
