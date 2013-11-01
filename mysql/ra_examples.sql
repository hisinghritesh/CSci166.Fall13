create table R1(K int, B int, C int, primary key (K));
create table R2(K int, F int, primary key (K));
create table R3(K int, D int, E int, primary key (K));

insert into R1 values (2, 1, 7);
insert into R1 values (3, 2, 0);
insert into R1 values (5, 1, 7);
insert into R1 values (7, 2, 2);
insert into R1 values (9, 1, 8);

insert into R2 values (2, 6);
insert into R2 values (3, 0);
insert into R2 values (5, 2);
insert into R2 values (7, 1);
insert into R2 values (9, 4);

insert into R3 values (2, 4, 5);
insert into R3 values (3, 5, 1);
insert into R3 values (5, 8, 0);
insert into R3 values (7, 3, 2);
insert into R3 values (9, 5, 4);

insert into R3(K) values(12);
select * from R3;

delete from R2;
insert into R2 values (0, 44);
insert into R2 values (1, 49);
insert into R2 values (2, 56);
insert into R2 values (3, 62);
insert into R2 values (4, 66);

drop table RX
create table RX ( a int, b int, c int)
insert into RX (a, b) 
   (select k, f from r1 natural join r2)

select * from RX
select k, f from r1 natural join r2
