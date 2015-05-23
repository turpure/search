2015.05.25

 
 查询月销售额超过150美金的itemnumber
 1.先查询 每个itemnumber详单内的销售总量
 select *,sum(quantity) from salesdetails group by itemnumber;
 2.再查询 每个itemnumber详单内日期大于2015.04.20的item。
 select *,sum(quantity) from salesdetails group by itemnumber having shoptime>'2015-04-20';
  select *,sum(quantity) from salesdetails where shoptime >'2015-04-20' group by itemnumber; 
  3.创建视图
  create algorithm=temptable view tempdetails as select * from salesdetails where shoptime>'2015-04-20';
  4 查询月销售额 
  select *,sum(quantity)*price from salesdetails group by itemnumber having shoptime>'2015-04-20';
  5.查询月销售额大于150美金的item
  select tempdetails.* from 
  (
select *,sum(quantity)*price as volume ,sum(quantity)as total from salesdetails group by itemnumber having shoptime>'2015-04-20'
  ) as tempdetails 
  where tempdetails.volume>150;
  
  6.和listing表联合查询，查出item的详细信息
  select * from
 (
 select tempdetails.* from 
 (
select *,sum(quantity)*price as volume ,sum(quantity)as total from salesdetails where shoptime>'2015-04-20'group by itemnumber 
  ) as tempdetails 
  where tempdetails.volume>150
 ) as finalldetails
 left join listing on finalldetails.itemnumber=listing.itemnumber;
 
