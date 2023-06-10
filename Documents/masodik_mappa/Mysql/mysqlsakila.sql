use sakila;
-- 1.feladat Összes színész vezetékneve és keresztneve
select first_name, last_name from actor;
--2.a Összes színész teljes neve csupa nagybetűvel egyetlen oszlopban , oszlopneve "Actor Name"
select concat(upper(first_name)," ",upper(last_name)) AS "Actor Name" from actor;
--2b Azonosító, vezetéknév, keresztnév annak a színésznek akinek keresztneve Joe
select * from actor where last_name like "Joe";