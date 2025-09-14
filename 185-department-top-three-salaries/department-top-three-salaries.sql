select Department,Employee,Salary FROM (
    select d.name as Department,e.name as Employee,e.salary as Salary,
    dense_rank() over (partition by e.departmentId order by e.salary desc) as rnk
    from Employee e
    join Department d
    on e.departmentID=d.id
) nt
where rnk<4 
order by Department and Salary desc;
