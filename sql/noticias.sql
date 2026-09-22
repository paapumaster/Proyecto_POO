-- ==========================================
-- ESTRUCTURA DE LA BASE DE DATOS
-- Plataforma de Noticias Digital
-- Compatible con MySQL / phpMyAdmin
-- ==========================================

CREATE DATABASE IF NOT EXISTS plataforma_noticias
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE plataforma_noticias;

-- 1. Tabla de Roles de Usuario
CREATE TABLE roles (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 2. Tabla de Usuarios (Periodistas, Editores, Lectores)
CREATE TABLE usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
rol_id INT NOT NULL,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,
fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 3. Tabla de Categorías
CREATE TABLE categorias (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL UNIQUE,
slug VARCHAR(120) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 4. Tabla de Etiquetas (Tags)
CREATE TABLE etiquetas (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL UNIQUE,
slug VARCHAR(60) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 5. Tabla de Noticias
-- Estado soporta el flujo de creación, revisión y publicación
CREATE TABLE noticias (
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(255) NOT NULL,
contenido LONGTEXT NOT NULL,
estado ENUM('borrador', 'en_revision', 'publicada', 'rechazada', 'archivada') DEFAULT 'borrador',
fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
fecha_publicacion DATETIME NULL
) ENGINE=InnoDB;

-- 6. Relación N:M (Noticias <-> Periodistas / Autores)
-- Permite que una noticia tenga múltiples coautores
CREATE TABLE noticia_autores (
noticia_id INT NOT NULL,
usuario_id INT NOT NULL,
PRIMARY KEY (noticia_id, usuario_id),
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 7. Relación N:M (Noticias <-> Categorías)
CREATE TABLE noticia_categorias (
noticia_id INT NOT NULL,
categoria_id INT NOT NULL,
PRIMARY KEY (noticia_id, categoria_id),
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 8. Relación N:M (Noticias <-> Etiquetas)
CREATE TABLE noticia_etiquetas (
noticia_id INT NOT NULL,
etiqueta_id INT NOT NULL,
PRIMARY KEY (noticia_id, etiqueta_id),
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (etiqueta_id) REFERENCES etiquetas(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 9. Tabla de Recursos Multimedia (Imágenes, Videos, Documentos)
CREATE TABLE recursos (
id INT AUTO_INCREMENT PRIMARY KEY,
noticia_id INT NOT NULL,
url_recurso VARCHAR(255) NOT NULL,
tipo ENUM('imagen', 'video', 'documento', 'audio') NOT NULL DEFAULT 'imagen',
leyenda VARCHAR(255) NULL,
fecha_subida DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 10. Tabla de Comentarios de Lectores
CREATE TABLE comentarios (
id INT AUTO_INCREMENT PRIMARY KEY,
noticia_id INT NOT NULL,
usuario_id INT NOT NULL,
comentario TEXT NOT NULL,
fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 11. Tabla de Contenido de Interés (Favoritos / Noticias Guardadas)
CREATE TABLE noticias_guardadas (
usuario_id INT NOT NULL,
noticia_id INT NOT NULL,
fecha_guardado DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (usuario_id, noticia_id),
FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;