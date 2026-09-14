#Fitness tracker

number = 0
results = []
sessions = int(input("How many workout sessions have you had this week? "))

for session in results(sessions):
    results = input(f"Enter workout for session {number} (cardio/strength/flexibility): ")
    number += 1
    if number == sessions:
        print("Workout summary:")
        