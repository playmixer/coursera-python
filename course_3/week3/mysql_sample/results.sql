use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select * from store

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct(store_id) from sale


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store_id from store where store_id not in (select store_id from sale)

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select p.name, avg(total / quantity)  from sale s join product p on p.product_id = s.product_id group by p.name

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select p.name from product p where (select count(distinct store_id) from sale s where product_id = p.product_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select s.name from store s where (select count(distinct store_id) from sale where product_id = s.store_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale s where total = (select max(total) from sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale s group by date order by count(*) desc, date limit 1
