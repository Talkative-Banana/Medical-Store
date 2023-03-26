-- [Trigger 1]
-- The Trigger Insures on every new addition of an entry to the database every consumer who has a prescription has atleast 10000 as sum insured (Minimum Plan)
DROP TRIGGER IF EXISTS `medical_store`.`minimum_sum_insured`;
DELIMITER $$
USE `medical_store`$$
CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`minimum_sum_insured` BEFORE INSERT ON `health_insurance` FOR EACH ROW
BEGIN
	IF NEW.sum_insured < 10000 THEN SET NEW.sum_insured = 10000;
END IF;  
END$$
DELIMITER ;

SELECT * from health_insurance;


-- [Trigger 2]
-- making sure that every insurance health insurance is atleat a year long 
DROP TRIGGER IF EXISTS `medical_store`.`minimum_span`;
DELIMITER $$
USE `medical_store`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `minimum_span` BEFORE INSERT ON `health_insurance` FOR EACH ROW BEGIN
	IF NEW.p_duration < 1 THEN SET NEW.p_duration = 1 AND NEW.p_enddate = NEW.p_startdate + 1;
END IF; 
END$$
DELIMITER ;

SELECT * from health_insurance;

-- [Trigger 3]
-- making sure that every employee has password of length >= 8 
DROP TRIGGER IF EXISTS `medical_store`.`employee_password_length`;
DELIMITER $$
USE `medical_store`$$
CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`employee_password_length` BEFORE INSERT ON `employee_credentials` FOR EACH ROW
BEGIN
	IF LENGTH(NEW.employee_login_password) < 8 THEN signal sqlstate '45000' set message_text = 'Invalid Password length (<8)';
end if;
END$$
DELIMITER ;

SELECT * FROM employee_credentials;

-- [Trigger 4]
-- making sure that every consumer has password of length >= 8
DROP TRIGGER IF EXISTS `medical_store`.`consumer_password_length`;
DELIMITER $$
USE `medical_store`$$
CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`consumer_password_length` BEFORE INSERT ON `consumer_credentials` FOR EACH ROW
BEGIN
	IF LENGTH(NEW.consumer_login_password) < 8 THEN signal sqlstate '45000' set message_text = 'Invalid Password length (<8)';
end if;
END$$
DELIMITER ;

SELECT * FROM consumer_credentials;

SHOW TRIGGERS;

-- [OLAP Query 1]
-- ROLLUP
SELECT sex, age, count(cid)
FROM consumer
group by sex, age with rollup;

-- [OLAP Query 2]
-- ROLLUP
SELECT rtype, defcon, count(doctor_alloted) as "Count"
FROM niche_requirements
group by rtype, defcon with rollup;

-- [OLAP Query 3]
-- ROLLLUP
SELECT sex, specialization, qualifications, count(did) as "Count"
FROM doctor
group by sex, specialization, qualifications with rollup;

-- [OLAP Query 4]
-- GROUPING SETS EQUIVALENT
SELECT NULL, NULL, qualifications, count(did) as "Count"
FROM doctor
group by qualifications
union all
SELECT NULL, specialization, NULL, count(did) as "Count"
FROM doctor
group by specialization
union all
SELECT sex, NULL, NULL, count(did) as "Count"
FROM doctor
group by sex;

-- [OLAP QUERY 5]
-- CUBE
SELECT rtype, defcon, count(doctor_alloted) as "Count"
FROM niche_requirements
group by rtype, defcon with rollup
union all
SELECT rtype,NULL, count(doctor_alloted) as "Count"
FROM niche_requirements
group by rtype
union all
SELECT NULL, defcon, count(doctor_alloted) as "Count"
FROM niche_requirements
group by defcon
union all
SELECT NULL, NULL, count(doctor_alloted) as "Count"
FROM niche_requirements
group by NULL;

-- [OLAP Query 6]
-- CUBE
SELECT sex, age, count(cid)
FROM consumer
group by sex, age with rollup
union all
SELECT NULL, age, count(cid)
FROM consumer
group by age
union all
SELECT sex, NULL, count(cid)
FROM consumer
group by sex
union all
SELECT NULL, NULL, count(cid)
FROM consumer
group by NULL;