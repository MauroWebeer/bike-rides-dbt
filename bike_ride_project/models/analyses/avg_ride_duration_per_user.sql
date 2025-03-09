-- models/analyses/avg_ride_duration_per_user.sql

WITH avg_duration_by_user AS (
    SELECT
        u.user_id,
        u.name AS user_name,
        AVG(f.ride_duration_minutes) AS avg_ride_duration_minutes
    FROM {{ ref('dim_users') }} u
    JOIN {{ ref('fact_rides') }} f
        ON u.user_id = f.user_id
    GROUP BY u.user_id, u.name
)

SELECT * FROM avg_duration_by_user
