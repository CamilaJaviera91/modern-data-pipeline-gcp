-- models/mock/mock_orders.sql

WITH order_data AS (
    SELECT 
        generate_series(1, 200) AS order_id,
        floor(random() * 500 + 1)::int AS user_id,  -- IDs between 1 y 100
        now() - (random() * interval '180 days') AS order_date,
        round((random() * 500 + 10)::numeric, 2) AS amount,
        CASE 
            WHEN random() > 0.8 THEN 'cancelled'
            WHEN random() > 0.5 THEN 'shipped'
            ELSE 'processing'
        END AS status
)
SELECT * FROM order_data
