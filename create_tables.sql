DROP TABLE IF EXISTS Users;

CREATE TABLE Users
(
    UserId CHAR(36) NOT NULL UNIQUE CHECK (typeof(UserId) = 'text'),
    Username VARCHAR(18) NOT NULL UNIQUE,
    PasswordHash TEXT NOT NULL,
    Email VARCHAR(254) NOT NULL UNIQUE,
    SignUpDate DATETIME NOT NULL DEFAULT (datetime('now','localtime')),
    EditDate DATETIME NULL,
    CONSTRAINT PK_Users_UserId PRIMARY KEY (UserId)
);

CREATE TRIGGER Users_EditDate_Update
    AFTER UPDATE ON Users
    BEGIN
        UPDATE Users
        SET EditDate = datetime('now','localtime')
        WHERE UserId = NEW.UserId;
    END;

DROP TABLE IF EXISTS WorkoutRoutines;

CREATE TABLE WorkoutRoutines
(
    RoutineId CHAR(36) NOT NULL UNIQUE CHECK (typeof(RoutineId) = 'text'),
    Title VARCHAR(75) NOT NULL,
    UserId CHAR(36) NOT NULL CHECK (typeof(UserId) = 'text'),
    PostDate DATETIME NOT NULL DEFAULT (datetime('now','localtime')),
    EditDate DATETIME DEFAULT (NULL),
    RoutineJSON TEXT NOT NULL,
    CONSTRAINT PK_WorkOutRoutines_RoutineId PRIMARY KEY (RoutineId),
    CONSTRAINT FK_WorkoutRoutines_UserId FOREIGN KEY (UserId) REFERENCES Users (UserId)
);

CREATE TRIGGER WorkoutRoutines_EditDate_Update
    AFTER UPDATE ON WorkoutRoutines
    BEGIN
        UPDATE WorkoutRoutines
        SET EditDate = datetime('now','localtime')
        WHERE UserId = NEW.UserId;
    END;

VACUUM;
