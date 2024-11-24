CREATE TABLE Caregivers
(
    Username varchar(255),
    Salt BINARY(16),
    Hash BINARY(16),
    PRIMARY KEY (Username)
);

CREATE TABLE Availabilities
(
    Time date,
    Username varchar(255) REFERENCES Caregivers,
    PRIMARY KEY (Time, Username)
);

CREATE TABLE Vaccines
(
    Name varchar(255),
    Doses int,
    PRIMARY KEY (Name)
);

CREATE TABLE Patients
(
    Username varchar (255),
    Salt BINARY (16),
    Hash BINARY (16),
    PRIMARY KEY (Username)
);

CREATE TABLE Reservations
(
    Id int,
    Time date REFERENCES Availabilities,
    Cusername varchar(255) REFERENCES Availabilities (Username),
    Pusername varchar(255) REFERENCES Patients (Unsername),
    Vname varchar(255) REFERENCES Vaccinies (name),
    PRIMARY KEY (Id)
);
