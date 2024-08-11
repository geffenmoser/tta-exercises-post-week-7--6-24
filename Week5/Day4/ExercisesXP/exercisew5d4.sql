--SELECT * FROM customer LIMIT 10;
--SELECT (first_name, last_name) AS full_name FROM customer; 
--SELECT DISTINCT create_date FROM customer;
--SELECT * FROM customer ORDER BY first_name;
/*SELECT
	film_id,
	title,
	description,
	release_year,
	rental_rate
	FROM film ORDER BY rental_rate ASC*/
--SELECT address, phone FROM address WHERE district = 'Texas'
--SELECT * FROM film WHERE film_id IN (15, 150)
/*SELECT
	film_id,
	title,
	description,
	rental_duration,
	rental_rate
	FROM film WHERE title ILIKE 'Dead Poets Society'*/
/*SELECT
	film_id,
	title,
	description,
	rental_duration,
	rental_rate
	FROM film WHERE title ILIKE 'De%'*/
/*SELECT
	film_id,
	title,
	description,
	release_year,
	rental_rate
	FROM film ORDER BY rental_rate ASC
	LIMIT 10 OFFSET 10*/
/*SELECT customer.first_name, customer.last_name, customer.customer_id, payment.amount, payment.payment_date
FROM customer
FULL JOIN payment ON customer.customer_id = payment.customer_id
ORDER BY payment.customer_id*/
/*SELECT film.title FROM film
LEFT JOIN inventory on film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL*/
SELECT city.city, country.country
FROM city
INNER JOIN country
ON city.country_id = country.country_id
