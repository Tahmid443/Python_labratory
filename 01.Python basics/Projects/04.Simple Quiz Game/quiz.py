import random
quiz_data = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .pyt", "B. .py", "C. .pt", "D. .python"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. void", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "What is the output of print(2 ** 3) in Python?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store multiple items in a single variable, ordered and unchangeable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "How do you insert comments in Python code?",
        "options": ["A. #", "B. //", "C. /* */", "D. <!-- -->"],
        "answer": "A"
    }
]

def run_quiz():
    print("=" * 40)
    print("Welcome to the Ultimate Python Quiz!")
    print("=" * 40)
    
    random.shuffle(quiz_data)
    
    score = 0
    total_questions = len(quiz_data)
    
    for index, item in enumerate(quiz_data, start=1):
        print(f"\nQuestion {index}: {item['question']}")
        
        for option in item['options']:
            print(option)
            
        while True:
            user_guess = input("Your answer (A, B, C, or D): ").strip().upper()
            if user_guess in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")
            
        if user_guess == item["answer"]:
            print("✅ Correct! Nicely done.")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {item['answer']}.")
            
    print("\n" + "=" * 40)
    print("GAME OVER!")
    print(f"Your final score: {score}/{total_questions}")
    
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage == 100:
        print("🏆 Perfect! You are a Python Master!")
    elif percentage >= 70:
        print("🎉 Great job! You know your stuff.")
    else:
        print("📚 Keep practicing! Consistency is key.")
    print("=" * 40)

if __name__ == "__main__":
    run_quiz()
