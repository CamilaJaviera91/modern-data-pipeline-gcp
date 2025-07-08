{{ config(
    materialized='table',
    full_refresh=true
) }}

-- models/mock/mock_products.sql

{{ config(materialized='table') }}

WITH base AS (
    SELECT
        generate_series(1, 1000) AS product_id
),
products AS (
    SELECT
        product_id,
        CONCAT('product_', product_id) AS product_name,
        (ARRAY['Electronics', 'Clothing', 'Home & Garden'])[floor(random() * 3 + 1)::int] AS category,
        ROUND((random() * 200 + 10)::numeric, 2) AS price,
        floor(random() * 500 + 1)::int AS stock,
        CURRENT_DATE - (trunc(random() * 365)::int) AS created_at
    FROM base
)

SELECT * FROM products