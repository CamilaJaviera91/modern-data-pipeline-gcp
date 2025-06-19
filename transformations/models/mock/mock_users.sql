{{ config(
    materialized='table',
    post_hook=[
        "ALTER TABLE {{ this }} ADD CONSTRAINT unique_user_id UNIQUE (user_id)"
    ]
) }}

-- models/mock/mock_users.sql

WITH base AS (
    SELECT 
    generate_series(1, 1000) AS user_id,
    (random() * interval '365 days') AS random_date,
    CASE 
        WHEN random() > 0.5 THEN 'active'
        ELSE 'inactive'
    END AS status
),
user_data AS (
    SELECT
        user_id,
        CONCAT('User_', user_id) AS username,
        CONCAT('User_', user_id, '@example.com') AS email,
        now() - random_date AS created_at,
        status,
        CASE
            WHEN status = 'active' THEN NULL
            ELSE random_date + now()
        END AS terminated_at
    FROM base
)

SELECT * FROM user_data
