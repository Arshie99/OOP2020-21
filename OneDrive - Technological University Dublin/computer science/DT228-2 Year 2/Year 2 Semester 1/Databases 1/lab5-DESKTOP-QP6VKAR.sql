--1. drop tables
drop table appRepair CASCADE CONSTRAINTS;
drop table appliance CASCADE CONSTRAINTS;



--1. create tables
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
repairDate date not null,
repairDesc varchar2(50) not null,
repairCost number(6,2) constraint chk_repair_cost check(repaircost between 60.50 and 160.30),
constraint appRepair_pk primary key (serialNo,repairDate),
constraint apprepair_app_fk foreign key (serialNo) references appliance (serialNo)
);

--2. Insert data into appliance
insert into appliance(serialNo, appDesc, appSaleDate, guaranteeLength) values (
9001,	'DVD Player',	'01 Jan 2018',2);
insert into appliance(serialNo, appDesc, appSaleDate, guaranteeLength) values (
9002,	'Fridge Freezer', '31 May 2018',5);
insert into appliance(serialNo, appDesc, appSaleDate) values (
9003,	'48 TV', 		'12 Jun 2018'); -- Should use default value from table definition

insert into appRepair(serialNo,  repairDate, repairDesc, repairCost) values (
9001,		'04 Mar 2018',	'DVD  Stuck',	67.50);
insert into appRepair(serialNo,  repairDate, repairDesc, repairCost) values (
9002,		'04 Jun 2018',	'Constantly Defrosting',	60.70);
insert into appRepair(serialNo,  repairDate, repairDesc, repairCost) values (
9003,		'16 Aug 2018',	'Blurred output',	102.50);
commit;
