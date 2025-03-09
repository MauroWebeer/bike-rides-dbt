-- models/facts/fact_ride.sql

WITH raw_ride_data AS (
    SELECT
        r.id AS ride_id,
        r.user_id,
        r.bike_id,
        r.start_time,
        EXTRACT(EPOCH FROM (r.end_time - r.start_time)) / 60 AS ride_duration_minutes,
        r.distance_km,
        p.amount AS payment_amount,
        p.currency,
        p.status AS payment_status,
        r.status AS ride_status
    FROM {{ source('bike_ride_project', 'rides') }} r
    LEFT JOIN {{ source('bike_ride_project', 'payments') }} p ON r.id = p.ride_id
)

SELECT
    ride_id,
    user_id,
    bike_id,
    start_time,
    ride_duration_minutes,
    distance_km,
    payment_amount,
    currency,
    payment_status,
    ride_status
FROM raw_ride_data
