use Department1;
create table Food1(
Item_id int primary key,
Item_Name varchar(50),
Item_Unit varchar(50),
Company_id int);

insert into Food1 values(1,"Chex Mix","Pcs",16);
insert into Food1 values(6,"Cheez-It","Pcs",15);
insert into Food1 values(2,"BN Biscuit","Pcs",15);
insert into Food1 values(3,"Mighty Munch","Pcs",17);
insert into Food1 values(4,"Pot Rice","Pcs",15);
insert into Food1 values(5,"Jaffa Cakes","Pcs",18);
insert into Food1 values(7,"Salt n Shake","Pcs",null);

select * from food1;

