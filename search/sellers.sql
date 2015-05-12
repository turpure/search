create table sexsellers
(
id int unsigned not null primary key auto_increment,
sellersid varchar(50) not null default 'no name',
itemnumber char(15) not null default 'no number',
title varchar(83) not null default 'no title',
sales varchar(20) not null default 'zero sold',
url varchar(250) not null default 'no url',
ctime datetime
)charset utf8;



create table search
(
id int unsigned not null primary key auto_increment,
sellersid varchar(50) not null default 'no name',
location varchar(35) not null default 'unkown',
itemnumber char(15) not null default 'no number',
title varchar(83) not null default 'no title',
sales varchar(20) not null default 'zero sold',
price varchar(10) not null default '0',
shipping varchar(10) not null default '0',
url varchar(250) not null default 'no url',
ctime datetime
)charset utf8;



select *,count(id) from search group by sellersid;

create view aim select * from count where sales like "%China";

