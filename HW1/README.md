Description: You will be creating and populating tables in your MySQL database for a football league regular season schedule during the 2022 season. Drawing an ER diagram and table schemas is recommended, but not required! Entities and relationships are designated in bold below. Do not turn in an ER diagram.


• Each football team has a name, a stadium, and a city.

• Each player has a name, a jersey number, and a position.

• Each coach has a name and a current contract end date.

• Each team has one coach. Each coach works for one team.

• Each player plays for one team. Each team has several players that play for it.

• A game is played by two teams (designated home and away) and has a date (specified as a week number in the season). [Note: game is not an entity.]

• No team can play more than one game in a given week.

• Each game will have two starting quarterbacks, the home QB and the away QB, one player from each team.


Part I: Problems


1. Write CREATE TABLE statements that capture the stated information. Your table structure should include necessary constraints.

2. Write INSERT statements to populate your tables with at least: a. 4 teams (which will have corresponding stadiums and cities) b. 8 players (at least four of which are quarterbacks)
c. 1 coach for each team d. 3 games.

Note that you must use INSERT statements, not LOAD DATA LOCAL INFILE.

Note: You can make up your own names, use a different sport, or go to www.nfl.com for some suggestions.


Part 2: Problems
3. Write SELECT statements to:

a) List all teams (team_name, stadium, city).

b) List all quarterbacks (name, number).

c) List each coach (name, team, contract_end) in descending order by contract end date.

d) List all players (name, position, team_name) in alphabetical order by team name and then player name.

e) List each game (home team name, away team name, stadium, week) in order by week ascending.
