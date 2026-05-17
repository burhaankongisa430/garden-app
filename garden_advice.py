# =========================================================
# Garden Advice Application
# Provides gardening tips based on season and month
# =========================================================

# TODO:
# 1. Create functions to reduce repeated code
# 2. Add more comments/documentation
# 3. Replace hardcoded values with variables

# Variable storing the current season
season = "Summer"

# Variable storing the current month
month = "January"

# Summer advice
if season == "Summer":
    print("Water plants early in the morning.")
    print("Protect plants from extreme heat.")

# Winter advice
elif season == "Winter":
    print("Reduce watering frequency.")
    print("Protect sensitive plants from frost.")

# Spring advice
elif season == "Spring":
    print("Plant flowers and vegetables.")
    print("Add compost to enrich the soil.")

# Autumn advice
elif season == "Autumn":
    print("Prepare soil for winter.")
    print("Trim dead leaves and branches.")

# Month-specific advice
if month == "January":
    print("January is great for harvesting summer vegetables.")

elif month == "June":
    print("June is ideal for pruning trees.")