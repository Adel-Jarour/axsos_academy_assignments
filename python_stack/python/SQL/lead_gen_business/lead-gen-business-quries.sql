USE lead_gen_business;

SELECT SUM(amount) AS revenue
FROM billing
WHERE charged_datetime >= '2012-03-01' AND charged_datetime < '2012-04-01';

SELECT client_id, SUM(b.amount) AS total_revenue
FROM billing b
WHERE b.client_id = 2;

SELECT s.domain_name AS website, client_id
FROM sites s
WHERE s.client_id = 10;

SELECT 
	client_id,
	COUNT(*) AS number_of_websities,
    MONTH(created_datetime) AS month,
    YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 1
GROUP BY YEAR(created_datetime), MONTH(created_datetime)
ORDER BY year DESC, month DESC;

SELECT 
    client_id,
	COUNT(*) AS number_of_websities,
    MONTH(created_datetime) AS month,
    YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 20
GROUP BY YEAR(created_datetime), MONTH(created_datetime)
ORDER BY year DESC, month DESC;

SELECT 
    s.site_id,
    s.domain_name AS website,
    COUNT(l.leads_id) AS number_of_leads
FROM sites s
LEFT JOIN leads l ON s.site_id = l.site_id
    AND l.registered_datetime >= '2011-01-01'
    AND l.registered_datetime < '2011-02-16'
GROUP BY s.site_id, s.domain_name
ORDER BY number_of_leads DESC;

SELECT 
    c.client_id,
    CONCAT(c.first_name, ' ', c.last_name) AS client,
    COUNT(l.leads_id) AS number_of_leads
FROM clients c
JOIN sites s ON c.client_id = s.client_id
JOIN leads l ON s.site_id = l.site_id
    
where l.registered_datetime >= '2011-01-01'
    AND l.registered_datetime < '2012-01-01'
GROUP BY c.client_id, client
ORDER BY number_of_leads DESC;

SELECT 
	concat(c.first_name, ' ', c.last_name) AS client,
    COUNT(l.leads_id) AS number_of_leads,
    month(l.registered_datetime) AS month
FROM clients c
join sites s ON c.client_id = s.client_id
join leads l ON s.site_id = l.site_id
	
where l.registered_datetime >= '2011-01-01'
    AND l.registered_datetime < '2011-07-01'
group by c.client_id, client, month;


SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS client,
    s.domain_name AS websites,
    COUNT(l.leads_id) AS number_of_leads
FROM clients c
JOIN sites s ON c.client_id = s.client_id
JOIN leads l ON s.site_id = l.site_id
	
where l.registered_datetime >= '2011-01-01'
    AND l.registered_datetime < '2012-01-01'
GROUP BY c.client_id, client, websites
ORDER BY c.client_id ASC, number_of_leads DESC;

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS client,
    s.domain_name AS websites,
    COUNT(l.leads_id) AS number_of_leads
FROM clients c
JOIN sites s ON c.client_id = s.client_id
JOIN leads l ON s.site_id = l.site_id
	
GROUP BY c.client_id, client, websites;

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    SUM(b.amount) AS total_revenue,
    MONTH(b.charged_datetime) AS month_charged,
    YEAR(b.charged_datetime) AS year_charged
FROM clients c
JOIN billing b ON c.client_id = b.client_id
GROUP BY c.client_id, client_name, year_charged, month_charged
ORDER BY c.client_id ASC, year_charged ASC, month_charged ASC;

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    SUM(b.amount) AS total_revenue,
    MONTHNAME(b.charged_datetime) AS month_charged,
    YEAR(b.charged_datetime) AS year_charged
FROM clients c
JOIN billing b ON c.client_id = b.client_id
GROUP BY c.client_id, client_name, YEAR(b.charged_datetime), MONTH(b.charged_datetime), month_charged
ORDER BY c.client_id ASC, year_charged ASC, MONTH(b.charged_datetime) ASC;

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    GROUP_CONCAT(s.domain_name ORDER BY s.domain_name ASC SEPARATOR ', ') AS sites
FROM clients c
JOIN sites s ON c.client_id = s.client_id
GROUP BY c.client_id, client_name
ORDER BY c.client_id ASC;