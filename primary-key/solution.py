FROM FROM 
    information_schema.columns c    information_schema.columns c
LEFT JOIN LEFT JOIN 
    information_schema.key_column_usage kcu    information_schema.key_column_usage kcu
    ON c.table_name = kcu.table_name     ON c.table_name = kcu.table_name 
    END AS is_primary_key    END AS is_primary_key
        ELSE 'NO'        ELSE 'NO'
    AND c.column_name = kcu.column_name    AND c.column_name = kcu.column_name
LEFT JOIN LEFT JOIN 