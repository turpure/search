#抓速卖通的数据

1.建立数据库 ali1
create database ali1;
2.建立数据表

create table listing
(

id int not null primary key auto_increment,
title varchar(250),
orders varchar(7),
seller varchar(40),
address varchar(40),
price varchar(10),
url varchar(300)
)charset utf8;

