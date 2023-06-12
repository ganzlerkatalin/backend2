use sakila;
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
-- 3. Különböző vezetéknevű színész száma
select distinct last_name from actor;
-- 4. Melyik vezetéknév szerepel több mint egyszer?
select last_name, count(last_name) from user group by last_name; 
-- 5. Jelenítsd meg az összes ország ID-t, és ország nevet, amelyik Kína,Afganisztán vagy Izrael.
select * from country;
select country_id, country from country where country like "%China%" or country like "%Afghanistan%" or country like "%Israel%";
-- 6. Mennyi az átlagos hossza egy filmnek?
select sum(length)/count(film_id) from film;
-- 7. Jelenítsd meg az összes személyzet nevét és címét.
select last_name, first_name,address, address2, district,city, country, postal_code from staff, address, city, country where staff.address_id=address.address_id and address.city_id= city.city_id and city.country_id = country.country_id ;
-- 8. Jelenitsd meg az összes vevő nevét és a hozzájuk tartozó összegeket amiket fizettek (payment amount)- első 10, limit 10
select payment_id, first_name, last_name, amount from payment, customer where payment.customer_id=customer.customer_id limit 10;
-- 9. Jelenítsd meg az összes film címét és a benne szereplő színészek neveit. első 20-limit 20