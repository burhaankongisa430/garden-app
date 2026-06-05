"""
garden_advice.py

A simple gardening advice app that provides tips based on the
current month and season.
"""

import datetime

# TODO: Replace these hardcoded month-to-season mappings with a dictionary or function

def get_season(month):
    """
    Determine the season based on a given month number.

    Args:
        month (int): The month as an integer (1-12).

    Returns:
        str: The name of the current season.
    """
    if month in [12, 1, 2]:
        return "Summer"      # Southern Hemisphere
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

def get_advice(season):
    """
    Return gardening advice for a given season.

    Args:
        season (str): The name of the season.

    Returns:
        str: A gardening tip relevant to that season.
    """
    # TODO: Consider moving advice strings into a dictionary instead of if/elif chain
    if season == "Summer":
        advice = "Water your plants early in the morning or late evening to reduce evaporation. Watch out for pests."
    elif season == "Autumn":
        advice = "Start planting bulbs for spring blooms. Clear fallen leaves to prevent mould."
    elif season == "Winter":
        advice = "Protect frost-sensitive plants with mulch or fleece. Focus on planning next year's garden."
    elif season == "Spring":
        advice = "Great time to plant vegetables and flowers. Keep an eye on late frosts."
    else:
        advice = "No advice available for this season."
    return advice

# TODO: Wrap the main logic in a main() function and use if __name__ == "__main__"

current_month = datetime.datetime.now().month
current_season = get_season(current_month)
advice = get_advice(current_season)

print(f"Current month: {current_month}")
print(f"Season: {current_season}")
print(f"Gardening advice: {advice}")