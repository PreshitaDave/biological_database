Select mid, name as miRNA_name, count(gid) as count
from miRNA join targets using (mid)
group by mid
order by count desc
limit 10;