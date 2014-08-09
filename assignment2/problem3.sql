
-- select value from (
--     select f1.docid as row_num, f2.docid as col_num, sum(f1.count * f2.count) as value 
--     from frequency as f1, frequency as f2 
--     where f1.term = f2.term 
--     and f1.docid < f2.docid
--     group by f1.docid, f2.docid
-- ) where row_num = '10080_txt_crude' and col_num = '17035_txt_earn';

-- create view aug_frequency as 
--     select * from frequency
--     union
--     select 'q' as docid, 'washington' as term, 1 as count 
--     union
--     select 'q' as docid, 'taxes' as term, 1 as count
--     union 
--     select 'q' as docid, 'treasury' as term, 1 as count;

-- select * from aug_frequency where docid = 'q';

select max(value) from (
    select f1.docid as row_num, f2.docid as col_num, sum(f1.count * f2.count) as value 
    from aug_frequency as f1, aug_frequency as f2 
    where f1.term = f2.term 
    and f1.docid < f2.docid
    group by f1.docid, f2.docid
) where col_num = 'q';
