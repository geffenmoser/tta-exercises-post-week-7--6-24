-- CREATE TABLE actors1(
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- 	);

-- INSERT INTO actors1 (first_name, last_name, age, number_oscars)
-- VALUES
-- 	('Matt','Damon','08/10/1970', 5),
-- 	('George', 'Clooney', '06/05/1961', 2),
-- 	('Al', 'Pacino', '04/25/1940', 1),
-- 	('Natalie', 'Portman', '06/09/1981', 1);
--SELECT * FROM actors1;
--SELECT max(actor_id) FROM actors1;

INSERT INTO actors1 (first_name, last_name, age, number_oscars)
VALUES ('','Shaq','03/6/1972');

-- ERROR:  INSERT has more target columns than expressions LINE 18: INSERT INTO actors1 (first_name, last_name, age, number_osca...