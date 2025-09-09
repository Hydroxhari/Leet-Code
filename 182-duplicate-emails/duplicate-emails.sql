select email from (select email,count(*) as cnt from Person group by email) nt
where cnt>1