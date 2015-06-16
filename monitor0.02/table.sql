建立数据库
create database ebay_monitor;
1.# 要抓取的数据项
#id,sellerid,itemnumer,category,title,price,shipping,quantity,listing_url
#id,itemnumber,price,quantity,shoptime
#id,itemnumber,push_date,behavior

2.# 要建立的表格
listing
salesdetails
listingdetails

3.在数据库ebay_monitor下建立这三张表
use ebay_monitor;
create table listing
(
itemnumber char(12) primary key,
sellerid varchar(30),
location varchar(30),
category varchar(50),
title varchar(85),
price varchar(10),
shipping varchar(7),
sales varchar(8),
listing_url varchar(250),
cretime date,
flag int,
pushdate date,
owner varchar(10),
deltas int not null default 0,
deltap float(6,2) not null default 0.00,
deltat int not null default 0,
volume int not null default 0
)charset utf8;


create table salesdetails
(
id int not null primary key auto_increment,
itemnumber char(12),
price varchar(10),
quantity varchar(3),
shoptime date
)charset utf8;

create table listingdetails
(
id int not null primary key auto_increment,
itemnumber char(12),
push_date date
behavior varchar(150) 
)charset utf8;
