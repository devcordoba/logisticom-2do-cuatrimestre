create database if not exists logisticom_db;
use logisticom_db;

create table roles (
    id_rol int primary key auto_increment,
    nombre varchar(50) not null unique
);

create table usuarios (
    id_usuario int primary key auto_increment,
    nombre varchar(100) not null,
    email varchar(100) not null unique,
    contrasena varchar(64) not null,
    id_rol int not null,
    constraint fk_usuarios_roles foreign key (id_rol) references roles(id_rol)
);

create table comisiones (
    id_comision int primary key auto_increment,
    id_usuario int not null,
    fecha date default (current_date),
    estado varchar(20) not null default 'Pendiente',
    descripcion varchar(500),
    constraint fk_comisiones_usuarios foreign key (id_usuario) references usuarios(id_usuario)
);

insert into roles (nombre) values ('admin');
insert into roles (nombre) values ('usuario');

insert into usuarios (nombre, email, contrasena, id_rol) values ('Admin', 'admin@abc.com', sha2('admin123', 256), 1);
insert into usuarios (nombre, email, contrasena, id_rol) values ('Juan', 'juan@abc.com', sha2('user123', 256), 2);
