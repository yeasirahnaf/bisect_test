def greet(name): return f"Greetings, {name}!"
def add(a, b): return a + b
def multiply(a, b): return a + b  # BUG!
def divide(a, b): return a / b
def subtract(a, b): return a - b
def power(a, b): return a**b
def modulo(a, b): return a % b
def absolute(a): return abs(a)

if __name__ == "__main__":
    print("Add:", add(2, 3))
    print("Multiply:", multiply(4, 5))
    print("Divide:", divide(10, 2))
    print("Subtract:", subtract(10, 5))
    print("Power:", power(2, 3))
    print("Modulo:", modulo(7, 3))
    print("Absolute:", absolute(-5))
    print("Add:", add(-2, 3))
    print("Multiply:", multiply(0, 5))
    print("Divide:", divide(10, 1))
    print("Absolute:", absolute(0))