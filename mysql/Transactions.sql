delete from r1;

select * from r1;

/* rollback */
start transaction;

insert into r2 values (10, 10, 10, 10);

select * from r2;
select count(*) from r2;
rollback;
select * from r2;
select count(*) from r2;

/* commit */
start transaction;

insert into r2 values (10, 10, 10, 10);

commit;
select * from r2;

delete from r2 where a = 10;

delete from Rtest;
set @count=0;
LOAD DATA LOCAL INFILE 'C:/Users/Administrator/Documents/bool.2.csv' 
INTO TABLE Rtest 
FIELDS TERMINATED BY ',';
select @count;

delimiter //
create procedure test(expected int)
begin
  set autocommit = 0;
  start transaction;
  set @count=0;
  update Rtest set F=0 where a=0;
  if @count = expected then
    select 'success';
    commit;
  else
    select 'Error';
    rollback;
  end if;
  set autocommit = 1;
end//
delimiter ;

select count(*) from Rtest where a=0;
select count(*) from Rtest where a=0 and F=0;
call test(1);
call test(8);

drop procedure test;
