-- PART 1
use preshita;


drop view if exists home_team;
drop view if exists away_team;


drop table if exists Game;
drop table if exists team_has_coach;
drop table if exists team_has_players;
drop table if exists Team;
drop table if exists Player;
drop table if exists Coach;

-- create table Team
create table Team(
	tid integer not null auto_increment,
	name varchar(100) not null,
    stadium varchar(100) not null,
    city varchar(100) not null,
	primary key(tid)
) engine = innodb;

-- create table Player
create table Player(
	pid integer not null auto_increment,
	name varchar(100) not null,
	jersey integer not null, 
    position varchar(100) not null,
	primary key(pid)
)engine = innodb;

-- create table Coach
create table Coach(
	cid integer not null auto_increment, 
	name varchar(100) not null,
	contract_end date not null, 
	primary key(cid)
)engine = innodb;

-- inserting data into table Team
INSERT INTO Team (tid, name, stadium, city)
VALUES (1, 'Arizona Cardinals', 'Farm Stadium', 'Glendale'),
(2, 'Cincinnati Bengals', 'Paul Brown Stadium', 'Cincinnati'),
(3, 'Los Angeles Rams', 'SoFi Stadium', 'Inglewood'),
(4, 'Tennessee Titans', 'Nissan Stadium', 'Nashville');


-- inserting data into table Coach
INSERT INTO Coach(cid, name, contract_end)
VALUES (51, 'Kliff Kingsbury','2025-10-20'),
(52, 'Zac Taylor', '2026-01-09'),
(53, 'Sean McVay', '2027-05-12'),
(54, 'Mike Vrabel', '2030-10-31');

-- inserting data into table Player
INSERT INTO Player(pid, name, jersey, position)
VALUES (101, 'Zach Allen', 94, 'Fullback'),
(102, 'Budda Baker', 3, 'Running Back'),
(103, 'Trace McSorley', 19, 'Quarterback'),

(104, 'Brandon Allen', 8, 'Quarterback'),
(105, 'Eli Apple', 20, 'Cornerback'),
(106, 'Vonn Bell', 24, 'Wide Receiver'),

(107, 'Bryce Perkins', 16, 'Quarterback'),
(108, 'Taylor Rapp', 24, 'Center'),
(109, 'Robin Merlow', 15, 'Running Back'),

(110, 'Patrick Mahomes', 15, 'Quarterback'),
(111, 'Tom Brady', 12, 'Quarterback'),
(112, 'Ezekiel Elliott', 21, 'Running Back');

-- creating table team_has_coach
create table team_has_coach(
	tid integer not null, 
	cid integer not null,
	primary key (tid),
	foreign key (tid) references Team(tid) ON UPDATE CASCADE ON DELETE CASCADE,
	foreign key (cid) references Coach(cid) ON UPDATE CASCADE ON DELETE CASCADE
)engine=innodb;

-- inserting data into team_has_coach
INSERT INTO team_has_coach(tid, cid)
VALUES(1, 51),
(2, 52),
(3, 53),
(4, 54);

-- creating table team_has_players
create table team_has_players(
	tid integer not null,
	pid integer not null, 
	primary key(pid),
	foreign key (pid) references Player(pid) ON UPDATE CASCADE ON DELETE CASCADE,
	foreign key (tid) references Team(tid) ON UPDATE CASCADE ON DELETE CASCADE
)engine=innodb;

-- inserting data into team_has_players
INSERT INTO team_has_players(tid, pid)
VALUES(1, 101),
(1, 102),
(1, 103),
(2, 104),
(2, 105),
(2, 106),
(3, 107),
(3, 108),
(3, 109),
(4, 110),
(4, 111),
(4, 112);

-- create table Game
create table Game(
	gid integer not null,
	home integer not null, 
	away integer not null, 
	home_QB integer not null, 
	away_QB integer not null,
	week_num integer not null, 
	primary key(gid),
	foreign key (home) references Team(tid) ON UPDATE CASCADE ON DELETE CASCADE,
	foreign key (away) references Team(tid) ON UPDATE CASCADE ON DELETE CASCADE,
	foreign key (home_QB) references Player(pid) ON UPDATE CASCADE ON DELETE CASCADE,
	foreign key (away_QB) references Player(pid) ON UPDATE CASCADE ON DELETE CASCADE
	
)engine=innodb;

-- inserting data into Game
INSERT INTO Game(gid, home, away, week_num, home_QB, away_QB)
VALUES(501, 1, 2, 1, 103, 104), 
(502, 1, 3, 2, 103, 107),
(503, 1, 4, 3, 103, 110),
(505, 2, 3, 4, 104, 107);


-- PART 2

-- 2(a)
SELECT name, stadium, city
FROM Team; 


-- 2(b)
SELECT name, jersey
From Player 
WHERE position like ('quarterback');

-- 2(c)
SELECT c.name as coach_name, t.name as team_name, contract_end
From Coach c join team_has_coach using(cid) join Team t using(tid)
order by contract_end DESC;

-- 2(d)
SELECT p.name as player_name, position, t.name as team_name
From Player p join team_has_players using(pid) join Team t using(tid)
order by team_name asc, player_name asc;

-- 2(e)
CREATE VIEW home_team AS
SELECT gid, name as home_name, week_num, stadium
FROM Game join Team on Game.home = Team.tid;


CREATE VIEW away_team AS
SELECT gid, name as away_name
FROM Game join Team on Game.away = Team.tid;


SELECT home_name, away_name, week_num, stadium 
FROM home_team JOIN away_team using(gid)
order by week_num asc;



