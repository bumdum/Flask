DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS races;

CREATE TABLE races (
raceId INTEGER PRIMARY KEY, 
year INTEGER NOT NULL, 
round INTEGER NOT NULL, 
circuitId INTEGER NOT NULL, 
[name] TEXT, 
[date] TEXT, 
[time] TEXT, 
[url] TEXT
);

CREATE TABLE results (
  resultId INTEGER PRIMARY KEY,
	raceId INTEGER NOT NULL,
	driverId INTEGER NOT NULL,
	constructorId INTEGER NOT NULL,
	[number] INTEGER NOT NULL,
	grid INTEGER NOT NULL,
	position INTEGER NOT NULL,
	positionText TEXT NOT NULL,
	positionOrder INTEGER NOT NULL,
	points INTEGER NOT NULL,
	laps INTEGER NOT NULL,
	[time] TEXT,
	milliseconds TEXT,
	fastestLap TEXT,
	rank INTEGER,
	fastestLapTime TEXT,
	fastestLapSpeed TEXT,
	statusId INTEGER,
  FOREIGN KEY (raceId) REFERENCES races (raceId)
  );


  


