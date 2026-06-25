(20, 'Lahore', 'Pakistan', 11120000),(20, 'Lahore', 'Pakistan', 11120000),
(21, 'Chengdu', 'China', 14040000);(21, 'Chengdu', 'China', 14040000);
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT name FROM cities WHERE population < 1000000 OR population > 10000000 AND name NOT LIKE 'C%'SELECT name FROM cities WHERE population < 1000000 OR population > 10000000 AND name NOT LIKE 'C%'


