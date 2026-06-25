););

INSERT INTO cities (id, name, country) VALUESINSERT INTO cities (id, name, country) VALUES
(1, 'Tokyo', 'Japan'),(1, 'Tokyo', 'Japan'),
(2, 'London', 'England'),(2, 'London', 'England'),
(3, 'Paris', 'France'),(3, 'Paris', 'France'),
(4, 'New York', 'USA'),(4, 'New York', 'USA'),
(5, 'New Delhi', 'India'),(5, 'New Delhi', 'India'),
(6, 'Shanghai', 'China'),(6, 'Shanghai', 'China'),
(7, 'Sao Paulo', 'Brazil'),(7, 'Sao Paulo', 'Brazil'),
(8, 'Mexico City', 'Mexico'),(8, 'Mexico City', 'Mexico'),
(9, 'Cairo', 'Egypt'),(9, 'Cairo', 'Egypt'),
(10, 'Mumbai', 'India'),(10, 'Mumbai', 'India'),
(11, 'Beijing', 'China'),(11, 'Beijing', 'China'),
(12, 'Los Angeles', 'USA'),(12, 'Los Angeles', 'USA'),
(13, 'Toronto', 'Canada'),(13, 'Toronto', 'Canada'),
(14, 'Vancouver', 'Canada');(14, 'Vancouver', 'Canada');
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT name FROM cities WHERE name IN ('USA', 'Canada', 'Mexico');SELECT name FROM cities WHERE name IN ('USA', 'Canada', 'Mexico');



