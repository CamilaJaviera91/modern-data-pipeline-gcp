-- models/mock/mock_order_items.sql

{{ config(materialized='table') }}

WITH order_ids AS (
    SELECT order_id FROM {{ ref('mock_orders') }}
),
product_ids AS (
    SELECT product_id, price FROM {{ ref('mock_products') }}
),
base AS (
    SELECT
        generate_series(1, 300) AS order_item_id,
        (SELECT order_id FROM order_ids ORDER BY random() LIMIT 1) AS order_id,
        (SELECT product_id FROM product_ids ORDER BY random() LIMIT 1) AS product_id,
        floor(random() * 5 + 1)::int AS quantity
),
order_items AS (
    SELECT
        b.order_item_id,
        b.order_id,
        b.product_id,
        b.quantity,
        ROUND(p.price::numeric, 2) AS item_price
    FROM base b
    LEFT JOIN product_ids p ON b.product_id = p.product_id
)

SELECT * FROM order_items