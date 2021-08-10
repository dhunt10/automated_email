drop database if exists onspot_patient_count;
create database if not exists onspot_patient_count;

use onspot_patient_count;

drop table if exists location;
create table location (
	location_id int auto_increment not null unique primary key,
    location_name varchar(100) not null,
    appointment_count int default 0,
    date_of_event date not null
);

drop table if exists patient_count;
create table patient_count (
	count_id int auto_increment not null unique primary key,
	patient_total int default 0
);

drop table if exists provider_count;
create table provider_count (
	count_id int auto_increment not null unique primary key,
	provider_total int default 0
);

drop table if exists encounter_count;
create table encounter_count (
	count_id int auto_increment not null unique primary key,
	encounter_total int default 0
);

drop table if exists location_count;
create table location_count (
	count_id int auto_increment not null unique primary key,
	location_total int default 0
);

drop table if exists appointment_count;
create table appointment_count (
	count_id int auto_increment not null unique primary key,
	appointment_total int default 0
);

insert into location_count (location_total) values (15);
insert into patient_count (patient_total) values (110);
insert into encounter_count (encounter_total) values (123);
insert into provider_count (provider_total) values (5);
insert into appointment_count (appointment_total) values (20);