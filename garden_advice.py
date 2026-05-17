# =========================================================
# Garden Advice Application
# Provides gardening advice based on season and month
# =========================================================


# ---------------------------------------------------------
# Function: seasonal_advice
# Displays gardening advice based on the season
# ---------------------------------------------------------
def seasonal_advice(season):

    if season == "Summer":
        print("Water plants early in the morning.")
        print("Protect plants from extreme heat.")

    elif season == "Winter":
        print("Reduce watering frequency.")
        print("Protect sensitive plants from frost.")

    elif season == "Spring":
        print("Plant flowers and vegetables.")
        print("Add compost to enrich the soil.")

    elif season == "Autumn":
        print("Prepare soil for winter.")
        print("Trim dead leaves and branches.")


# ---------------------------------------------------------
# Function: monthly_advice
# Displays gardening advice based on the month
# ---------------------------------------------------------
def monthly_advice(month):

    if month == "January":
        print("January is great for harvesting summer vegetables.")

    elif month == "June":
        print("June is ideal for pruning trees.")


# Store current season
season = "Summer"

# Store current month
month = "January"

# Execute seasonal advice
seasonal_advice(season)

# Execute monthly advice
monthly_advice(month)