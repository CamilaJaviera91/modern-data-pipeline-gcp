{{ config(
    materialized='table',
    post_hook=[
        "ALTER TABLE {{ this }} ADD CONSTRAINT unique_user_id UNIQUE (user_id)"
    ]
) }}

-- models/mock/mock_users.sql

WITH first_names AS (
    SELECT *
    FROM unnest(ARRAY[
        'Camila', 'Luis', 'Javiera', 'Pedro', 'Ignacia', 'Felipe', 'Sofía', 'José', 'Valentina', 'Andrés', 'Javier'
    ]) WITH ORDINALITY AS t(first_name, id)
),
last_names AS (
    SELECT *
    FROM unnest(ARRAY[
        'Muñoz', 'Pérez', 'González', 'Rojas', 'Contreras', 'Díaz', 'Morales', 'Castro', 'Torres', 'Silva', 'Acevedo'
    ]) WITH ORDINALITY AS t(last_name, id)
),
base AS (
    SELECT 
        generate_series(1, 1000) AS user_id,
        (random() * interval '365 days') AS random_date,
        floor(random() * 10 + 1)::int AS fn_id,
        floor(random() * 10 + 1)::int AS ln_id,
        CASE 
            WHEN random() > 0.5 THEN 'active'
            ELSE 'inactive'
        END AS status
),
user_data AS (
    SELECT
        b.user_id,
        fn.first_name,
        ln.last_name,
        CONCAT(fn.first_name, '_', ln.last_name, '_', b.user_id) AS username,
        CONCAT(fn.first_name, '.', ln.last_name, b.user_id, '@example.com') AS email,
        now() - b.random_date AS created_at,
        b.status,
        CASE
            WHEN b.status = 'active' THEN NULL
            ELSE b.random_date + now()
        END AS terminated_at
    FROM base b
    LEFT JOIN first_names fn ON b.fn_id = fn.id
    LEFT JOIN last_names ln ON b.ln_id = ln.id
)

SELECT * FROM user_data