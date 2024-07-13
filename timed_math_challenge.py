import random
import time 

operators = ["+","-","*"]
min_operand = 1
max_operand = 10
total_problems = 20

def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    print(expr)
    return expr, answer

wrong = 0
print("-----------------")
start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("----------------")
print("you finished in", total_time, "seconds!")
