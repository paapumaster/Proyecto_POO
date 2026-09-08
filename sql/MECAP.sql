CREATE DATABASE mecapp;
USE mecapp;

CREATE TABLE tipos_direccion(
    id_tipo_direccion INTEGER AUTO_INCREMENT PRIMARY KEY,
    tipo_direccion VARCHAR(25) NOT NULL,
    detalle VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_direccion PRIMARY KEY (id_tipo_direccion)

);



CREATE TABLE comunas(
    id_comuna INTEGER AUTO_INCREMENT,
    codigo_comuna VARCHAR(5) NOT NULL UNIQUE,
    nombre_comuna VARCHAR(38) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id_comuna)

);

CREATE TABLE direcciones(
    id_direccion INTEGER AUTO_INCREMENT,
    comuna INTEGER NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NULL,
    departamento VARCHAR(5) NULL,
    tipo_direccion INTEGER NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (comuna) REFERENCES comunas(id_comuna),
    CONSTRAINT fk_direcciones_tipos_direccion FOREIGN KEY (tipo_direccion) REFERENCES tipos_direccion

);