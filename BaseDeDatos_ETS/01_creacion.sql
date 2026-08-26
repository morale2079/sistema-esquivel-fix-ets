CREATE DATABASE IF NOT EXISTS esquivel_fix;
USE esquivel_fix;

CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE Equipos (
    id_equipo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    imei VARCHAR(50),
    passcode VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Ordenes_Servicio (
    folio INT AUTO_INCREMENT PRIMARY KEY,
    id_equipo INT NOT NULL,
    fecha_ingreso DATE NOT NULL,
    falla_reportada TEXT NOT NULL,
    condicion_estetica TEXT,
    diagnostico TEXT,
    solucion TEXT,
    costo_total DECIMAL(10, 2),
    anticipo DECIMAL(10, 2),
    estado VARCHAR(50) DEFAULT 'Pendiente',
    FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo)
);