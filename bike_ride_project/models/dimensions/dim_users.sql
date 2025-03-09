-- models/dimensions/dim_users.sql

WITH raw_users AS (
    SELECT
        id AS user_id,
        name,
        email,
        created_at
    FROM {{ source('bike_ride_project', 'users') }} -- Adjust with your actual source name
)

SELECT
    user_id,
    name,
    email,
    created_at
FROM raw_users
