import sympy 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training the AI operation predictor model (very basic)
data = [
    ("He bought 3 apples and 2 bananas.", "+"),
    ("She lost 5 pencils from her bag.", "-"),
    ("Multiply 6 with 4 to get the total.", "*"),
    ("Divide 20 by 5 to get equal parts.", "/"),
    ("Add 7 to 8.", "+"),
    ("Subtract 10 from 15.", "-"),
]

sentences, labels = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)

# Feature 1: Basic Calculator
def basic_calculator():
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))
    if op == '+': print("Result:", a + b)
    elif op == '-': print("Result:", a - b)
    elif op == '*': print("Result:", a * b)
    elif op == '/': print("Result:", a / b)
    else: print("Invalid operation")

# Feature 2: Solve Linear Equation
def solve_equation():
    eq = input("Enter equation (e.g. 2*x + 3 = 7): ")
    x = sympy.Symbol('x')
    result = sympy.solve(eq, x)
    print("Solution:", result)

# Feature 3: Factorial
def factorial():
    n = int(input("Enter number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

# Feature 4: Prime Checker
def prime_checker():
    n = int(input("Enter number: "))
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

# Feature 5: Area Calculator
def area_calculator():
    choice = input("Choose shape (circle/rectangle/triangle): ").lower()
    if choice == "circle":
        r = float(input("Enter radius: "))
        print("Area:", 3.14 * r * r)
    elif choice == "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area:", l * w)
    elif choice == "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area:", 0.5 * b * h)
    else:
        print("Invalid shape")

# Feature 6: AI Operation Predictor
def operation_predictor():
    sentence = input("Enter math sentence (e.g. 'He added 4 and 5'): ")
    X_test = vectorizer.transform([sentence])
    prediction = model.predict(X_test)[0]
    print("Predicted operation:", prediction)

# Feature 7: Number Pattern Generator
def pattern_generator():
    n = int(input("Enter how many terms: "))
    print("Fibonacci Sequence:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Menu and Main Function
def main():
    while True:
        print("\n--- Smart Math Tool ---")
        print("1. Basic Calculator")
        print("2. Solve Equation")
        print("3. Factorial")
        print("4. Prime Checker")
        print("5. Area Calculator")
        print("6. AI Operation Predictor")
        print("7. Pattern Generator")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")
        
        if choice == '1': basic_calculator()
        elif choice == '2': solve_equation()
        elif choice == '3': factorial()
        elif choice == '4': prime_checker()
        elif choice == '5': area_calculator()
        elif choice == '6': operation_predictor()
        elif choice == '7': pattern_generator()
        elif choice == '8': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()