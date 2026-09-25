from services.recommendation import recommend_destinations
from services.budget_planner import BudgetPlanner
from services.route_optimizer import RouteOptimizer


class TripPlanner:

    def __init__(
        self,
        budget,
        days,
        travelers,
        interests
    ):
        self.budget = float(budget)
        self.days = int(days)
        self.travelers = int(travelers)
        self.interests = interests

    def plan_trip(self):

        # 1. Get recommendations
        recommendations = recommend_destinations(
            budget=self.budget,
            interests=self.interests,
            number_of_recommendations=max(
                self.days * 2,
                5
            )
        )

        destinations = recommendations.to_dict(
            orient="records"
        )

        # 2. Optimize route
        optimizer = RouteOptimizer(
            start_latitude=24.8170,
            start_longitude=93.9368
        )

        route = optimizer.optimize_route(
            destinations
        )

        # 3. Create itinerary
        itinerary = []

        for day in range(1, self.days + 1):
            itinerary.append({
                "day": day,
                "destinations": []
            })

        # Maximum 2 destinations per day
        for index, destination in enumerate(route):

            day_index = index // 2

            if day_index >= self.days:
                break

            itinerary[day_index]["destinations"].append(
                destination
            )

        # 4. Calculate budget
        budget_planner = BudgetPlanner(
            budget=self.budget,
            travelers=self.travelers,
            days=self.days
        )

        total_transport = 0
        total_entry = 0

        for destination in destinations:

            total_transport += float(
                destination["estimated_transport_cost"]
            )

            total_entry += float(
                destination["entry_fee"]
            )

        budget_result = budget_planner.calculate_trip_cost(
            transport_cost=total_transport,
            entry_fee=total_entry
        )

        return {
            "budget": self.budget,
            "days": self.days,
            "travelers": self.travelers,
            "interests": self.interests,
            "itinerary": itinerary,
            "budget_summary": budget_result
        }


def get_user_input():

    print("\n==============================")
    print("     MANIPUR AI TRIP PLANNER")
    print("==============================\n")

    # Budget
    while True:
        try:
            budget = float(
                input("Enter your budget (₹): ")
            )

            if budget <= 0:
                print("Budget must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Days
    while True:
        try:
            days = int(
                input("Enter number of days: ")
            )

            if days <= 0:
                print("Days must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Travelers
    while True:
        try:
            travelers = int(
                input("Enter number of travelers: ")
            )

            if travelers <= 0:
                print("Travelers must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Interests
    print("\nAvailable interests:")
    print("nature")
    print("culture")
    print("adventure")
    print("wildlife")
    print("heritage")
    print("food")
    print("family")

    interests_input = input(
        "\nEnter your interests separated by commas: "
    )

    interests = [
        interest.strip().lower()
        for interest in interests_input.split(",")
        if interest.strip()
    ]

    return budget, days, travelers, interests


if __name__ == "__main__":

    budget, days, travelers, interests = get_user_input()

    planner = TripPlanner(
        budget=budget,
        days=days,
        travelers=travelers,
        interests=interests
    )

    result = planner.plan_trip()

    print("\n==============================")
    print("     YOUR MANIPUR TRIP")
    print("==============================")

    print(f"\nBudget: ₹{result['budget']}")
    print(f"Days: {result['days']}")
    print(f"Travelers: {result['travelers']}")
    print(
        f"Interests: "
        f"{', '.join(result['interests'])}"
    )

    print("\nManipur Trip Itinerary\n")

    for day in result["itinerary"]:

        print(f"Day {day['day']}")

        if not day["destinations"]:
            print("  No destination assigned")
        else:
            for destination in day["destinations"]:
                print(
                    f"  - {destination['name']}"
                )

        print()

    print("------------------------------")
    print("Budget Summary")
    print("------------------------------")

    budget = result["budget_summary"]

    print(
        f"Transport: ₹{budget['transport_cost']}"
    )

    print(
        f"Entry Fees: ₹{budget['entry_fee']}"
    )

    print(
        f"Total Estimated Cost: "
        f"₹{budget['total_cost']}"
    )

    print(
        f"Remaining Budget: "
        f"₹{budget['remaining_budget']}"
    )

    print(
        f"Within Budget: "
        f"{budget['within_budget']}"
    )