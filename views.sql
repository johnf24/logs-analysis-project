
-- Views

create view pop_articles as
select title, count(*) from articles, log
where log.path = '/article/' || articles.slug
group by title
order by count(*) desc limit 3;

create view pop_authors as
select name, count(*) as views from articles, log, authors
where authors.id = articles.author and log.path = '/article/' || articles.slug
group by name
order by views desc;

create view error_rate as
select date(time), 100.0 * sum(case when status != '200 OK' then 1 else 0 end) / count(*) as percent from log
group by date(time)
order by percent desc;