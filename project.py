def greet(name): return f"Greetings, {name}!"
def add(a, b): return a + b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def subtract(a, b): return a - b
def power(a, b): return a**b
def modulo(a, b): return a % b

if __name__ == "__main__":
    print("Add:", add(2, 3))
    print("Multiply:", multiply(4, 5))
    print("Divide:", divide(10, 2))
    print("Subtract:", subtract(10, 5))
    print("Power:", power(2, 3))
    print("Modulo:", modulo(7, 3))