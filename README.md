# Sistema Taller - Esquivel Fix

Sistema web desarrollado para la gestión, control de órdenes de servicio, recepción de equipos y diagnóstico técnico en un taller de reparación de telefonía móvil.

Autor
Alan Miranda Esquivel

---

 Tecnologías Utilizadas
Backend: Python, FastAPI, Uvicorn, Pydantic, MySQL Connector.
Base de Datos: MySQL (Arquitectura relacional con normalización de tablas).
Frontend: HTML5, Tailwind CSS, React (implementado vía Babel Standalone).

---

Estructura del Repositorio
* `01_creacion.sql`: Script DDL para la creación del esquema de base de datos y sus tablas relacionales (`Clientes`, `Equipos`, `Ordenes_Servicio`).
* `02_rollbacks_creacion.sql`: Script de seguridad para la eliminación limpia de las tablas y la base de datos.
* `03_poblado.sql`: Script DML con datos de prueba para pruebas iniciales del sistema.
* `04_rollbacks_poblado.sql`: Script para el vaciado seguro de los registros manteniendo la estructura intacta.
* `main.py`: Servidor de la API REST construido con FastAPI, encargado de manejar las operaciones de lectura y escritura con la base de datos.
* `index.html`: Interfaz gráfica interactiva en React con un tablero de control dinámico y generación de órdenes imprimibles.

---

Requisitos Previos
1. Python 3.8 o superior instalado en el equipo.
2. Servidor MySQL local activo (por ejemplo, mediante MySQL Workbench o XAMPP).
3. Instalación de las librerías necesarias de Python ejecutando el siguiente comando en tu terminal:
   ```bash
   pip install fastapi uvicorn mysql-connector-python pydantic
