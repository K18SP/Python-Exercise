questions = [
    ["Best cricketer of India?", "Virat", "Dhoni", "Sachin", "Rohit", 1],
    ["Who is PM of India?", "Modi", "Rahul", "Sonia", "None of the above", 1],
    ["Which is the best Shoe company?", "Nike", "Puma", "NB", "Adidas", 1],
    ["Best cricketer of India?", "Virat", "Dhoni", "Sachin", "Rohit", 1],
    ["Who is PM of India?", "Modi", "Rahul", "Sonia", "None of the above", 1],
    ["Which is the best Shoe company?", "Nike", "Puma", "NB", "Adidas", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(questions)):
    question = questions[i]

    print(f"Question for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}  b. {question[2]}")
    print(f"c. {question[3]}  d. {question[4]}")

    reply = input("Enter your answer (a, b, c, d): ").strip().lower()

    if reply == 'abcd'[question[-1]-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 1000000
    else:
        print(f"Incorrect answer, correct answer is {'abcd'[question[-1]-1]}")

print(f"Your take-home money is Rs. {money}")
