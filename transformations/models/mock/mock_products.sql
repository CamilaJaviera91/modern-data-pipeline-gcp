-- models/mock/mock_products.sql

with products as (
    select
        generate_series(1, 100) as product_id,
        -- Nombre del producto: Producto + número
        concat('Product ', generate_series(1, 100)) as product_name,
        -- Categorías mock
        case
            when random() < 0.3 then 'Electronics'
            when random() < 0.6 then 'Clothing'
            else 'Home & Garden'
        end as category,
        -- Precio entre 5 y 1000 con 2 decimales
        round((random() * 995 + 5)::numeric, 2) as price,
        -- Stock entre 0 y 100 unidades
        floor(random() * 101)::int as stock,
        -- Fecha aleatoria de creación en últimos 2 años
        (current_date - (random() * 730)::int) as created_at
)
select * from products
