--Exercise1
--1
--SELECT language.name, language.language_id from language

/*2

SELECT film.title, film.description, language.name
FROM film
RIGHT JOIN language ON film.language_id = language.language_id*/

/*3
SELECT film.title, film.description, language.name AS language_name
FROM language
LEFT JOIN film ON film.language_id = language.language_id
ORDER BY language.name, film.title;*/

--4
CREATE TABLE new_film(id SERIAL PRIMARY KEY, film_name VARCHAR NOT NULL);
INSERT INTO new_film(film_name)
VALUES 
('Asia'),
('Here We Are'),
('Honeymood'),
('The Death of Cinema and My Father Too'),
('Sublet'),
('Golden Voices'),
('Incitement'),
('Born in Jerusalem and Still Alive'),
('Forgiveness'),
('Valley of Tears');

-- 5-6
CREATE TABLE IF NOT EXISTS customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL REFERENCES new_film(film_id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(language_id),
    title VARCHAR(255),
    score INTEGER CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert first review
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES 
(1, 1, 'Asia', 9, 'This film was an exceptional journey through the complexities of human emotion and relationships. The direction and performances were top-notch.', CURRENT_TIMESTAMP);

-- Insert second review
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES 
(2, 2, 'Here We Are', 8, 'A deeply moving narrative that keeps you engaged from start to finish. The storytelling was profound and the cinematography stunning.', CURRENT_TIMESTAMP);

--7 (the cascade reference associates them and deletes both)
--DELETE FROM new_film WHERE film_id = 1;

--exercise2
--1
--UPDATE film
--SET language_id = '3' WHERE film.title = 'Flying Hook' and film.title ='Forrest Sons'