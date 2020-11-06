--1. drop tables
drop table appRepair CASCADE CONSTRAINTS;
drop table appliance CASCADE CONSTRAINTS;
drop table customer CASCADE CONSTRAINTS;



--1. create tables
--the customer table
Create Table customer(
CustID number(6),
CustName VARCHAR2(50) not NULL,
CustPhone VARCHAR2(30) not NULL,
CustEmail VARCHAR2(30), 
constraint customer_pk primary key (CustID),
constraint CustEmail_chk CHECK(CustEmail like '%@%.com')
);

--appliance(serialNo, appDesc, appSaleDate, guaranteeLength)
--appliance: Stores for each appliance, the serial no which is unique, a description of the appliance, the purchase date and the length of the guarantee in years.

Create Table appliance(
serialNo number(6) , 
appDesc varchar2(50) not null, 
appSaleDate Date not null, 
guaranteeLength number(2) default 2 not null ,
constraint chk_guarantee check(guaranteeLength between 1 and 10),
constraint appliance_pk primary key (serialNo)
);

--appRepair(serialNo, repairDate, repairDesc, repairCost)
--Stores for each repair completed, the appliance serialNo,  a description of the repair and the cost of the repair. 
Create Table appRepair(
serialNo number(6) not null, 
CustID number(6),
repairDate date not null, 
repairDesc varchar2(50) not null, 
repairCost number(6,2) constraint chk_repair_cost check(repaircost between 60.50 and 160.30),
constraint appRepair_pk primary key (serialNo,repairDate,CustID),
constraint apprepair_app_fk foreign key (serialNo) references appliance (serialNo),
constraint apprepair_cust_fk foreign key (CustID) references customer (CustID)
);



--insert for customer
insert into customer(CustID,CustName,CustPhone,CustEmail)
values (1001, 'A. Green', '01 402 2849', 'agreen@mail.com');

insert into customer(CustID,CustName,CustPhone,CustEmail)
values (1002, 'J.Keogh', '02 203 7896', 'jkeogh@mail.com');

insert into customer(CustID,CustName,CustPhone,CustEmail)
values (1003,'K.Jones','03 333 8888','NULL@.com');

--2. Insert data into appliance
insert into appliance(serialNo, appDesc, appSaleDate, guaranteeLength) 
values (9001,'DVD Player','01 Jan 2018',2);

insert into appliance(serialNo, appDesc, appSaleDate, guaranteeLength) 
values (9002,'Fridge Freezer','31 May 2018',5);

insert into appliance(serialNo, appDesc, appSaleDate,guaranteeLength )
values (9003,'48 TV','12 Jun 2018',2);

--insert for apprepair
insert into appRepair(serialNo,CustID,  repairDate, repairDesc, repairCost) values (
9001,1001,'04 Mar 2018','DVD  Stuck',67.50);
insert into appRepair(serialNo,CustID,  repairDate, repairDesc, repairCost) values (
9002,1002,'04 Jun 2018','Constantly Defrosting',60.70);
insert into appRepair(serialNo,CustID,  repairDate, repairDesc, repairCost) values (
9003,1003,'16 Aug 2018','Blurred output',102.50);

commit;

--queries
--number6
SELECT UPPER(customer.CustName ) AS CUSTOMERNAME
FROM customer;

--number7
SELECT appRepair.serialNo,customer.CustName,customer.CustEmail 
FROM appRepair
INNER JOIN customer
ON appRepair.CustID = customer.CustID;

--number 8
SELECT appliance.serialNo,appliance.appDesc,appliance.appSaleDate,customer.CustName,customer.CustEmail 
FROM appliance,appRepair
INNER JOIN customer
ON appRepair.CustID = customer.CustID;

--number 9
SELECT appliance.serialNo,appliance.appDesc,customer.CustName,appRepair.repairDesc,appRepair.repairCost
FROM appliance,appRepair
INNER JOIN customer
ON appRepair.CustID = customer.CustID;
