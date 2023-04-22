
create database dbtest3;
use dbtest3;
create table doctor_details(d_id int(5),d_name varchar(25) primary key,d_age int(3),d_department varchar(40),d_phono varchar(15));
alter table doctor_details modify d_id varchar(5);
create table worker_details(w_id varchar (5),w_name varchar(25) primary key,w_age int(3),w_workname varchar(40),w_phono varchar(15));


create table patient_details(p_id varchar (5),p_name varchar(25) primary key,p_age int(3),p_problems varchar(40),p_phono varchar(15));
insert into doctor_details values(101,'Dr Avinash Jha',35,'Allergy and Immunology',9136108876),(103,'Dr Santosh Kumar',26,'Anesthesiology',8970456723),(140,'Dr Arvind Arora',52,'Dermatology',7681539873),(130,'Dr Kassehra',40,'Neurology',9830164257),(110,'Dr Manoj Jha',45,'Pediatrics',9863210897),(120,'Dr Nimish Dutta',38,'Surgery',8765098901),(121,'Dr Vivek Raj',54,'Covid',9874324315);
insert into worker_details values(03,'Suresh',28,'Security Guard',9871234980),(10,'Ramesh',35,'Canteen Manager',7896543278),(11,'Mukesh',25,'Maintenance',9808907641),(15,'Lokesh',40,'Nurse',8907896785);
insert into patient_details values(310,'Aditya',17,'OCD',9834545671),(410,'Mitadru',30,'Dengue',9830145675),(150,'Pranav',56,'Covid',9887654321),(560,'Yash',40,'Bone Fracture',8909876785),(389,'Mrinal',22,'Appendix',98451098761),(432,'Aryan',68,'Heart Surgery',9870981325);

select d_id as Doctor_ID,d_name as Doctor_Name,d_age as Doctor_Age ,d_department as Doctor_Department,d_phono as Doctor_Phono from doctor_details;
select p_id as Patient_ID,p_name as Patient_Name,p_age as Patient_Age ,p_problems as Patient_Diagnosis,p_phono as Patient_Phono from patient_details;

select * from doctor_details;
drop table worker_details;
select now();
create table worker_details(w_id varchar(5) primary key,w_name varchar(25) ,w_age int(3),w_workname varchar(40),w_phono varchar(15));
