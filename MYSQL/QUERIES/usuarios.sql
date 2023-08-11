SET SQL_SAFE_UPDATES = 0;

select *
from users;

DELETE 
FROM users 
WHERE id >3;

UPDATE users
SET email = "nuevo@correo.cl"
WHERE id = 1;

UPDATE users
SET email = "segundo@correo.cl"
WHERE id = 2;



select *
from users
where id = 1;

select *
from users 
where id = 3;

UPDATE users
SET last_name = 'panqueques'
WHERE id = 3;

DELETE FROM users
 WHERE id = 2;
 
 SELECT first_name
 From users;

Select *
FROM users
ORDER BY first_name DESC;
