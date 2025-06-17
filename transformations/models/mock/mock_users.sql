-- models/mock/mock_users.sql

WITH raw_data AS (
    SELECT 
        generate_series(1, 100) AS user_id,
        md5(random()::text) AS hash,
        now() - (random() * interval '365 days') AS created_at,
        CASE WHEN random() > 0.5 THEN 'active' ELSE 'inactive' END AS status
)
SELECT 
    user_id,
    CONCAT('user_', user_id) AS username,
    CONCAT(hash, '@example.com') AS email,
    created_at,
    status
FROM raw_data