-- models/analyses/ride_count_by_bike.sql

WITH ride_count_by_bike AS (
    SELECT
        b.bike_id,
        b.model AS bike_model,
        COUNT(f.ride_id) AS ride_count
    FROM {{ ref('dim_bikes') }} b
    JOIN {{ ref('fact_rides') }} f
        ON b.bike_id = f.bike_id
    GROUP BY b.bike_id, b.model
)

SELECT * FROM ride_count_by_bike
