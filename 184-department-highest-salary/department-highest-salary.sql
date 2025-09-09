with ntal as (select b.id,b.name,max(a.salary) as mx
from Employee a join Department b on a.departmentID=b.id 
group by b.id)
select b.name as Department,a.name as Employee,a.salary as Salary
from Employee a join ntal b
on a.departmentid=b.id
where a.salary=b.mx;