USE world;

SELECT c.name, l.language, l.percentage
FROM languages l
JOIN countries c ON l.country_id = c.id
WHERE l.language = 'Slovene'
ORDER BY l.percentage DESC;

SELECT c.name, COUNT(ct.id) AS cities
FROM countries c
JOIN cities ct ON c.id = ct.country_id
GROUP BY c.id, c.name
ORDER BY cities DESC;

SELECT ct.name, ct.population, ct.country_id
FROM cities ct
JOIN countries c ON ct.country_id = c.id
WHERE c.name = 'Mexico' AND ct.population > 500000
ORDER BY ct.population DESC;

SELECT c.name, l.language, l.percentage
FROM languages l
JOIN countries c ON l.country_id = c.id
WHERE l.percentage > 89
ORDER BY l.percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy'
  AND capital > 200
  AND life_expectancy > 75;
  
SELECT c.name AS country_name, ct.name AS city_name, ct.district, ct.population
FROM cities ct
JOIN countries c ON ct.country_id = c.id
WHERE c.name = 'Argentina'
  AND ct.district = 'Buenos Aires'
  AND ct.population > 500000;
  
SELECT region, COUNT(id) AS countries
FROM countries
GROUP BY region
ORDER BY countries DESC;