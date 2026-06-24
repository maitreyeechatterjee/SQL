CREATE TABLE basketball_boxscore (CREATE TABLE basketball_boxscore (
    game_id INT PRIMARY KEY,    game_id INT PRIMARY KEY,
    away_team_points INT,    away_team_points INT,
    home_team_points INT    home_team_points INT
););

INSERT INTO basketball_boxscore (game_id, away_team_points, home_team_points) VALUESINSERT INTO basketball_boxscore (game_id, away_team_points, home_team_points) VALUES
(1, 100, 95),(1, 100, 95),
(2, 105, 110),(2, 105, 110),
(3, 90, 92),(3, 90, 92),
(4, 110, 105),(4, 110, 105),
(5, 95, 98);(5, 95, 98);



SELECT * FROM basketball_boxscore WHERE away_team_points > home_team_points;SELECT * FROM basketball_boxscore WHERE away_team_points > home_team_points;
-- Do not modify above this line ---- Do not modify above this line --
