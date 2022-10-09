select distinct gid, gene.name
from gene join targets using(gid) join miRNA using(mid)
where miRNA.name regexp 'let-7c'
and gid not in (select gid
            from gene join targets using(gid) join miRNA using(mid)
            where miRNA.name regexp 'miR-16');