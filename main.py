from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes_rol import rol
from routes.routes_usuario import usuario
from routes.routes_auto import auto
from routes.routes_servicios import servicio
from routes.routes_auto_servicio import auto_servicio

app = FastAPI(
    title="API Segura de Administración de un autolavado",
    description="API robusta para la gestión de vehículos y servicios de limpieza.",
    version="1.0.0"
)

# 1. Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Ruta de bienvenida
@app.get("/", tags=["Inicio"])
def home():
    return {"message": "API de Autolavado activa y funcionando"}

# 3. Inclusión de Routers
app.include_router(usuario)
app.include_router(rol)
app.include_router(auto)
app.include_router(servicio)
app.include_router(auto_servicio)