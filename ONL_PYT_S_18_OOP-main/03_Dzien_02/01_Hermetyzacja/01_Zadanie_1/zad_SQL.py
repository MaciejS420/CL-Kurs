zad="""
create database exercises_db;
"""

create table products(
	id serial primary key,
	name varchar(100),
	description text,
	price float
)


create table orders(
	id serial primary key,
	description text
)


create table clients(
	id serial primary key,
	name varchar(100),
	surname varchar(100)
	)