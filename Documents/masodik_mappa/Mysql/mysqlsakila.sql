dir
-- 1.feladat Összes színész vezetékneve és keresztneve
select first_name, last_name from actor;
-- 2.a Összes színész teljes neve csupa nagybetűvel egyetlen oszlopban , oszlopneve "Actor Name"
select concat(upper(first_name)," ",upper(last_name)) AS "Actor Name" from actor;
-- 2.b Azonosító, vezetéknév, keresztnév annak a színésznek akinek keresztneve Joe
select * from actor where first_name like "Joe";
-- 2.c Minden színész akinek vezetékneve tartalmazza a 'gen' szót.
select * from actor where last_name like '%gen%'; 
-- 2.d Minden szinész akinek vezetékneve tartalmazza a 'li' szót, vezetéknév és keresztnév szerint rendezve.
select * from actor where last_name like '%li%' order by last_name, first_name;
