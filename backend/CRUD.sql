-- dar de alta un usuario
insert into usuarios (nombre, email, contrasena, id_rol)
values ('Lucia Ramos', 'lucia@example.com', sha2('clave123', 256), 2);

-- ver todos los usuarios
select u.id_usuario, u.nombre, u.email, r.nombre as rol
from usuarios u
join roles r on u.id_rol = r.id_rol;

-- actualizar nombre a usuario
update usuarios set nombre = 'Juan' where id_usuario = 1;

-- actualizar rol a usuario
update usuarios set id_rol = 1 where id_usuario = 1;

-- eliminar un usuario
delete from usuarios where id_usuario = 1;

-- =====================
-- Operaciones de Comisiones
-- =====================

-- crear una comisión
insert into comisiones (id_usuario, descripcion) values (2, 'Entrega de documentación');

-- listar comisiones propias con JOIN
select c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion
from comisiones c
join usuarios u on c.id_usuario = u.id_usuario
where c.id_usuario = 2
order by c.fecha desc;

-- listar todas las comisiones con JOIN
select c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion
from comisiones c
join usuarios u on c.id_usuario = u.id_usuario
order by c.fecha desc;

-- despachar una comisión
update comisiones set estado = 'Despachado' where id_comision = 1;