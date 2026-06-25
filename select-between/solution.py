(18, 'Bangkok', 'Thailand', 8305000),(18, 'Bangkok', 'Thailand', 8305000),
(19, 'Jakarta', 'Indonesia', 10560000),(19, 'Jakarta', 'Indonesia', 10560000),
(20, 'Lahore', 'Pakistan', 11120000),(20, 'Lahore', 'Pakistan', 11120000),
(21, 'Chengdu', 'China', 14040000);(21, 'Chengdu', 'China', 14040000);
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT DISTINCT cities FROM countries WHERE population BETWEEN 1,000,000 and 10,000,000; SELECT DISTINCT cities FROM countries WHERE population BETWEEN 1,000,000 and 10,000,000; 
