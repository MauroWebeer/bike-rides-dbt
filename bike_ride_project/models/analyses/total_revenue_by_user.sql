-- models/analyses/total_revenue_by_user.sql

WITH revenue_by_user AS (
    SELECT
        u.user_id,
        u.name AS user_name,
        SUM(f.payment_amount) AS total_revenue
    FROM {{ ref('dim_users') }} u
    JOIN {{ ref('fact_rides') }} f
        ON u.user_id = f.user_id
    WHERE f.payment_status = 'succeeded'
    GROUP BY u.user_id, u.name
)

SELECT * FROM revenue_by_user
