USE Medical_Store;

-- Query1 [select, order by asc/desc]
SELECT pid, p_startdate, premium_amount, sum_insured
FROM health_insurance
ORDER BY pid ASC;

-- Query 2 [insert]
INSERT INTO niche_requirements (rtype, defcon, location, doctor_alloted)
VALUES ("PPE Kit", 4, "Central Hospital", 25);
SELECT * 
FROM niche_requirements
WHERE doctor_alloted = 25;
-- DELETE FROM niche_requirements WHERE doctor_alloted = 25;

-- Query 2b [Insert]
INSERT INTO department (did, dname)
VALUES (101, 'Test_Department');
SELECT * 
FROM department
WHERE did > 90;
-- DELETE FROM department WHERE did = 101;

-- Query 3 [update]
UPDATE employee
SET department = 10
WHERE eid = 50;
SELECT * FROM employee;

-- Query 4 [delete]
DELETE FROM transporter
WHERE tid = 25;
-- INSERT INTO transporter
-- VALUES (25, "Hammes, Dietrich and Keebler", "951", "8:38 PM", 19);

-- Query  [sum, if_null]
SELECT SUM(unclaimed_amount)
AS TOTAL_SUM_ALLOTED
FROM health_insurance;

-- Query 6 [case when then else]
SELECT pid,
CASE
WHEN sum_insured > 10000 THEN 'The Sum Insured is greater than 10 thousand'
WHEN sum_insured > 50000 THEN 'The Sum Insured is greater than 50 thousand'
ELSE ' The Sum Insured is under 1 lakh'
END 
AS BALANCE
FROM health_insurance;

-- Query 7 [exists]
SELECT pid, organisation_details, patient_details
FROM prescription
WHERE EXISTS (SELECT * FROM doctor WHERE doctor.did = prescription.doctor_details AND doctor.work_experience < 10);

-- Query 8 [like]
SELECT * 
FROM consumer
WHERE cname LIKE 'Smith_%';

-- Query 9 [between, and]
SELECT * 
FROM drug
WHERE quantity > 5 AND m_date BETWEEN '1995-01-01' AND '2000-01-01';

-- Query 10 [count, group by, having]
-- Aggregate
-- Lists the quantity of sellers having same amount of stock where group size > 2
SELECT count(sid), stock
FROM seller
GROUP BY stock
HAVING count(sid) > 2;

-- Query 11 [inner join all]
SELECT eid, ename, age, gender, department
FROM department AS Dep INNER JOIN employee ON department = Dep.did;

-- Query 12 [left join]
SELECT eid, ename, age, gender, department, dname
FROM department AS Dep LEFT JOIN employee ON department = Dep.did;

-- Query 13 [inner join some]
SELECT eid, ename, age, gender, department
FROM employee INNER JOIN department AS Dep ON department = Dep.did 
WHERE Dep.dname = "Accounting";

-- Query 14 [union names]
SELECT ename FROM employee
UNION
SELECT tname FROM transporter;

-- Query 15 [alter table]
-- won't work as entries with age < 18 are already in the table
ALTER TABLE employee
ADD CONSTRAINT chk_age CHECK (age > 60);
-- ALTER TABLE employee DROP CONSTRAINT chk_age;
SELECT * FROM employee;

select * from Major_Discounts;
-- Query 16 [create view]
CREATE VIEW Major_Discounts AS
SELECT *
FROM seller
WHERE Discount > 60;
SELECT * FROM Major_Discounts;