drop database if exists Medical_Store;
create database  Medical_Store;
use Medical_Store;

create table department(did int primary key,
						dname varchar(45) not null default "dname");

create table employee (eid int primary key,
					   ename varchar(100),
                       pannumber varchar(45),
                       aadhaarnumber varchar(45),
					   age int,
                       dob date,
                       department int,
					   email varchar(100),
					   gender varchar(20),
					   phone varchar(20),
					   address varchar(100),
                       foreign key(department) references department(did) on delete cascade on update cascade
                       );

create table seller(sid int primary key,
					stock int,
                    category varchar(100),
                    location varchar(100),
					open_hours varchar(45),
					Discount varchar(100));

create table drug(did int primary key,
				  dname varchar(45),
                  salts varchar(100),
                  m_date date,
                  producer int,
                  price double,
                  quantity int,
                  category varchar(100),
                  foreign key(producer) references seller(sid) on delete cascade on update cascade
                  );

create table transporter(tid int primary key,
						 tname varchar(100),
                         category varchar(100),
                         open_hours varchar(45),
                         discount varchar(100)
                         );
                         
create table consumer(cid int primary key,
					  pannumber varchar(45),
                      cname varchar(100),
					  sex varchar(20),
                      age int,
                      emailId varchar(100),
                      phone varchar(10)
					);
                    
create table health_insurance(pid int,
							  p_startdate date,
                              p_duration int,
							  p_enddate date,
							  premium_amount double,
                              sum_insured double,
                              unclaimed_amount double,
                              foreign key(pid) references consumer(cid) on delete cascade on update cascade
							  );

create table employee_credentials(employee_login_id int,
								  employee_login_password varchar(100),
                                  foreign key(employee_login_id) references employee(eid) on delete cascade on update cascade
								  );

create table consumer_credentials(consumer_login_id int,
								  consumer_login_password varchar(100),
                                  foreign key(consumer_login_id) references consumer(cid) on delete cascade on update cascade
                                  );

create table doctor(did int primary key,
					age int,
                    sex varchar(45),
                    phonenumber varchar(20),
                    specialization varchar(100),
                    work_experience varchar(100),
                    qualifications varchar(100),
                    current_place_of_work varchar(100),
                    department varchar(100)
                    );
                    
create table niche_requirements(rtype varchar(45),
								defcon int,
								location varchar(100),
                                doctor_alloted int,
                                foreign key(doctor_alloted) references doctor(did) on delete cascade on update cascade);

create table prescription(pid int primary key,
						  organisation_details varchar(200),
                          doctor_details int,
						  Medicinal_details varchar(300),
                          patient_details int,
                          pdate date,
                          foreign key(doctor_details) references doctor(did) on delete cascade on update cascade,
                          foreign key(patient_details) references consumer(cid) on delete cascade on update cascade
                          );