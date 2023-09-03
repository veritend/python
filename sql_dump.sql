BEGIN TRANSACTION;CREATE TABLE cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        );INSERT INTO "cars" VALUES(2,'Chevrolet',51500);INSERT INTO "cars" VALUES(3,'Renault',22300);INSERT INTO "cars" VALUES(4,'Renault',22100);DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('cars',4);COMMIT;