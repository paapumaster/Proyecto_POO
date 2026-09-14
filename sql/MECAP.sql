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


ALTER TABLE tipos_direccion COMMENT = 'Tipos de direccion, Domiciliario, laboral, academico, oficina'
ALTER TABLE comunas COMMENT = 'Datos d ecomunas de chile segun el codigo unico territorial (CUT) de'
ALTER TABLE direcciones COMMENT = 'Informacion de direcciones para asociar a talleres, clientes'
ALTER TABLE direcciones ADD habilitado TINYINT NOT NULL DEFAULT 1;


CREATE TABLE talleres(
    id_taller INTEGER AUTO_INCREMENT,
    nombre_taller VARCHAR(50) NOT NULL,
    direccion,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_talleres PRIMARY KEY (id_taller)
    COMMENT = 'Informacion de talleres mecanicos';


)




CREATE TABLE tipos_mecanicos(
    id_tipo_mecanico INTEGER AUTO_INCREMENT,
    tipo_mecanico VARCHAR(25) NOT NULL,
    detalle VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_mecanicos PRIMARY KEY (id_tipo_mecanico)
    COMMENT = 'Informacion de tipos de mecanico para a sociar a mecanicos de talleres';
)


CREATE TABLE mecanicos(
    rut INTEGER NOT NULL UNIQUE,
    correo VARCHAR(255) NULL,
    telefono VARCHAR(15) NULL,
    digito_verificador CMAR(i) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    fecha_contrato DATE NOT NULL,
    salario DECIMAL NULL,
    direccion INTEGER,
    tipo_mecanico INTEGER,

    CONSTRAINT pk_mecanico PRIMARY KEY (rut),
    CONSTRAINT fk_mecanicos_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
    CONSTRAINT fk_mecanicos_tipomecanico FOREIGN KEY (tipo_mecanico) REFERENCES tipos_mecanicos(id_tipo_mecanico)
) 


CREATE TABLE talleres_mecanicos(
    id_taller_mecanico INTEGER AUTO_INCREMENT,
    mecanico INTEGER NOT NULL,
    taller INTEGER NOT NULL,
    habilitado TINYINT NOT NULL,

    CONSTRAINT pk_talleres_mecanicos PRIMARY KEY (id_taller_mecanico),
    CONSTRAINT fk_talleresmecanicos_taller FOREIGN KEY (taller) REFERENCES talleres(id_taller),
    CONSTRAINT fk_talleresmecanicos_mecanico FOREIGN KEY (mecanico) REFERENCES mecanicos(rut),
    )



CREATE TABLE parametros(
    id_parametro INTEGER AUTO_INCREMENT,
    tipo_parametro VARCHAR(30) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,

    CONSTRAINT pk_parametros PRIMARY KEY (id_parametro)
) COMMENT = 'Informacion parametrica usada dentro de la aplicacion: Combustible, tipo d evehiculo, etc';


ALTER TABLE parametros ADD habilitado TINYINT NOT NULL DEFAULT 1; 