import random
import json

d = "Which operation do you want? (+, -, *, /) or type 'all' for random: "
while True:
    a = input("enter how many data you need?")
    try:
        a = int(a)
        break
    except:
        print("enter a number!")
while True:
    k = input("enter what number you want to in your range data:")
    try:
        k = int(k)
        break
    except:
        print("enter a number!!")
while True:
    c = input(d)
    if c == "+":
        break
    elif c == "-":
        break
    elif c == "*":
        break
    elif c == "/":
        break
    elif c in ("all", "all of them"):
        break
    else:
        print(f"choose one of them or all of them")
        break
      
data = []
seen_problems = set()  

for i in range(1, a+1):
    while True:  
        if c == "+":
            op = ("+")
        elif c == "-":
            op = ("-")
        elif c == "*":
            op = ("*")
        elif c == "/":
            op = ("/")
        elif c == "all of them " or "all":
            op = random.choice(("+","-","*","/"))

        num_1 = random.randint(1,k)
        num_2 = random.randint(1,k)

        if op == "+":
            ans = num_1 + num_2
            problem = f"{num_1} + {num_2}"
            solution = f"{problem} = {ans}"
        elif op == "-":
            if num_1 >= num_2:
                ans = num_1 - num_2
                problem = f"{num_1} - {num_2}"
                solution = f"{problem} = {ans}"
            else:
                ans = num_2 - num_1
                problem = f"{num_2} - {num_1}"
                solution = f"{problem} = {ans}"
        elif op == "*":
            if num_1 == 1 or num_2 == 1:
                ans = num_1 * num_2
                problem = f"{num_1} * {num_2}"
                solution= f"{problem} = {ans}"
            else:
                ans = num_1 * num_2
                problem = f"{num_1} * {num_2}"
                solution = f"{problem} = {ans}"
        elif op == "/":
            num_1 = random.randint(1, k) 
            ans = random.randint(1, k)  
            num_2 = num_1 * ans     
            problem = f"{num_2} / {num_1}"
            solution = f"{problem} = {ans}"

        if problem not in seen_problems: 
            seen_problems.add(problem)
            break 
    data.append({
        "id": i,
        "problem": problem,
        "solution": solution,
        "answer": str(ans), 
        "operation": op,
        "number_one" : num_1,
        'number_two' : num_2
        })
    
       
with open("dataset.json", "w", encoding="utf-8")as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
print(f"{len(data)} simpel saved!")