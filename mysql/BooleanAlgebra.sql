create database bool;
create table R1(a int, b int, c int, d int, F int);
create table R2(a int, b int, c int, F int);

insert into R1 values
(0,0,0,0,0),
(1,0,0,0,0),
(0,1,0,0,0),
(1,1,0,0,1),
(0,0,1,0,0),
(1,0,1,0,0),
(0,1,1,0,0),
(1,1,1,0,1),
(0,0,0,1,0),
(1,0,0,1,0),
(0,1,0,1,0),
(1,1,0,1,1),
(0,0,1,1,1),
(1,0,1,1,1),
(0,1,1,1,1),
(1,1,1,1,1);

set @count = 0;
insert into R2 values
(0, 0, 0, 0),
(1, 0, 0, 0),
(0, 1, 0, 0),
(1, 1, 0, 1),
(0, 0, 1, 0),
(1, 0, 1, 0),
(0, 1, 1, 0),
(1, 1, 1, 1);
select @count;

set @count=0;
update R2 set F = 0 where a=1 or b=1;
select @count;

select count(*) from R2 where a=1 or b=1;

select a, count(*) from R2 group by a;
select a, F, count(*) from R2 group by a, F;
select c, F, count(*) from R2 group by c, F;

create trigger Trig1 
after update on R2
for each row
  set @count = @count + 1;

drop trigger Trig1;

create table Rtest(a int, b int, c int, d int, F int, 
     InsertDate date default null, InsertTime time default null,
     ModifyDate date default null, ModifyTime time default null);
create trigger Trig2 
after update on RTest
for each row
  set @count = @count + 1;

drop trigger Trig2;

delimiter //
create trigger Trig3 
before insert on RTest
for each row
begin
  set @count = @count + 1;
  set new.InsertDate = curdate();
  set new.InsertTime = curtime();
  set new.ModifyDate = curdate();
  set new.ModifyTime = curtime();
end;//
delimiter ;

drop trigger Trig3;
drop trigger Trig4;

delimiter //
create trigger Trig4 
before update on RTest
for each row
begin
  set @count = @count + 1;
  set new.ModifyDate = curdate();
  set new.ModifyTime = curtime();
end;//
delimiter ;

drop trigger Trig4;

delimiter //
create trigger Trig4 
after update on RTest
for each row
begin
  set @count = @count + 1;
end;//
delimiter ;

delete from Rtest;
set @count=0;
LOAD DATA LOCAL INFILE 'C:/Users/Administrator/Documents/bool.2.csv' INTO TABLE Rtest 
FIELDS TERMINATED BY ',';
select @count;

select count(*) from RTest;

select * from Rtest;

drop table Rtest;

select curdate();

update Rtest set F=0 where a=0;



