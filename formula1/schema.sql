DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS races;

CREATE TABLE races (
raceId INTEGER PRIMARY KEY, 
year INTEGER, 
round INTEGER, 
circuitId INTEGER, 
[name] TEXT, 
[date] TEXT, 
[time] TEXT, 
[url] TEXT
);

CREATE TABLE results (
  resultId INTEGER PRIMARY KEY,
	raceId INTEGER,
	driverId INTEGER,
	constructorId INTEGER,
	[number] INTEGER,
	grid INTEGER,
	position INTEGER,
	positionText TEXT,
	positionOrder INTEGER,
	points INTEGER,
	laps INTEGER,
	[time] TEXT,
	milliseconds TEXT,
	fastestLap TEXT,
	rank INTEGER,
	fastestLapTime TEXT,
	fastestLapSpeed TEXT,
	statusId INTEGER,
  FOREIGN KEY (raceId) REFERENCES races (raceId)
  );


  


