class Exercise:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned


class FitnessTracker:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def total_duration(self):
        return sum(exercise.duration for exercise in self.exercises)

    def total_calories_burned(self):
        return sum(exercise.calories_burned for exercise in self.exercises)


if __name__ == "__main__":
    # Create a fitness tracker instance
    tracker = FitnessTracker()

    # Add exercises
    tracker.add_exercise(Exercise("Running", 0, 0))  #explanation. The first number is minutes, and second number is calories burned.
    tracker.add_exercise(Exercise("Cycling", 0, 0))
    tracker.add_exercise(Exercise("Swimming", 0, 0))

    # Display statistics
    print("Fitness Tracker Summary:")  #explanation. You can change the name if you want
    print(f"Total Duration: *type your total duration here*{tracker.total_duration()} minutes")
    print(f"Total Calories Burned: *type your burned calories here* {tracker.total_calories_burned()} calories")
