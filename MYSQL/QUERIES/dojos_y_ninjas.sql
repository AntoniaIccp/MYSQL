-- Creando 3 usuarios.
insert into dojos (name)
values
("Ignacio"),
("Antonia"),
("Dojo");

-- elimina los 3 dojos que acabas de crear
delete
from dojos
where id >= 1;

-- Crear 3 dojos nuevos
insert into dojos (name)
values
("Ignacio"),
("Antonia"),
("Dojo");

----recupera todos los ninjas del primer dojo
select *
from ninjas
join dojos
on ninjas.dojo_id = dojos.id
where dojo_id = 4;

----recupera todos los ninjas del ultimo dojo.
from ninjas
join dojos
on ninjas.dojo_id = dojos.id
where dojo_id = 6;

-- recupera el dojo del último ninja
select *
from dojos
join ninjas
on dojos.id = ninjas.dojo_id
where id = 16;