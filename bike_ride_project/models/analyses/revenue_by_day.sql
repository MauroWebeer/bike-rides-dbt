-- models/analyses/revenue_by_day.sql

WITH revenue_by_day AS (
    SELECT
        DATE(f.start_time) AS day,
        SUM(f.payment_amount) AS daily_revenue
    FROM {{ ref('fact_rides') }} f
    WHERE f.payment_status = 'succeeded'
    GROUP BY day
)

SELECT * FROM revenue_by_day
