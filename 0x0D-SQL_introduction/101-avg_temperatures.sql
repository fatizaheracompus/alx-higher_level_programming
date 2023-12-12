-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
