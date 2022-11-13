CREATE TABLE phrases (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date_create DATETIME,
date_update DATETAIME,
knowledge_level TEXT,  -- Уровень знания
appemtps_count INTEGER DEFAULT 0,
id_eng INTEGER,
id_ru INTEGER,
FOREIGN KEY (id_eng) REFERENCES eng (id),
FOREIGN KEY (id_ru) REFERENCES ru (id)
);

CREATE TABLE eng (
id INTEGER PRIMARY KEY AUTOINCREMENT,
value TEXT NOT NULL);

CREATE TABLE ru (
id INTEGER PRIMARY KEY AUTOINCREMENT,
value TEXT NOT NULL);