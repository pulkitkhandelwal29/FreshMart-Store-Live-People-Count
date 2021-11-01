#creating database 
create database freshmartstoredb;
use freshmartstoredb;

CREATE TABLE customer_details (
gender varchar(6),
minimum_age int,
maximum_age int
);

select * from customer_details;

CREATE TABLE people_in_outlet (
people_entry_time timestamp,
people_in int
);

select * from people_in_outlet;



CREATE TABLE people_exit_outlet (
people_exit_time timestamp,
people_exit int
);

select * from people_exit_outlet;