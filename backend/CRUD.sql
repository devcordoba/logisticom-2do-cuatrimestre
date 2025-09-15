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