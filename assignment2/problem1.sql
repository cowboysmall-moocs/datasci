-- select count(*) from (
--     select * from frequency where docid = '10398_txt_earn'
-- ) x;

-- select count(*) from (
--     select term from frequency where docid = '10398_txt_earn' and count = 1
-- ) x;

-- select count(*) from (
--     select term from frequency where docid = '10398_txt_earn' and count = 1
--     union
--     select term from frequency where docid = '925_txt_trade' and count = 1
-- ) x;

-- select count(*) from frequency where term = 'parliament';

-- select count(*) from (
--     select docid, sum(count) as term_count from frequency group by docid having term_count > 300
-- ) x;

-- select count(*) from (
--     select docid, term from frequency where term = 'transactions' and docid in (
--         select docid from frequency where term = 'world'
--     )
-- ) x;

select count(*) from (
    select f1.docid, f1.term as term1, f2.term as term1 
        from frequency as f1 
        inner join frequency as f2 
        on f1.docid = f2.docid 
        and f1.term = 'transactions' 
        and f2.term = 'world'
) x;

