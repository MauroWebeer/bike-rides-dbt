import random
from faker import Faker
import psycopg2
from datetime import datetime, timedelta

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",  # Change if needed
    database="bike_ride_project",  # Your database name
    user="dbt_user",  # Your database user
    password="password"  # Your database password
)
cursor = conn.cursor()

fake = Faker()

# Utility functions
def create_user():
    """Create a random user."""
    name = fake.name()
    email = fake.email()
    created_at = fake.date_this_decade()
    cursor.execute("""
        INSERT INTO users (name, email, created_at)
        VALUES (%s, %s, %s) RETURNING id
    """, (name, email, created_at))
    return cursor.fetchone()[0]

def create_bike():
    """Create a random bike."""
    models = [
        "Trek FX 3", "Giant Escape 2", "Cannondale Quick", "Specialized Sirrus", "Schwinn Discover",
        "Bianchi Infinito", "Merida Reacto", "Salsa Vaya", "Santa Cruz Tallboy", "Felt VR30",
        "Pinarello Dogma", "Scott Addict", "Cervelo R5", "Orbea Orca", "Colnago C64",
        "Rad Power Bikes RadRover", "Norco Search XR", "Trek Domane", "Specialized S-Works Venge",
        "Kona Process 153", "Fuji Norcom Straight", "Cannondale Synapse", "BMC Teammachine",
        "Diamondback Century", "Raleigh Revenio", "Rocky Mountain Element", "Ibis Ripmo", "Salsa Beargrease",
        "Surly Moonlander", "Giant Trance", "Yeti SB130", "Marin Hawk Hill", "GT Avalanche",
        "Haro Double Peak", "Evil Insurgent", "Pivot Mach 4", "Canyon Ultimate", "Borealis Flume",
        "Trek Madone", "Specialized Turbo Vado", "Raleigh Talus", "BMC Roadmachine", "Mondraker Foxy",
        "Canyon Spectral", "Norco Optic", "Bianchi Aria", "Raleigh Camargue", "RockShox Reverb",
        "Trek Slash", "Surly Krampus", "Intense Tracer", "Santa Cruz Hightower", "Santa Cruz Chameleon",
        "Cube Reaction", "Marin Nail Trail", "KHS SixFifty", "Felt Virtue", "GT Force",
        "Mongoose Dolomite", "Orbea Alma", "Trek Superfly", "Specialized Epic", "Cannondale Scalpel",
        "Bianchi Oltre XR4", "Basso Diamante", "Merida Big Nine", "Kona Honzo", "Giant Reign",
        "Cube Stereo", "Pivot Trail 429", "Yeti SB150", "Norco Range", "Ragley Blue Pig"
    ]
    status = random.choice(["available", "in_use", "maintenance"])
    location = f"({random.uniform(-180, 180)}, {random.uniform(-90, 90)})"  # Random location (longitude, latitude)
    created_at = fake.date_this_decade()
    cursor.execute("""
        INSERT INTO bikes (model, status, location, created_at)
        VALUES (%s, %s, %s, %s) RETURNING id
    """, (random.choice(models), status, location, created_at))
    return cursor.fetchone()[0]

from datetime import datetime, timedelta
import random

def create_ride(user_id, bike_id):
    """Create a random ride."""
    # Generate a random start time within the last 30 days
    start_time = datetime.now() - timedelta(days=random.randint(0, 30))  # Random start time
    
    # Generate a random ride duration (between 10 and 180 minutes)
    duration_minutes = random.randint(10, 180)  # Ensure the duration is always positive
    end_time = start_time + timedelta(minutes=duration_minutes)  # Add duration to start time

    distance_km = random.randint(1, 50)  # Random distance in km
    cost = round(distance_km * 0.5, 2)  # Simple pricing model based on distance
    status = random.choice(["completed", "ongoing"])  # Random ride status
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp as created_at

    #print(f"Start Time: {start_time}, End Time: {end_time}")  # Debug print for checking the times

    cursor.execute("""
        INSERT INTO rides (user_id, bike_id, start_time, end_time, distance_km, cost, status, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    """, (user_id, bike_id, start_time, end_time, distance_km, cost, status, created_at))
    
    return cursor.fetchone()[0], cost


def create_payment(ride_id, amount):
    """Create a payment for the ride."""
    stripe_payment_id = fake.uuid4()
    currency = "USD"
    status = random.choice(["succeeded", "failed", "pending"])
    created_at = fake.date_this_decade()

    cursor.execute("""
        INSERT INTO payments (ride_id, stripe_payment_id, amount, currency, status, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (ride_id, stripe_payment_id, amount, currency, status, created_at))

# Populate the tables with data
try:
    # Create 10,000 users and store their IDs
    print("Creating users...")
    user_ids = []  # List to store created user IDs
    for _ in range(1000):
        user_id = create_user()
        user_ids.append(user_id)

    # Create 50 bikes
    print("Creating bikes...")
    bikes = [create_bike() for _ in range(25)]

    # Create rides and payments
    print("Creating rides and payments...")
    for _ in range(1000):
        user_id = random.choice(user_ids)  # Randomly select an existing user_id
        bike_id = random.choice(bikes)  # Random bike
        ride_id, ride_cost = create_ride(user_id, bike_id)
        create_payment(ride_id, ride_cost)

    # Commit all changes
    conn.commit()
    print("Data populated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()

