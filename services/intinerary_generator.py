class ItineraryGenerator:

    def __init__(self, days):
        self.days = int(days)

    def generate_itinerary(self, destinations):

        itinerary = []

        # Create empty days
        for day in range(1, self.days + 1):
            itinerary.append({
                "day": day,
                "destinations": []
            })

        # Distribute destinations across days
        for index, destination in enumerate(destinations):
            day_index = index % self.days

            itinerary[day_index]["destinations"].append(
                destination
            )

        return itinerary


if __name__ == "__main__":

    destinations = [
        {
            "name": "Keibul Lamjao National Park"
        },
        {
            "name": "Shirui Hills"
        },
        {
            "name": "Loktak Lake"
        },
        {
            "name": "Khonghampat Orchidarium"
        },
        {
            "name": "Zeilad Lake"
        }
    ]

    planner = ItineraryGenerator(days=3)

    itinerary = planner.generate_itinerary(
        destinations
    )

    print("\nManipur Trip Itinerary\n")

    for day in itinerary:

        print(f"Day {day['day']}")

        for destination in day["destinations"]:
            print(f"  - {destination['name']}")

        print()