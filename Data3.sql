Create database Department1;
use Department1;
create table Product2(
pid int,
proname varchar(12),
original_price int,
selling_Date date,
stock int
);

insert into Product2 values(101,"oil",1500,"2024-2-02",4000);
insert into Product2 values(102,"Iron",2000,"2024-12-03",6000);
insert into Product2 values(103,"scrab",1500,"2024-7-05",4600);
insert into Product2 values(104,"Steal",1000,"2024-8-12",5000);

select * from product2
where original_price between 2000 and 15000;

select * from product2
where proname between 'a' and 'j';

select * from product2
where selling_Date between "2024-8-12" and "2024-12-03";

