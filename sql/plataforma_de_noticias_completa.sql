-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 28-09-2026 a las 16:04:00
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26


CREATE DATABASE IF NOT EXISTS plataforma_noticias;
USE plataforma_noticias;



SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `plataforma_noticias`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE IF NOT EXISTS `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id`, `nombre`, `slug`) VALUES
(1, 'Nacional', 'nacional'),
(2, 'Internacional', 'internacional'),
(3, 'Tecnología', 'tecnologia'),
(4, 'Deportes', 'deportes'),
(5, 'Cultura', 'cultura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
CREATE TABLE IF NOT EXISTS `comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `noticia_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `comentario` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `noticia_id` (`noticia_id`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `etiquetas`
--

DROP TABLE IF EXISTS `etiquetas`;
CREATE TABLE IF NOT EXISTS `etiquetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `etiquetas`
--

INSERT INTO `etiquetas` (`id`, `nombre`, `slug`) VALUES
(1, 'Última Hora', 'ultima-hora'),
(2, 'Exclusivo', 'exclusivo'),
(3, 'Opinión', 'opinion'),
(4, 'Tendencias', 'tendencias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticias`
--

DROP TABLE IF EXISTS `noticias`;
CREATE TABLE IF NOT EXISTS `noticias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contenido` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` enum('borrador','en_revision','publicada','rechazada','archivada') COLLATE utf8mb4_unicode_ci DEFAULT 'borrador',
  `fecha_creacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `fecha_publicacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `noticias`
--

INSERT INTO `noticias` (`id`, `titulo`, `contenido`, `estado`, `fecha_creacion`, `fecha_publicacion`) VALUES
(1, 'La noticia', 'esta es una noticia muy impactante que cambiara como vemos el dia a dia en nuestra vida', 'publicada', '2026-09-28 12:30:59', '2026-09-28 12:32:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticias_guardadas`
--

DROP TABLE IF EXISTS `noticias_guardadas`;
CREATE TABLE IF NOT EXISTS `noticias_guardadas` (
  `usuario_id` int NOT NULL,
  `noticia_id` int NOT NULL,
  `fecha_guardado` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`usuario_id`,`noticia_id`),
  KEY `noticia_id` (`noticia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia_autores`
--

DROP TABLE IF EXISTS `noticia_autores`;
CREATE TABLE IF NOT EXISTS `noticia_autores` (
  `noticia_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`noticia_id`,`usuario_id`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `noticia_autores`
--

INSERT INTO `noticia_autores` (`noticia_id`, `usuario_id`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia_categorias`
--

DROP TABLE IF EXISTS `noticia_categorias`;
CREATE TABLE IF NOT EXISTS `noticia_categorias` (
  `noticia_id` int NOT NULL,
  `categoria_id` int NOT NULL,
  PRIMARY KEY (`noticia_id`,`categoria_id`),
  KEY `categoria_id` (`categoria_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia_etiquetas`
--

DROP TABLE IF EXISTS `noticia_etiquetas`;
CREATE TABLE IF NOT EXISTS `noticia_etiquetas` (
  `noticia_id` int NOT NULL,
  `etiqueta_id` int NOT NULL,
  PRIMARY KEY (`noticia_id`,`etiqueta_id`),
  KEY `etiqueta_id` (`etiqueta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recursos`
--

DROP TABLE IF EXISTS `recursos`;
CREATE TABLE IF NOT EXISTS `recursos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `noticia_id` int NOT NULL,
  `url_recurso` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo` enum('imagen','video','documento','audio') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'imagen',
  `leyenda` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_subida` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `noticia_id` (`noticia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Editor'),
(4, 'Lector'),
(3, 'Periodista');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol_id` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `rol_id` (`rol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `rol_id`, `nombre`, `email`, `password`, `fecha_registro`) VALUES
(1, 3, 'Juan Pérez', 'juan.periodista@prensa.com', '$2y$10$abcdef1234567890demo1', '2026-09-28 12:06:37'),
(2, 2, 'María Gómez', 'maria.editora@prensa.com', '$2y$10$abcdef1234567890demo2', '2026-09-28 12:06:37'),
(3, 4, 'Carlos Lector', 'carlos.lector@email.com', '$2y$10$abcdef1234567890demo3', '2026-09-28 12:06:37'),
(4, 2, 'Pedro Periodista', 'periodista@test.com', '1234', '2026-09-28 12:20:00'),
(5, 3, 'Elena Editora', 'editora@test.com', '1234', '2026-09-28 12:20:00'),
(6, 4, 'Lucas Lector', 'lector@test.com', '1234', '2026-09-28 12:20:00');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD CONSTRAINT `comentarios_ibfk_1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `comentarios_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `noticias_guardadas`
--
ALTER TABLE `noticias_guardadas`
  ADD CONSTRAINT `noticias_guardadas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `noticias_guardadas_ibfk_2` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `noticia_autores`
--
ALTER TABLE `noticia_autores`
  ADD CONSTRAINT `noticia_autores_ibfk_1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `noticia_autores_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `noticia_categorias`
--
ALTER TABLE `noticia_categorias`
  ADD CONSTRAINT `noticia_categorias_ibfk_1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `noticia_categorias_ibfk_2` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `noticia_etiquetas`
--
ALTER TABLE `noticia_etiquetas`
  ADD CONSTRAINT `noticia_etiquetas_ibfk_1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `noticia_etiquetas_ibfk_2` FOREIGN KEY (`etiqueta_id`) REFERENCES `etiquetas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `recursos`
--
ALTER TABLE `recursos`
  ADD CONSTRAINT `recursos_ibfk_1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
