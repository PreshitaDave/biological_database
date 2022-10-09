select count(gene) as gene_count, miRNA_id1, miRNA1, miRNA_id2, B.name as miRNA2
from 
(select miRNA_id1, miRNA_id2, gene, A.name as miRNA1 
from 
(
select a.mid as miRNA_id1, b.mid as miRNA_id2, a.gid as gene
from targets a join targets b on a.gid=b.gid and a.mid<b.mid
) pairs join miRNA A on A.mid = miRNA_id1) pairs1
join miRNA B on B.mid = miRNA_id2
group by miRNA_id1, miRNA_id2
order by gene_count desc
limit 10;

