# Diccionario de Datos - Esquivel Fix

Este documento describe la estructura de la base de datos `esquivel_fix`.

## Tabla: `Clientes`
Almacena la información de contacto básica de los clientes del taller.

| Nombre de Columna | Tipo de Dato | Longitud | Restricciones | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `id_cliente` | INT | N/A | PRIMARY KEY, AUTO_INCREMENT | Identificador único del cliente. |
| `nombre` | VARCHAR | 100 | NOT NULL | Nombre completo del cliente. |
| `telefono` | VARCHAR | 15 | NOT NULL | Número de contacto del cliente (generalmente WhatsApp). |

---

## Tabla: `Equipos`
Almacena la información de los dispositivos móviles que los clientes dejan para reparación o diagnóstico.

| Nombre de Columna | Tipo de Dato | Longitud | Restricciones | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `id_equipo` | INT | N/A | PRIMARY KEY, AUTO_INCREMENT | Identificador único del dispositivo. |
| `id_cliente` | INT | N/A | FOREIGN KEY, NOT NULL | Llave foránea vinculada a la tabla `Clientes`. |
| `marca` | VARCHAR | 50 | NOT NULL | Marca del dispositivo (Ej. Apple, Samsung, Motorola). |
| `modelo` | VARCHAR | 100 | NOT NULL | Modelo específico del dispositivo (Ej. iPhone 13 Pro Max). |
| `color` | VARCHAR | 50 | NOT NULL | Color exterior del dispositivo. |
| `imei` | VARCHAR | 50 | NULL | Número de serie o IMEI del dispositivo para su identificación legal/física. |
| `passcode` | VARCHAR | 50 | NULL | Contraseña, PIN o patrón de desbloqueo proporcionado para realizar pruebas. |

---

## Tabla: `Ordenes_Servicio`
Almacena la información transaccional y técnica del servicio prestado a un equipo.

| Nombre de Columna | Tipo de Dato | Longitud | Restricciones | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `folio` | INT | N/A | PRIMARY KEY, AUTO_INCREMENT | Número de folio único de la orden de servicio. |
| `id_equipo` | INT | N/A | FOREIGN KEY, NOT NULL | Llave foránea vinculada a la tabla `Equipos`. |
| `fecha_ingreso` | DATE | N/A | NOT NULL | Fecha en la que se recibió el equipo en el taller. |
| `falla_reportada` | TEXT | N/A | NOT NULL | Descripción que hace el cliente sobre lo que le falla al dispositivo. |
| `condicion_estetica`| TEXT | N/A | NULL | Notas del técnico sobre el estado físico inicial del dispositivo (Check-in). |
| `diagnostico` | TEXT | N/A | NULL | Reporte técnico posterior a la revisión del dispositivo. |
| `solucion` | TEXT | N/A | NULL | Descripción de la reparación o servicio realizado. |
| `costo_total` | DECIMAL | 10, 2 | NULL | Costo total del servicio en MXN. |
| `anticipo` | DECIMAL | 10, 2 | NULL | Abono o anticipo dejado por el cliente en MXN. |
| `estado` | VARCHAR | 50 | DEFAULT 'Pendiente'| Estado actual del equipo (Ej. Pendiente, En Revisión, Esperando Pieza, Listo, Entregado). |
