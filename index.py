# Dictionary of states and capitals
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def conduct_quiz():
    score = 0
    total_questions = len(states_and_capitals)

    print("Welcome to the States and Capitals Quiz!")
    print("You will be asked to identify the capital of each state.")
    print("For each correct answer, you get 1 point.\n")

    for state, capital in states_and_capitals.items():
        print(f"Question: What is the capital of {state}?")
        user_answer = input("Your Answer: ").strip()

        if user_answer.lower() == capital.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {capital}.\n")

    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")

if __name__ == "__main__":
    conduct_quiz()
