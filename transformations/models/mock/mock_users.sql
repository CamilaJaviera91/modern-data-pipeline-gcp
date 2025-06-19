{{ config(
    materialized='table',
    post_hook=[
        "ALTER TABLE {{ this }} ADD CONSTRAINT unique_user_id UNIQUE (user_id)"
    ]
) }}

-- models/mock/mock_users.sql

WITH base AS (
    SELECT generate_series(1, 1000) AS user_id
),
user_data AS (
    SELECT
        user_id,
        CONCAT('User_', user_id) AS username,
        CONCAT('User_', user_id, '@example.com') AS email,
        now() - (random() * interval '365 days') AS created_at,
        CASE
            WHEN random() > 0.5 THEN 'active'
            ELSE 'inactive'
        END AS status
    FROM base
)

SELECT * FROM user_data
