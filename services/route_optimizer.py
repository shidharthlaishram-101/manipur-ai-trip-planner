import math


class RouteOptimizer:

    def __init__(self, start_latitude, start_longitude):
        self.start_latitude = float(start_latitude)
        self.start_longitude = float(start_longitude)

    def calculate_distance(
        self,
        lat1,
        lon1,
        lat2,
        lon2
    ):
        """
        Calculate approximate distance between
        two geographical coordinates using Haversine formula.
        """

        R = 6371  # Earth radius in km

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return R * c

    def optimize_route(self, destinations):

        remaining = destinations.copy()

        current_lat = self.start_latitude
        current_lon = self.start_longitude

        optimized_route = []

        while remaining:

            nearest = min(
                remaining,
                key=lambda destination:
                self.calculate_distance(
                    current_lat,
                    current_lon,
                    float(destination["latitude"]),
                    float(destination["longitude"])
                )
            )

            distance = self.calculate_distance(
                current_lat,
                current_lon,
                float(nearest["latitude"]),
                float(nearest["longitude"])
            )

            optimized_route.append({
                "name": nearest["name"],
                "latitude": nearest["latitude"],
                "longitude": nearest["longitude"],
                "distance_from_previous": round(
                    distance, 2
                )
            })

            current_lat = float(nearest["latitude"])
            current_lon = float(nearest["longitude"])

            remaining.remove(nearest)

        return optimized_route


if __name__ == "__main__":

    destinations = [
        {
            "name": "Loktak Lake",
            "latitude": 24.5276,
            "longitude": 93.7800
        },
        {
            "name": "Keibul Lamjao National Park",
            "latitude": 24.5087,
            "longitude": 93.8157
        },
        {
            "name": "Khonghampat Orchidarium",
            "latitude": 24.8667,
            "longitude": 93.9167
        }
    ]

    # Imphal starting point
    optimizer = RouteOptimizer(
        start_latitude=24.8170,
        start_longitude=93.9368
    )

    route = optimizer.optimize_route(
        destinations
    )

    print("\nOptimized Route:\n")

    for number, destination in enumerate(
        route,
        start=1
    ):
        print(
            f"{number}. {destination['name']} "
            f"({destination['distance_from_previous']} km)"
        )