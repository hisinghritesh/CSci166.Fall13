create table rx(k int, x int, y int, z int, check (x > 100), primary key (k));
insert into rx values (0, 0, 0, 0);
select * from rx;

create trigger t 

create table ry( k int, x int, foreign key (k) references rx(k) 
 on update cascade on delete cascade );

drop table ry;
insert into rx values (10,10,10,10);
insert into rx values (11,10,10,10);
insert into ry values (10, 10);
insert into ry values (11, 10);

select * from ry;

delete from rx where k=10;

select * from ry;

update rx set k=22 where k=11;
select * from ry;