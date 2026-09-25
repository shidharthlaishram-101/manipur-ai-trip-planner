import sqlite3
import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "tourism.db"


def load_destinations():
    """
    Load all destinations from the SQLite database.
    """
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM destinations",
        conn
    )

    conn.close()

    return df


def calculate_preference_score(destination, interests):
    """
    Calculate the user's preference score.

    Dataset scores are stored from 1 to 10.
    Convert the average score to a 0-1 range
    for use by the recommendation algorithm.
    """

    if not interests:
        return 0

    scores = []

    for interest in interests:
        column = f"{interest}_score"

        if column in destination:
            score = float(destination[column])

            # Convert 1-10 score to approximately 0-1
            normalized_score = score / 10

            scores.append(normalized_score)

    if not scores:
        return 0

    return sum(scores) / len(scores)


def calculate_budget_score(destination, budget):
    """
    Estimate whether the destination fits
    within the user's budget.
    """

    estimated_cost = (
        float(destination["estimated_transport_cost"]) +
        float(destination["estimated_food_cost"]) +
        float(destination["entry_fee"])
    )

    if estimated_cost <= budget:
        return 1.0

    # Gradually reduce the score if it exceeds budget
    return max(0, budget / estimated_cost)


def calculate_distance_score(destination):
    """
    Give higher scores to destinations
    closer to Imphal.
    """

    distance = float(
    str(destination["distance_from_imphal"])
    .replace("km", "")
    .strip()
)

    if distance <= 20:
        return 1.0

    elif distance <= 50:
        return 0.8

    elif distance <= 100:
        return 0.6

    elif distance <= 150:
        return 0.4

    else:
        return 0.2


def recommend_destinations(
    budget,
    interests,
    number_of_recommendations=5
):
    """
    Recommend destinations based on:
    - User interests
    - Budget
    - Distance from Imphal
    """

    df = load_destinations()

    results = []

    for _, destination in df.iterrows():

        preference_score = calculate_preference_score(
            destination,
            interests
        )

        budget_score = calculate_budget_score(
            destination,
            budget
        )

        distance_score = calculate_distance_score(
            destination
        )

        # Overall recommendation score
        final_score = (
            0.60 * preference_score +
            0.25 * budget_score +
            0.15 * distance_score
        )

        results.append({
            "name": destination["name"],
            "district": destination["district"],
            "category": destination["category"],
            "description": destination["description"],
            "latitude": destination["latitude"],
            "longitude": destination["longitude"],
            "distance_from_imphal": destination["distance_from_imphal"],
            "estimated_visit_hours": destination["estimated_visit_hours"],
            "entry_fee": destination["entry_fee"],
            "estimated_transport_cost": destination["estimated_transport_cost"],
            "estimated_food_cost": destination["estimated_food_cost"],
            "preference_score": round(preference_score, 3),
            "budget_score": round(budget_score, 3),
            "distance_score": round(distance_score, 3),
            "recommendation_score": round(final_score, 3)
        })

    results_df = pd.DataFrame(results)

    # Sort from highest recommendation score
    results_df = results_df.sort_values(
        by="recommendation_score",
        ascending=False
    )

    return results_df.head(number_of_recommendations)


# Test the recommendation system
if __name__ == "__main__":

    budget = 10000

    interests = [
        "nature",
        "wildlife"
    ]

    recommendations = recommend_destinations(
        budget=budget,
        interests=interests,
        number_of_recommendations=5
    )

    print("\nRecommended destinations:\n")

    print(
        recommendations[
            [
                "name",
                "district",
                "category",
                "recommendation_score"
            ]
        ].to_string(index=False)
    )