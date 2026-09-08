participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

if len(participants) != len(scores):
    print("Error: Participants and scores lists have different lengths!")
    exit()

def add_participant():
    while True:
        name = input("Enter participant's name (or 'quit' to stop): ").strip()
        if name.lower() == 'quit':
            return False
        if name == "":
            print("Error: Name cannot be empty!")
            continue
        if name in participants:
            print(f"Error: {name} is already registered!")
            continue
        score_input = input("Enter participant's score (0-100): ").strip()
        try:
            score = float(score_input)
            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100!")
                continue
        except ValueError:
            print("Error: Score must be a number!")
            continue
        participants.append(name)
        scores.append(score)
        print(f"{name} has been successfully registered with score {score}!")
        return True

def search_participant():
    name = input("Enter the name of the participant to search: ").strip()
    if name == "":
        print("Error: Name cannot be empty!")
        return
    if name in participants:
        idx = participants.index(name)
        score = scores[idx]
        print(f"\nName: {name}")
        print(f"Score: {score}")
        if score >= distinction_score:
            print("Status: DISTINCTION")
        elif score >= qualification_score:
            print("Status: QUALIFIED")
        else:
            print("Status: NOT QUALIFIED")
    else:
        print(f"Participant '{name}' not found.")

def display_all_participants():
    print("\n=== All Participants with Qualification Status ===")
    for name, score in zip(participants, scores):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"{name}: {score} - {status}")
    print()

def check_distinction_and_passed():
    has_distinction = any(score >= distinction_score for score in scores)
    all_passed = all(score >= 50 for score in scores)
    print("\n=== Status Checks ===")
    if has_distinction:
        print("✓ At least one participant has a DISTINCTION")
    else:
        print("✗ No participant has a DISTINCTION")
    if all_passed:
        print("✓ All participants have PASSED (score >= 50)")
    else:
        print("✗ Not all participants have PASSED")
    print()

def update_score():
    name = input("Enter the participant's name to update score: ").strip()
    if name == "":
        print("Error: Name cannot be empty!")
        return
    if name not in participants:
        print(f"Error: {name} not found in the participant list!")
        return
    score_input = input("Enter the new score (0-100): ").strip()
    try:
        new_score = float(score_input)
        if new_score < 0 or new_score > 100:
            print("Error: Score must be between 0 and 100!")
            return
    except ValueError:
        print("Error: Score must be a number!")
        return
    idx = participants.index(name)
    old_score = scores[idx]
    scores[idx] = new_score
    print(f"{name}'s score has been updated from {old_score} to {new_score}!")

def remove_participant():
    name = input("Enter the participant's name to remove: ").strip()
    if name == "":
        print("Error: Name cannot be empty!")
        return
    if name not in participants:
        print(f"Error: {name} not found in the participant list!")
        return
    idx = participants.index(name)
    removed_name = participants.pop(idx)
    removed_score = scores.pop(idx)
    print(f"{removed_name} (score: {removed_score}) has been removed from the list.")

def display_scoreboard():
    print("\n=== Scoreboard (Descending Order) ===")
    sorted_pairs = sorted(zip(scores, participants), reverse=True)
    for rank, (score, name) in enumerate(sorted_pairs, 1):
        print(f"#{rank}: {name} - {score}")
    print()

def calculate_statistics():
    if not scores:
        print("No participants to calculate statistics!")
        return
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    num_highest = scores.count(highest)
    num_lowest = scores.count(lowest)
    num_distinction = sum(1 for s in scores if s >= distinction_score)
    num_qualified = sum(1 for s in scores if qualification_score <= s < distinction_score)
    num_not_qualified = sum(1 for s in scores if s < qualification_score)
    print("\n=== Statistics ===")
    print(f"Highest Score: {highest} (by {num_highest} participant(s))")
    print(f"Lowest Score: {lowest} (by {num_lowest} participant(s))")
    print(f"Average Score: {average:.2f}")
    print(f"Participants with DISTINCTION: {num_distinction}")
    print(f"Participants QUALIFIED: {num_qualified}")
    print(f"Participants NOT QUALIFIED: {num_not_qualified}")
    print()

def generate_final_report():
    print("\n" + "="*60)
    print("FINAL REPORT")
    print("="*60)
    sorted_pairs = sorted(zip(scores, participants), reverse=True)
    print("\n=== Participant Rankings ===")
    for rank, (score, name) in enumerate(sorted_pairs, 1):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"#{rank}: {name} - Score: {score} - {status}")
    calculate_statistics()
    print("="*60)

def main():
    print("=== Current Participants ===")
    for name, score in zip(participants, scores):
        print(f"{name}: {score}")
    print()
    while True:
        print("\n" + "="*50)
        print("PARTICIPANT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Display all participants")
        print("2. Add a new participant")
        print("3. Search for a participant")
        print("4. Update a participant's score")
        print("5. Remove a participant")
        print("6. Display scoreboard")
        print("7. Check distinction and passed status")
        print("8. Calculate statistics")
        print("9. Generate final report")
        print("10. Exit")
        choice = input("\nEnter your choice (1-10): ").strip()
        if choice == "1":
            display_all_participants()
        elif choice == "2":
            add_participant()
        elif choice == "3":
            search_participant()
        elif choice == "4":
            update_score()
        elif choice == "5":
            remove_participant()
        elif choice == "6":
            display_scoreboard()
        elif choice == "7":
            check_distinction_and_passed()
        elif choice == "8":
            calculate_statistics()
        elif choice == "9":
            generate_final_report()
        elif choice == "10":
            print("Thank you for using the Participant Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
