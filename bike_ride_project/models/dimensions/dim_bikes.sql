-- models/dimensions/dim_bikes.sql

WITH raw_bikes AS (
    SELECT
        id AS bike_id,
        model,
        status,
        location,
        created_at
    FROM {{ source('bike_ride_project', 'bikes') }} -- Adjust with your actual source name
)

SELECT
    bike_id,
    model,
    status,
    location,
    created_at
FROM raw_bikes
