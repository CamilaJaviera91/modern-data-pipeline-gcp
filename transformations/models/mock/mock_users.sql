{{ config(
    materialized='table',
    post_hook=[
        "ALTER TABLE {{ this }} ADD CONSTRAINT unique_user_id UNIQUE (user_id)"
    ]
) }}

-- models/mock/mock_users.sql

WITH user_data AS (
    SELECT 
        generate_series(1, 500) AS user_id,
        md5(random()::text) AS username,
        md5(random()::text) || '@example.com' AS email,
        now() - (random() * interval '365 days') AS created_at,
        CASE WHEN random() > 0.5 THEN 'active' ELSE 'inactive' END AS status
)
SELECT * FROM user_data