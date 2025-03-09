CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE bikes (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('available', 'in_use', 'maintenance')) DEFAULT 'available',
    location POINT,  -- (latitude, longitude)
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE rides (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    bike_id INT REFERENCES bikes(id) ON DELETE SET NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    distance_km DECIMAL(5,2),  -- Optional: Store ride distance
    cost DECIMAL(10,2),
    status VARCHAR(20) CHECK (status IN ('ongoing', 'completed', 'canceled')) DEFAULT 'ongoing',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    ride_id INT REFERENCES rides(id) ON DELETE CASCADE,
    stripe_payment_id VARCHAR(50) UNIQUE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    status VARCHAR(20) CHECK (status IN ('succeeded', 'failed', 'pending')),
    created_at TIMESTAMP DEFAULT NOW()
);
