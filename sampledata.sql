INSERT INTO Employee (EmployeeID, GivenName, FamilyName, Age, Email, Phone, JobTitle, Apartment, Street, City, ProvinceState, Country) VALUES
(1, 'John', 'Doe', 30, 'john.doe@email.com', '+1-123-456-7890', 'Operator', 'Apt 101', '123 Elm St', 'Oshawa', 'ON', 'Canada'),
(2, 'Jane', 'Smith', 25, 'jane.smith@email.com', '+1-234-567-8901', 'Operator', 'Apt 202', '456 Maple St', 'Oshawa', 'ON', 'Canada'),
(3, 'Robert', 'Johnson', 35, 'robert.johnson@email.com', '+1-345-678-9012', 'Operator', 'Apt 303', '789 Oak St', 'Oshawa', 'ON', 'Canada'),
(4, 'Emily', 'Brown', 28, 'emily.brown@email.com', '+1-456-789-0123', 'Operator', 'Apt 404', '567 Cedar St', 'Oshawa', 'ON', 'Canada'),
(5, 'Michael', 'Lee', 32, 'michael.lee@email.com', '+1-567-890-1234', 'Operator', 'Apt 505', '345 Birch St', 'Oshawa', 'ON', 'Canada'),
(6, 'Sophia', 'Anderson', 29, 'sophia.anderson@email.com', '+1-678-901-2345', 'Operator', 'Apt 606', '678 Pine St', 'Oshawa', 'ON', 'Canada'),
(7, 'William', 'Martinez', 27, 'william.martinez@email.com', '+1-789-012-3456', 'Operator', 'Apt 707', '890 Walnut St', 'Oshawa', 'ON', 'Canada'),
(8, 'Olivia', 'Harris', 31, 'olivia.harris@email.com', '+1-890-123-4567', 'Operator', 'Apt 808', '432 Elm St', 'Oshawa', 'ON', 'Canada'),
(9, 'James', 'Garcia', 33, 'james.garcia@email.com', '+1-901-234-5678', 'Operator', 'Apt 909', '321 Oak St', 'Oshawa', 'ON', 'Canada'),
(10, 'Ava', 'Taylor', 26, 'ava.taylor@email.com', '+1-012-345-6789', 'Operator', 'Apt 1010', '123 Cedar St', 'Oshawa', 'ON', 'Canada'),
(11, 'Liam', 'Smith', 24, 'liam.smith@email.com', '+1-123-456-7890', 'Operator', 'Apt 1111', '456 Maple St', 'Oshawa', 'ON', 'Canada'),
(12, 'Mia', 'Wilson', 30, 'mia.wilson@email.com', '+1-234-567-8901', 'Operator', 'Apt 1212', '789 Oak St', 'Oshawa', 'ON', 'Canada'),
(13, 'Ethan', 'Johnson', 34, 'ethan.johnson@email.com', '+1-345-678-9012', 'Operator', 'Apt 1313', '567 Cedar St', 'Oshawa', 'ON', 'Canada'),
(14, 'Isabella', 'Garcia', 27, 'isabella.garcia@email.com', '+1-456-789-0123', 'Operator', 'Apt 1414', '345 Birch St', 'Oshawa', 'ON', 'Canada'),
(15, 'Noah', 'Brown', 29, 'noah.brown@email.com', '+1-567-890-1234', 'Operator', 'Apt 1515', '678 Pine St', 'Oshawa', 'ON', 'Canada');

INSERT INTO Availability (EmployeeID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES
(1, 1, 1, 0, 0, 1, 0, 0),
(2, 1, 1, 1, 0, 1, 0, 0),
(3, 1, 0, 0, 1, 0, 0, 1),
(4, 0, 1, 0, 0, 1, 0, 0),
(5, 1, 1, 1, 1, 1, 0, 0),
(6, 1, 0, 0, 1, 0, 0, 1),
(7, 1, 1, 0, 1, 0, 0, 0),
(8, 1, 0, 1, 0, 1, 0, 0),
(9, 1, 0, 0, 1, 1, 0, 1),
(10, 1, 1, 1, 0, 1, 0, 0),
(11, 0, 1, 1, 0, 0, 0, 0),
(12, 1, 0, 0, 1, 0, 0, 0),
(13, 0, 1, 1, 1, 0, 0, 0),
(14, 1, 0, 0, 1, 0, 1, 0),
(15, 1, 0, 0, 1, 1, 0, 0);

-- Insert data into the Workstation table
INSERT INTO Workstation (WorkstationID, WorkstationName)
VALUES
(101, 'Doors OFF'),
(102, 'Manifest'),
(103, 'Airbags'),
(104, 'VIN'),
(105, 'Spoiler'),
(106, 'Harness'),
(107, 'WeatherStrip'),
(108, 'Hoodclamp'),
(109, 'SeatBelts'),
(110, 'ABS');

INSERT INTO WSTask (TaskID, WorkstationID, TaskName)
VALUES
(1, 101, 'Usecure connecting bolts'),
(2, 101, 'Use hoist'),
(3, 101, 'Seperate Door from chassis'),
(4, 102, 'Place Manifest on Chassis'),
(5, 102, 'Scan Manifest'),
(6, 103, 'Place Airbags in Chassis'),
(7, 103, 'Scan Airbags'),
(8, 103, 'Secure Airbags in Chassis'),
(9, 104, 'Place VIN sticker mold'),
(10, 104, 'Place VIN'),
(11, 104, 'Scan VIN'),
(12, 105, 'Place spoiler on chasssis'),
(13, 105, 'Connect lights cable to Chassis'),
(14, 105, 'Secure Spoiler to Chassis'),
(15, 106, 'Scan Harness'),
(16, 106, 'Place and Secure harness into Chassis'),
(17, 107, 'Place Weather Strip around Door Ridges'),
(18, 107, 'Crimp the Weather strip'),
(19, 108, 'Secure Hood Clamps'),
(20, 109, 'Scan Seatbelts'),
(21, 109, 'Place and Secure Seatbelts'),
(22, 110, 'Scan ABS Module'),
(23, 110, 'Place ABS onto Chassis'),
(24, 110, 'Secure ABS'),
(25, 110, 'Secure Breaklines');

INSERT INTO Schedule (WorkstationID, EmployeeID, StartTime, EndTime)
VALUES
(101, 5, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(102, 7, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(103, 6, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(104, 9, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(105, 10, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(106, 11, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(107, 1, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(108, 3, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(109, 13, '2023-11-05 06:30:00', '2023-11-05 14:30:00'),
(110, 15, '2023-11-05 06:30:00', '2023-11-05 14:30:00');


INSERT INTO SensorData (SensorID, TaskID, StartDateTime, StopDateTime)
VALUES
  (1, 13, '2023-11-05 07:30:02', '2023-11-05 07:31:13'),
  (2, 13, '2023-11-05 07:30:02', '2023-11-05 07:31:13'),
  (3, 1, '2023-11-05 06:30:00', '2023-11-05 06:32:00'),
  (4, 20, '2023-11-05 06:35:25', '2023-11-05 06:37:24'),
  (5, 13, '2023-11-05 06:42:10', '2023-11-05 06:44:09'),
  (6, 9, '2023-11-05 07:00:50', '2023-11-05 07:02:49'),
  (7, 20, '2023-11-05 07:07:15', '2023-11-05 07:09:14'),
  (8, 6, '2023-11-05 07:22:30', '2023-11-05 07:24:29'),
  (9, 6, '2023-11-05 07:31:40', '2023-11-05 07:33:39'),
  (10, 6, '2023-11-05 07:44:55', '2023-11-05 07:46:54'),
  (11, 5, '2023-11-05 08:01:20', '2023-11-05 08:03:19'),
  (12, 6, '2023-11-05 08:10:45', '2023-11-05 08:12:44'),
  (13, 3, '2023-11-05 08:22:00', '2023-11-05 08:24:00'),
  (14, 1, '2023-11-05 08:37:25', '2023-11-05 08:39:24'),
  (15, 24, '2023-11-05 09:00:30', '2023-11-05 09:02:30'),
  (16, 9, '2023-11-05 09:12:55', '2023-11-05 09:14:54'),
  (17, 8, '2023-11-05 09:20:10', '2023-11-05 09:22:10'),
  (18, 7, '2023-11-05 09:45:35', '2023-11-05 09:47:35'),
  (19, 7, '2023-11-05 10:00:50', '2023-11-05 10:02:50'),
  (20, 7, '2023-11-05 10:12:15', '2023-11-05 10:14:15'),
  (21, 5, '2023-11-05 10:30:40', '2023-11-05 10:32:40'),
  (22, 4, '2023-11-05 10:45:05', '2023-11-05 10:47:05');

INSERT INTO Performance (WorkstationID, EmployeeID, EmployeePerformanceScore)
VALUES
(101, 1, 0.85),
(102, 2, 0.92),
(103, 3, 0.78),
(104, 4, 0.65),
(105, 5, 0.89),
(106, 6, 0.72),
(107, 7, 0.95),
(108, 8, 0.81),
(109, 9, 0.88),
(110, 10, 0.75),
(101, 11, 0.79),
(102, 12, 0.93),
(103, 13, 0.86),
(104, 14, 0.77),
(105, 15, 0.91);