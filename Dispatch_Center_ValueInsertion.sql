-- Dispatcher 10 Characters --> 'DIS1234567'
	-- FName 1-15 Characters --> 'Doug'
-- Dispatch:
	-- Dispatcher_ID = Dispatch ID
    -- DIncident_ID = Incident Incident_ID
    -- Incident_Start_Date Datetime --> 'YYYY-MM-DD HH:MM:SS' (Can use function curdate())
    -- Incident_End_Date Datetime -->  'YYYY-MM-DD HH:MM:SS' (Can be NULL Initially)
-- Police, Paramedic, Fire Station 6 Characters --> 'PO, AM, FS1234'
	-- Location 1-20 Characters --> 'Santano Street' 
    -- Hospital Address 1-30 Characters --> '155 Argos Street'
    -- Address 1-30 Characters --> '163 Fire Lane'
-- Incident:
	-- Incident_ID 10 Characters --> 'I123456789'
    -- Caller_ID 10 Characters --> 'C123456789'
    -- Phone_Number 10 Characters --> 8001112222
    -- Address 1-50 Characters --> '123 Sesame Street'
	-- Description 1-100 Characters --> 'Fire, Robbery, Heart Attack, etc.'
-- Response:
	-- Response_ID = Police, Paramedic, Fire Station ID
	-- RIncident_ID = Incident ID
    -- Response_Type 1-35 Characters --> 'Police, Fire Station, Paramedics' (Some combination)
INSERT INTO login
VALUES('DIS2413895', SHA('123453')),
('DIS6194327', SHA('12767jj53')),
('DIS6731498', SHA('baseballfan23')),
('DIS7521986', SHA('ruby83254')),
('FS2740', SHA('Firegod123')),
('FS6985', SHA('YoLo822')),
('FS8452', SHA('B0mO22')),
('AM4325', SHA('l1Fesaver99')),
('AM6071', SHA('123pass')),
('AM7681', SHA('Saviorc0mpl3x')),
('PO0573', SHA('pOP0573')),
('PO1498', SHA('N3ighborh00d_H3ro')),
('PO6453', SHA('Cherr1o5_22')),
('PO9071', SHA('5hoWt!m3'));


INSERT INTO police_station
VALUES('PO6453', 'Pacific Street'),
('PO9071','Spring Drive'),
('PO1498','Henry Street'),
('PO0573','Ann Road');

INSERT INTO paramedic
VALUES('AM4325','700 Lexington Court'),
('AM7681','62 Court Street'),
('AM6071','8641 Iroquois Lane');

INSERT INTO fire_station
VALUES('FS8452','32 Walnut Avenue'),
('FS6985','31 Mountain Lane'),
('FS2740','7891 Prince Road');

INSERT INTO dispatcher
VALUES('DIS2413895', 'John'),
('DIS6731498', 'Francine'),
('DIS6194327', 'Sean'),
('DIS7521986', 'Bill');

INSERT INTO incident
VALUES('I580613472','C305829476','8289248550','7592 Amherst Court','Robbery'),
('I691582703','C460951372','7719922788','8477 Grand Avenue','Heart Attack'),
('I738094162','C781634029','4147571432','53 East Branch Street','House Fire'),
('I765381420','C182456397','5402336160','78 Courtland lane','Car Theft'),
('I326497180','C460951372','7719922788','8477 Grand Avenue','Heart Attack'),
('I217450938','C932781406','3134371668','9599 West Branch Road','Someone Collapsed'),
('I163094852','C460951372','7719922788','8477 Grand Avenue','Car Fire');

INSERT INTO dispatch
VALUES('DIS7521986','I580613472','2023-10-14 10:32:19',NULL);

INSERT INTO dispatch
VALUES('DIS6194327','I691582703','2023-09-01 8:45:22','2023-09-01 10:30:58'),
('DIS6731498','I738094162','2023-09-30 14:58:00','2023-09-30 17:38:44'),
('DIS2413895','I765381420','2023-08-14 18:20:33', NULL),
('DIS6194327','I326497180','2023-07-04 22:11:18','2023-07-05 08:23:06'),
('DIS2413895','I217450938','2023-06-10 23:08:59','2023-06-13 15:46:50'),
('DIS6731498','I163094852','2023-04-23 03:12:22','2023-04-23 05:20:16');


INSERT INTO response
VALUES('PO1498','I580613472','Police'),
('AM7681','I691582703','Paramedics'),
('FS6985','I738094162','Firefighter'),
('PO0573','I765381420','Police'),
('AM6071','I326497180','Paramedics'),
('AM4325','I217450938','Paramedics'),
('FS2740','I163094852','Firefighter');

-- All simply have access to the database but the dispatcher controls what goes in and updates info
INSERT INTO DB_Roles
VALUES('Dispatcher','Admin'),
('Firefighter','End-User'),
('Police', 'End-User'),
('Paramdedic', 'End-User'),
('Caller', 'End-User');

