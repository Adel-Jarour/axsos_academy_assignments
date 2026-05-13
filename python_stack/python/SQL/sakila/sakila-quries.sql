USE sakila;

SELECT first_name, last_name, email, address
FROM customer AS c
JOIN address AS a
    ON c.address_id = a.address_id
WHERE a.city_id = 312;

SELECT title, description, release_year, rating, special_features, category.name FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'comedy';

SELECT actor.actor_id, actor.first_name, actor.last_name, title, description, release_year FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = '5';

SELECT first_name, last_name, email, address FROM customer
JOIN address
    ON customer.address_id = address.address_id
WHERE customer.store_id = 1
AND address.city_id IN (1, 42, 312, 459);

SELECT title, description, release_year, rating, special_features
FROM film
JOIN film_actor
    ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 15
AND film.rating = 'G'
AND film.special_features LIKE '%Behind the Scenes%';

SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film.film_id = 369;

SELECT title, description, release_year, rating, special_features, category.name FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Drama' AND rental_rate = 2.99;

SELECT title, description, release_year, rating, special_features, category.name, actor.actor_id, actor.last_name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action'
AND actor.first_name = 'SANDRA'
AND actor.last_name = 'KILMER';
