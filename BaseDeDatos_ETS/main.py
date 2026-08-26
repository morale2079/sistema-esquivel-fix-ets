from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

class OrdenNueva(BaseModel):
    cliente: str
    telefono: str
    modelo: str
    imei: str
    passcode: str
    fecha: str
    falla: str
    condicion: str
    diagnostico: str
    reparacionRealizada: str
    total: str
    anticipo: str
    status: str

app = FastAPI(
    title="API Esquivel Fix",
    description="API para el sistema de control de reparaciones de telefonía móvil.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=("esquivelfix2026"),
        database="esquivel_fix"
    )

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "¡El servidor de Esquivel Fix está funcionando al 100%!"}

@app.get("/ordenes", tags=["Órdenes de Servicio"])
def obtener_ordenes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    
    consulta = """
    SELECT 
        o.folio, o.fecha_ingreso, o.falla_reportada, o.condicion_estetica, o.diagnostico, o.solucion, o.costo_total, o.anticipo, o.estado,
        e.modelo, e.imei, e.passcode, 
        c.nombre as cliente, c.telefono
    FROM Ordenes_Servicio o
    JOIN Equipos e ON o.id_equipo = e.id_equipo
    JOIN Clientes c ON e.id_cliente = c.id_cliente
    """
    
    cursor.execute(consulta)
    ordenes = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return ordenes

@app.post("/ordenes", tags=["Órdenes de Servicio"])
def guardar_orden(orden: OrdenNueva):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        costo = float(orden.total) if orden.total else 0.0
        anticipo = float(orden.anticipo) if orden.anticipo else 0.0

        cursor.execute("INSERT INTO Clientes (nombre, telefono) VALUES (%s, %s)", (orden.cliente, orden.telefono))
        id_cliente = cursor.lastrowid 

        cursor.execute("INSERT INTO Equipos (id_cliente, modelo, imei, passcode) VALUES (%s, %s, %s, %s)",
                       (id_cliente, orden.modelo, orden.imei, orden.passcode))
        id_equipo = cursor.lastrowid

        cursor.execute("""
            INSERT INTO Ordenes_Servicio
            (id_equipo, fecha_ingreso, falla_reportada, condicion_estetica, diagnostico, solucion, costo_total, anticipo, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (id_equipo, orden.fecha, orden.falla, orden.condicion, orden.diagnostico, orden.reparacionRealizada, costo, anticipo, orden.status))

        conn.commit() 
        return {"mensaje": "¡Orden guardada con éxito en la base de datos!"}
    
    except Exception as e:
        conn.rollback() 
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()