

--Create the table structure
CREATE TABLE Student 
( 
idnumber VARCHAR2(9), 
firstname VARCHAR2(20), 
lastname VARCHAR2(20), 
dateofbirth DATE, 
address VARCHAR2(200), 
email VARCHAR2(50), 
programme VARCHAR2(5), 
points number(3), 
PRIMARY KEY (idnumber) 
);

--Insert the data
INSERT INTO Student VALUES ( 
'D1234567', 
'Student ONE', 
'TWO THREE', 
'10 May 2000', 
'100 The Road, The Town, The County, The Country', 
'd1234567@mydit.ie', 
'DT228', 
380 
);

INSERT INTO Student VALUES ( 
'D2345678', 
'Student TWO', 
'FOUR FIVE', 
'10 Apr 2000', 
'100 The Avenue, The Town, The County, The Country', 
'd2345678@mydit.ie', 
'DT228', 
280 
);
commit;

--Query to find all students with  300 points or more
SELECT firstname, lastname 
FROM student 
WHERE points >= 300;


--Write an SQL Query to find all students with less than 300 points
