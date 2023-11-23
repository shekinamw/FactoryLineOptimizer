
-- Employee Table
CREATE TABLE Employee (
  EmployeeID INT PRIMARY KEY,
  GivenName VARCHAR(255),
  FamilyName VARCHAR(255),
  Age INT,
  Email VARCHAR(255),
  Phone VARCHAR(255),
  JobTitle VARCHAR(255),
  Apartment VARCHAR(255),
  Street VARCHAR(255),
  City VARCHAR(255),
  ProvinceState VARCHAR(2),
  Country VARCHAR(255)
);

-- Employee_Weekly_Availability Table
CREATE TABLE Availability (
  EmployeeID INT,
  Monday BOOLEAN,
  Tuesday BOOLEAN,
  Wednesday BOOLEAN,
  Thursday BOOLEAN,
  Friday BOOLEAN,
  Saturday BOOLEAN,
  Sunday BOOLEAN,
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Workstation Table
CREATE TABLE Workstation (
  WorkstationID INT PRIMARY KEY,
  WorkstationName VARCHAR(255)
);

-- WSTask Table
CREATE TABLE WSTask (
  TaskID INT PRIMARY KEY,
  WorkstationID INT,
  TaskName VARCHAR(255),
  FOREIGN KEY (WorkstationID) REFERENCES Workstation(WorkstationID)
);

-- Schedule Table
CREATE TABLE Schedule (
  WorkstationID INT,
  EmployeeID INT,
  StartTime DATETIME,
  EndTime DATETIME,
  FOREIGN KEY (WorkstationID) REFERENCES Workstation(WorkstationID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- SensorData Table
CREATE TABLE SensorData (
  SensorID INT PRIMARY KEY,
  TaskID INT,
  StartDateTime DATETIME,
  StopDateTime DATETIME,
  FOREIGN KEY (TaskID) REFERENCES WSTask(TaskID)
);

-- Performance Table
CREATE TABLE Performance (
  WorkstationID INT,
  EmployeeID INT,
  EmployeePerformanceScore FLOAT,
  FOREIGN KEY (WorkstationID) REFERENCES Workstation(WorkstationID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
