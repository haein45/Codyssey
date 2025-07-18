def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b
def calculate(expression):
    operators = {'+': add, '-': subtract, '*': multiply, '/': divide}
    try:
        tokens = expression.strip().split()
        if len(tokens) % 2 == 0:
            print("Invalid input.")
            return

        nums = []
        ops = []

        for i, token in enumerate(tokens):
            if i % 2 == 0:
                try:
                    nums.append(float(token))
                except ValueError:
                    print("Invalid input.")
                    return
            else:
                if token not in operators:
                    print("Invalid input.")
                    return
                ops.append(token)

        i = 0
        while i < len(ops):
            if ops[i] in ('*', '/'):
                result = operators[ops[i]](nums[i], nums[i+1])
                if result is None:
                    return
                nums[i] = result
                del nums[i+1]
                del ops[i]
            else:
                i += 1
        result = nums[0]
        for i, op in enumerate(ops):
            result = operators[op](result, nums[i+1])

        print(f"Result: {result}")

    except Exception:
        print("Invalid input.")

def main():
    expression = input("Enter expression: ")
    calculate(expression)

if __name__ == "__main__":
    main()
