USE esquivel_fix;

INSERT INTO Clientes (nombre, telefono) VALUES 
('Carlos Mendoza', '5543902187'),
('Ana López', '5576129843');

INSERT INTO Equipos (id_cliente, modelo, imei, passcode) VALUES 
(1, 'iPhone 11 Rojo', '359182736451029', '123456'),
(2, 'Samsung Galaxy S21', '354829103847562', 'Patrón Z');

INSERT INTO Ordenes_Servicio (id_equipo, fecha_ingreso, falla_reportada, condicion_estetica, diagnostico, solucion, costo_total, anticipo, estado) VALUES 
(1, '2026-08-25', 'La batería dura muy poco y se calienta.', 'Pantalla con ligeros rayones', 'Batería degradada al 70%', 'Cambio de batería OEM', 850.00, 200.00, 'Listo'),
(2, '2026-08-26', 'No carga al conectarlo.', 'Golpe en esquina inferior derecha', 'Centro de carga dañado por humedad', 'Reemplazo de centro de carga (Flex)', 600.00, 0.00, 'En Revisión');