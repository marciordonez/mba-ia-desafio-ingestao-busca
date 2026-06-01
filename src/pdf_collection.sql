SELECT
    c.name,
    e.document,
    e.cmetadata
FROM public.langchain_pg_embedding e
INNER JOIN public.langchain_pg_collection c
    ON e.collection_id = c.uuid
WHERE c.name = 'pdf_collection';