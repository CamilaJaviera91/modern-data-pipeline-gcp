-- models/mock/mock_products.sql

{{ config(materialized='table') }}

WITH base AS (
    SELECT
        generate_series(1, 100) AS product_id,
        md5(random()::text) AS random_text
),
products AS (
    SELECT
        product_id,
        INITCAP(SUBSTRING(random_text, 1, 10)) || ' ' || INITCAP(SUBSTRING(random_text, 11, 5)) AS product_name,
        (ARRAY['Electronics', 'Clothing', 'Home & Garden'])[floor(random() * 3 + 1)::int] AS category,
        ROUND((random() * 200 + 10)::numeric, 2) AS price,
        floor(random() * 500 + 1)::int AS stock,
        CURRENT_DATE - (trunc(random() * 365)::int) AS created_at
    FROM base
)

SELECT * FROM products