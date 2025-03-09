-- models/dimensions/dim_payments.sql

WITH raw_payments AS (
    SELECT
        id AS payment_id,
        ride_id,
        stripe_payment_id,
        status,          -- Payment status (succeeded, failed, etc.)
        created_at      -- When the payment was processed
    FROM {{ source('bike_ride_project', 'payments') }} -- Adjust with your actual source name
)

SELECT
    payment_id,
    ride_id,
    stripe_payment_id,
    status,
    created_at
FROM raw_payments
