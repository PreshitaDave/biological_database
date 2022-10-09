select count(distinct(mid)) as unique_count
from targets
where score < -0.6;  