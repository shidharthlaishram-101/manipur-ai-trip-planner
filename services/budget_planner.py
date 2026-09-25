class BudgetPlanner:

    def __init__(
        self,
        budget,
        travelers,
        days
    ):
        self.budget = float(budget)
        self.travelers = int(travelers)
        self.days = int(days)

    def calculate_trip_cost(
        self,
        transport_cost,
        entry_fee
    ):
        transport_total = transport_cost * self.travelers
        entry_total = entry_fee * self.travelers

        total_cost = (
            transport_total
            + entry_total
        )

        remaining_budget = self.budget - total_cost

        return {
            "transport_cost": transport_total,
            "entry_fee": entry_total,
            "total_cost": total_cost,
            "remaining_budget": remaining_budget,
            "within_budget": total_cost <= self.budget
        }


if __name__ == "__main__":

    planner = BudgetPlanner(
        budget=10000,
        travelers=2,
        days=3
    )

    result = planner.calculate_trip_cost(
        transport_cost=500,
        entry_fee=50
    )

    print("\nTrip Budget:")
    print(f"Transport: ₹{result['transport_cost']}")
    print(f"Entry Fee: ₹{result['entry_fee']}")
    print(f"Total Cost: ₹{result['total_cost']}")
    print(f"Remaining Budget: ₹{result['remaining_budget']}")
    print(f"Within Budget: {result['within_budget']}")