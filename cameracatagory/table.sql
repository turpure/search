#建表 camerasearch
create table camerasearch
(
id int not null primary key auto_increment,
sellerid varchar(30),
location varchar(30),
itemnumber char(12),
title varchar(85),
sales varchar(8),
price varchar(10),
shipping varchar(7),
url varchar(300),
ctime date 
)charset utf8;



#建表 camerasalesdetails
create table camerasalesdetails
(
id int not null primary key auto_increment,
itemnumber char(12),
price varchar(10),
quantity varchar(2),
shoptime date
)charset utf8;
