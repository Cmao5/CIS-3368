/* Calvin Mao */
show databases;

create database cis3368falldb;

use cis3368falldb;
/* Reference from Techonthenet.com SQL tutorial */
/* Reference from TA class demonstration on SQL in week 3 */
/* creating a new table to show retail data */
create table if not exists Retail (
id int primary key auto_increment,
seller varchar(255) not null,
product varchar(255) not null,
quantity INT NOT NULL,
price DECIMAL(10,2) not null
)


select * from Retail;
/* inset my data to fill table for Retail */
insert into Retail (seller, product,quantity,price) values
("Gregory","Toothbrush","50","4.29");

insert into Retail (seller, product,quantity,price) values
("Laslow","GTA 5","10","60.00");

insert into Retail (seller, product,quantity,price) values
("Arthur","Xbox Series X","20","499.00");

insert into Retail (seller, product,quantity,price) values
("Gregory","ToothPaste","50","5.29");

insert into Retail (seller, product,quantity,price) values
("Laslow","Red Dead Redemption 2","20","60.00");

insert into Retail (seller, product,quantity,price) values
("Arthur","Playstation 5","40","500.00");

insert into Retail (seller, product,quantity,price) values
("Gregory","Floss","50","1.99");

insert into Retail (seller, product,quantity,price) values
("Laslow","LA Norie","10","40.00");

insert into Retail (seller, product,quantity,price) values
("Arthur","Nintendo Switch","30","299.00");


