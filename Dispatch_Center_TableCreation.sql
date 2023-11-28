CREATE TABLE LOGIN(username VARCHAR(10) PRIMARY KEY, password VARCHAR(100));

CREATE TABLE Incident(Incident_ID CHAR(10) NOT NULL PRIMARY KEY, Caller_ID CHAR(10) NOT NULL, Phone_Number CHAR(10) NOT NULL,
Address VARCHAR(50) NOT NULL, Description VARCHAR(100) NOT NULL);

CREATE TABLE Dispatcher(ID CHAR(10) NOT NULL PRIMARY KEY, FName VARCHAR(20) NOT NULL, FOREIGN KEY(ID) REFERENCES LOGIN(username) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Dispatch(Dispatcher_ID CHAR(10) NOT NULL, DIncident_ID CHAR(10) NOT NULL, 
Incident_Start_Date DATETIME NOT NULL, Incident_End_Date DATETIME, PRIMARY KEY(Dispatcher_ID, DIncident_ID),
FOREIGN KEY(DIncident_ID) REFERENCES Incident(Incident_ID) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY(Dispatcher_ID) REFERENCES Dispatcher(ID) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Police_Station(Officer_ID CHAR(6) NOT NULL PRIMARY KEY, Location VARCHAR(20) NOT NULL, FOREIGN KEY(Officer_ID) REFERENCES LOGIN(username) ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE Fire_Station(Station_ID CHAR(6) NOT NULL PRIMARY KEY, Address VARCHAR(30) NOT NULL, FOREIGN KEY(Station_ID) REFERENCES LOGIN(username) ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE Paramedic(Ambulance_ID CHAR(6) NOT NULL PRIMARY KEY, Hospital_Address VARCHAR(30) NOT NULL, FOREIGN KEY(Ambulance_ID) REFERENCES LOGIN(username) ON UPDATE CASCADE ON DELETE CASCADE);

CREATE TABLE Response(Response_ID CHAR(6) NOT NULL, RIncident_ID CHAR(10) NOT NULL, Response_Type VARCHAR(35) NOT NULL,
PRIMARY KEY(Response_ID, RIncident_ID), FOREIGN KEY(RIncident_ID) REFERENCES Incident(Incident_ID) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE DB_Roles(Dispatch_Member VARCHAR(25) PRIMARY KEY, Role VARCHAR(25));