create database if not exists logisticom_db;
use logisticom_db;

create table roles (
    id_rol int primary key auto_increment,
    nombre varchar(50) not null
);

create table usuarios (
    id_usuario int primary key auto_increment,
    nombre varchar(100) not null,
    email varchar(100) not null,
    contrasena varchar(64) not null,
    id_rol int not null
);

create table comisiones (
    id_comision int primary key auto_increment,
    id_usuario int not null,
    fecha date,
    estado varchar(20) not null,
    descripcion varchar(500)
);

insert into roles (nombre) values ('admin');
insert into roles (nombre) values ('usuario');

insert into usuarios (nombre, email, contrasena, id_rol) values ('Admin', 'admin@abc.com', sha2('admin123', 256), 1);
insert into usuarios (nombre, email, contrasena, id_rol) values ('Juan', 'juan@abc.com', sha2('user123', 256), 2);
