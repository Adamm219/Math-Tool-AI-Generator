import random
import turtle 

def generate_addition_question(difficulty):

    range_limit = difficulty * 10
    num1 = random.randint(1, range_limit)
    num2 = random.randint(1, range_limit)
    correct_answer = num1 + num2
    print("What is %d + %d?" % (num1, num2))
    return correct_answer

def generate_subtraction_question(difficulty):
    range_limit = difficulty * 10
    num1 = random.randint(1, range_limit)
    num2 = random.randint(1, num1)  
    correct_answer = num1 - num2
    print("What is %d - %d?" % (num1, num2))
    return correct_answer

def generate_division_question(difficulty):
    
    range_limit = difficulty * 10
    divisor = random.randint(1, range_limit)
    quotient = random.randint(1, range_limit)
    dividend = divisor * quotient
    correct_answer = dividend // divisor
    print("What is %d / %d?" % (dividend, divisor))
    return correct_answer

def generate_algebra_question(difficulty):
  
    x = random.randint(1, difficulty * 5)
    num1 = random.randint(1, difficulty * 10)
    num2 = random.randint(1, difficulty * 10)
    result = x * num1 + num2
    correct_answer = x
    print("What is %d * %d + %d?" % (x, num1, num2))
    return correct_answer


def draw_circle():
    t = turtle.Turtle()
    t.circle(50)
    t.hideturtle()
    return "circle"

def draw_square():
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.hideturtle()
    return "square"

def draw_triangle():
    t = turtle.Turtle()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.hideturtle()
    return "triangle"


def draw_rectangle():
    t = turtle.Turtle()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.hideturtle()
    return "rectangle"


def draw_pentagon():
    t = turtle.Turtle()
    for _ in range(5):
        t.forward(100)
        t.left(72)
    t.hideturtle()
    return "pentagon"

def generate_geometry_question():
    shapes = [draw_circle, draw_rectangle, draw_pentagon, draw_triangle, draw_square]
    selected_shape_function = random.choice(shapes)  
    correct_answer = selected_shape_function()        
    return f"Identify the shape drawn on the screen:", correct_answer


def get_question(topic, difficulty):

    if topic == "addition":
        return generate_addition_question(difficulty)
    elif topic == "subtraction":
        return generate_subtraction_question(difficulty)
    elif topic == "division":
        return generate_division_question(difficulty)
    elif topic == "algebra":
        return generate_algebra_question(difficulty)
    elif topic == "geometry":
        return generate_geometry_question()

def main():
    print("Welcome to the Math Practice Program!")
    topics = ["addition", "subtraction", "division", "algebra", "geometry"]
    print("Available topics: ", ", ".join(topics))

    topic = input("Select a topic: ").strip().lower()
    while topic not in topics:
        topic = input("Invalid topic. Please select again: ").strip().lower()

    difficulty = int(input("Select a difficulty level (1-5): "))
    num_questions = int(input("How many questions would you like to answer? "))

    correct_answers = 0

    for _ in range(num_questions):
        question, correct_answer = get_question(topic, difficulty)
        print("\n" + question)
        try:
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print(f"Invalid input! The correct answer was {correct_answer}.")

    accuracy = (correct_answers / num_questions) * 100
    print("\nSession Summary:")
    print(f"Total Questions: {num_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("Hello test")
if _name_ == "_main_":
     main()
