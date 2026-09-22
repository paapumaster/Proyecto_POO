-- ==========================================
-- DATOS INICIALES Y DE PRUEBA
-- Plataforma de Noticias Digital
-- ==========================================USE plataforma_noticias;-- 1. Insertar Roles base
INSERT INTO roles (id, nombre) VALUES
(1, 'Administrador'),
(2, 'Editor'),
(3, 'Periodista'),
(4, 'Lector');-- 2. Insertar Categorías básicas
INSERT INTO categorias (nombre, slug) VALUES
('Nacional', 'nacional'),
('Internacional', 'internacional'),
('Tecnología', 'tecnologia'),
('Deportes', 'deportes'),
('Cultura', 'cultura');-- 3. Insertar Etiquetas básicas
INSERT INTO etiquetas (nombre, slug) VALUES
('Última Hora', 'ultima-hora'),
('Exclusivo', 'exclusivo'),
('Opinión', 'opinion'),
('Tendencias', 'tendencias');-- 4. Usuarios de prueba (1 Periodista, 1 Editor, 1 Lector)
-- Nota: Contraseñas simuladas de prueba
INSERT INTO usuarios (rol_id, nombre, email, password) VALUES
(3, 'Juan Pérez', 'juan.periodista@prensa.com', '$2y$10$abcdef1234567890demo1'),
(2, 'María Gómez', 'maria.editora@prensa.com', '$2y$10$abcdef1234567890demo2'),
(4, 'Carlos Lector', 'carlos.lector@email.com', '$2y$10$abcdef1234567890demo3');