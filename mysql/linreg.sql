select count(*) from songs ;

select sum(High) from songs limit 50000;
select sum(CH) from songs limit 50000;
select sum(CH2) from
 (select power(CH,2) as CH2 from songs limit 50000) x

select sum(High2) from
 (select power(High,2) as High2 from songs limit 50000) x

select sum(CH*High) as XY from songs limit 50000
 
select count(CH) from songs
drop database cs126
create database cs126a
select * from r1
