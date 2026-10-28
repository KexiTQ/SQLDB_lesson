SELECT * FROM measurements;

SELECT date, time, temperature
FROM measurements;

SELECT *
FROM measurements
WHERE temperature < 0;

SELECT *
FROM measurements
WHERE precipitation = 'rain';

SELECT *
FROM measurements
WHERE wind_speed > 20;

SELECT *
FROM measurements
WHERE date = '2026-05-01'
ORDER BY temperature ASC;

SELECT *
FROM measurements
WHERE precipitation = 'snow'
ORDER BY temperature ASC;

SELECT *
FROM measurements
WHERE precipitation IS NULL
ORDER BY wind_speed ASC;
