(3, 'Berlin', 'London', 200),(3, 'Berlin', 'London', 200),
(4, 'London', 'Berlin', 120),(4, 'London', 'Berlin', 120),
(5, 'Paris', 'Berlin', 110),(5, 'Paris', 'Berlin', 110),
(6, 'Berlin', 'Paris', 130),(6, 'Berlin', 'Paris', 130),
(7, 'London', 'Paris', 90),(7, 'London', 'Paris', 90),
(8, 'Paris', 'London', 140),(8, 'Paris', 'London', 140),
(9, 'Berlin', 'London', 180),(9, 'Berlin', 'London', 180),
(10, 'London', 'Berlin', 115),(10, 'London', 'Berlin', 115),
(11, 'London', 'Paris', 105),(11, 'London', 'Paris', 105),
(12, 'Paris', 'London', 160),(12, 'Paris', 'London', 160),
(13, 'Berlin', 'London', 210),(13, 'Berlin', 'London', 210),
(14, 'London', 'Paris', 125),(14, 'London', 'Paris', 125),
(15, 'Paris', 'Berlin', 115);(15, 'Paris', 'Berlin', 115);
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT * cheapest flightsSELECT * cheapest flights



FROM flightsFROM flights
WHERE origin 'London' AND destination 'Paris'WHERE origin 'London' AND destination 'Paris'

ORDER BY price ASCORDER BY price ASC

