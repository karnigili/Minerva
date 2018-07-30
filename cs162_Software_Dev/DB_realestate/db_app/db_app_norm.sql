.mode column
.headers on


-- CREATE TABLES

CREATE TABLE Offices (
    id INT PRIMARY KEY,
    zip_code INT, 
    PhoneNumber TEXT,

    FOREIGN KEY (zip_code) REFERENCES Locations(zip_code)

);

CREATE TABLE Agents (
    id INT PRIMARY KEY,
    FirstName TEXT,
    SurName TEXT,
    PhoneNumber TEXT,
    LicenseNumber INT,
    Mail TEXT

);

CREATE TABLE Offices_Agents (
	id INT PRIMARY KEY,
	AgentID INT,
	OfficeID INT,
	FOREIGN KEY (OfficeID) REFERENCES Offices(id),
    FOREIGN KEY (AgentID) REFERENCES Agents(id)

);



CREATE TABLE Property (
    id INT PRIMARY KEY,
    zip_code INT,
    sellerID INT, -- one to may
    BedRooms INT,
    BathRooms INT,
    ListingPrice INT,
    ListingDate DATE,
    ListingOffice_AgentID INT, -- one to many
    -- AgentID INT,
 
    StatusID INT, -- 0 is open 1 is sold

    FOREIGN KEY (sellerID) REFERENCES Sellers(id),
    FOREIGN KEY (ListingOffice_AgentID) REFERENCES Offices_Agents(id),
    FOREIGN KEY (zip_code) REFERENCES Locations(zip_code)
);




CREATE TABLE Sellers (
    id INT PRIMARY KEY,
    zip_code INT,
  	FirstName TEXT,
    SurName TEXT,
    Mail TEXT,
    PhoneNumber TEXT,

    FOREIGN KEY (zip_code) REFERENCES Locations(zip_code)
 
);

CREATE TABLE Commissions (
	id INT PRIMARY KEY,
	MinPrice INT,
	MaxPrice INT,
	Commission INT

);

CREATE TABLE Buyers (
	id INT PRIMARY KEY,
    zip_code INT,
    FirstName TEXT,
    SurName TEXT,
    Mail TEXT,
    PhoneNumber TEXT,


    FOREIGN KEY (zip_code) REFERENCES Locations(zip_code)


);

CREATE TABLE Deals (
 	id INT PRIMARY KEY,
 	PropertyID INT,
    DealOffice_AgentID INT,
 	DealDate Date,
 	DealPrice INT,
 	BuyerID INT,
 	Commission INT,


 	FOREIGN KEY (PropertyID) REFERENCES Property(id),
 	FOREIGN KEY (BuyerID) REFERENCES Buyers(id),
    FOREIGN KEY (DealOffice_AgentID) REFERENCES Offices_Agents(id)--DENORM


);

CREATE TABLE SumSales (
    ListingOffice_AgentID INT,
    SalesSum INT,
    SalesCount INT,
    CommissionSum INT,

    FOREIGN KEY (ListingOffice_AgentID) REFERENCES Offices_Agents(id)
);



CREATE TABLE Locations (
	zip_code INT PRIMARY KEY,
	Neighborhood TEXT,
	City TEXT,
	State TEXT

);

CREATE UNIQUE INDEX Offices_Agents_index ON Offices_Agents(id);
CREATE UNIQUE INDEX ListingOffice_AgentID_index ON Property(ListingOffice_AgentID);
CREATE UNIQUE INDEX Office_Agent_index ON Offices_Agents(id, AgentID, OfficeID);

 



-- INSERT MOCK UP INFO

INSERT INTO Offices VALUES (1001, 94102, '+1 415 324 0555');
INSERT INTO Offices VALUES (1002, 91007, '+1 213 435 9556');

INSERT INTO Locations VALUES (94102, 'Market ST', 'San Francisco', 'CA');
INSERT INTO Locations VALUES (91007, 'Pasadena','Los Angeles', 'CA');

INSERT INTO Agents VALUES (2001, 'Barbara', 'Brown', '+1 213 445 9556', '1231234', 'bbrown@gmail.com');
INSERT INTO Agents VALUES (2002, 'John', 'Van Der Deen', '+1 232 445 9556', '4443334', 'John@gmail.com');
INSERT INTO Agents VALUES (2003, 'Daniel', 'White', '+1 213 445 4556', '9900998', 'White@gmail.com');

INSERT INTO Offices_Agents VALUES (111, 2001, 1001);
INSERT INTO Offices_Agents VALUES (112, 2001, 1002);
INSERT INTO Offices_Agents VALUES (113, 2002, 1001);
INSERT INTO Offices_Agents VALUES (114, 2003, 1002);

INSERT INTO Property VALUES (3001, 94102, 4001, 2, 2, 1000000, '2017-11-01 10:00:00', 111, 1);
INSERT INTO Property VALUES (3002, 94102, 4002, 3, 2, 1500000, '2017-10-01 10:00:00', 113, 0);
INSERT INTO Property VALUES (3003, 91007, 4003, 4, 3, 2500000, '2017-10-01 10:00:00', 112, 0);
INSERT INTO Property VALUES (3004, 91007, 4004, 4, 3, 3000000, '2017-09-01 10:00:00', 114, 1);
INSERT INTO Property VALUES (3005, 91007, 4005, 3, 2, 1700000, '2017-11-01 10:00:00', 114, 0);
INSERT INTO Property VALUES (3006, 94102, 4001, 2, 2, 1500000, '2017-10-01 10:00:00', 111, 0);

INSERT INTO Sellers VALUES (4001, 94103, 'Maya', 'London', 'maya@gmail.com', '+1 768 984 3445');
INSERT INTO Sellers VALUES (4002, 94102, 'Don', 'Perri', 'Don@hotmail.com', '+1 768 984 3498');
INSERT INTO Sellers VALUES (4003, 91006, 'Levi', 'Sanchez', 'Levi@gmail.com', '+1 988 657 3995');
INSERT INTO Sellers VALUES (4004, 91006, 'Josh', 'Hyun', 'Josh@mail.com', '+1 768 984 3412');
INSERT INTO Sellers VALUES (4005, 91007, 'Dana', 'Man', 'Dana@gmail.com', '+1 199 998 30978');

INSERT INTO Commissions VALUES (9001, 0, 100000, 0.10);
INSERT INTO Commissions VALUES (9002, 100000, 200000, 0.075);
INSERT INTO Commissions VALUES (9003, 200000, 500000, 0.06);
INSERT INTO Commissions VALUES (9004, 500000, 1000000, 0.05);
INSERT INTO Commissions VALUES (9005, 1000000, 9e999, 0.04);

INSERT INTO Buyers VALUES (5001, 94103, 'Rena', 'Robsom', 'rrobsom@gmail.com', '+1 978 685 3445');
INSERT INTO Buyers VALUES (5002, 91003, 'Sean', 'Black', 'Sblack@gmail.com', '+1 213 443 0987');
INSERT INTO Buyers VALUES (5003, 94104, 'Alexis', 'Dor', 'doral@gmail.com', '+1 917 334 2222');

INSERT INTO Deals VALUES (701, 3001, 111, '2017-12-01 10:00:00', 900000, 5001, 90000);
INSERT INTO Deals VALUES (702, 3004, 114, '2017-10-01 10:00:00', 2700000, 5003, 162000);

INSERT INTO SumSales VALUES (111, 0, 0, 0);
INSERT INTO SumSales VALUES (112, 0, 0, 0);
INSERT INTO SumSales VALUES (113, 0, 0, 0);
INSERT INTO SumSales VALUES (114, 0, 0, 0);


-- Closing a deal
BEGIN TRANSACTION;
-- add a new buyer
INSERT INTO Buyers VALUES (5004, 91004, 'Ron', 'Ayer', 'Ayer@gmail.com', '+1 990 324 3344');

-- insert infor the deals
INSERT INTO Deals 
SELECT 703, 3006, 0,'2018-02-01 10:00:00', 950000, 5004, 950000*Commission 
FROM Commissions 
WHERE 950000 BETWEEN MinPrice AND MaxPrice;

-- make sure the agent is the same in the deals and the property tables
UPDATE Deals 
SET DealOffice_AgentID=
(SELECT ListingOffice_AgentID FROM Property WHERE id = 3006)
WHERE PropertyID=3006;

-- update the property to sold
UPDATE Property SET StatusID=1 WHERE id = 3006;


-- update summary table with sales info
UPDATE SumSales 
SET SalesCount = SalesCount+1 
AND SalesSum = SalesSum + 950000
AND CommissionSum = CommissionSum +950000*(
SELECT Commission
FROM Commissions 
WHERE 950000 BETWEEN MinPrice AND MaxPrice )
WHERE ListingOffice_AgentID = 111;

-- print relevant info
SELECT 'VALIDATE deal info';
SELECT * FROM Buyers WHERE id = 5004;
SELECT * FROM Deals WHERE id = 703;
SELECT StatusID FROM Property WHERE id=3006;
SELECT * FROM SumSales WHERE ListingOffice_AgentID=
(SELECT ListingOffice_AgentID FROM Property WHERE id = 3006);

COMMIT;


-- Listing a new property
BEGIN TRANSACTION;
INSERT INTO Sellers 
VALUES (4006, 91007, 'Micheal', 'Fry', 'mfry@gmail.com', '+1 917 332 0909');

INSERT INTO Property 
VALUES (3007, 91002, 4006, 3, 2, 1000000, '2017-10-01 10:00:00', 112, 0);

SELECT 'VALIDATE listing';
SELECT * FROM Property WHERE id=3007;
SELECT * FROM Sellers WHERE id=4006;

COMMIT;

-- Queries

-- Find the top 5 offices with the most sales for that month.
SELECT 'TOP 5 offices with the most sales';

SELECT OA.OfficeID, SUM (P.StatusID) AS Sales
FROM Offices_Agents OA 
JOIN Property P ON OA.id = P.ListingOffice_AgentID 
GROUP BY OA.OfficeID 
ORDER BY SUM(P.StatusID) DESC
LIMIT 5;

-- Find the top 5 estate agents who have sold the most 
-- (include their contact details and their sales details
SELECT 'TOP 5 offices with the most sales';


-- SELECT OA.AgentID
-- FROM Offices_Agents OA 
-- JOIN Property P ON OA.id = P.ListingOffice_AgentID 
-- GROUP BY OA.AgentID 
-- ORDER BY SUM(P.StatusID) DESC
-- LIMIT 5


-- SELECT D.PropertyID, D.DealDate, D.DealPrice, D.Commission, P.ListingPrice, P.ListingDate, P.AgentID
-- FROM Deals D
-- JOIN Property P ON D.PropertyID=P.id



