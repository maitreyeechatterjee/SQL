    id INT PRIMARY KEY,    id INT PRIMARY KEY,
    name TEXT,    name TEXT,
    country TEXT    country TEXT
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
(12, 'Los Angeles', 'USA');(12, 'Los Angeles', 'USA');
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT DISTINCT country FROM cities;SELECT DISTINCT country FROM cities;


CREATE TABLE cities (CREATE TABLE cities (