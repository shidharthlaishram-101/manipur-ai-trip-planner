class UserPreferences:
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

    def to_dict(self):
        return {
            "budget": self.budget,
            "days": self.days,
            "travelers": self.travelers,
            "interests": self.interests
        }


if __name__ == "__main__":

    preferences = UserPreferences(
        budget=10000,
        days=3,
        travelers=2,
        interests=["nature", "wildlife"]
    )

    print("User Preferences:")
    print(preferences.to_dict())