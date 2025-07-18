def main():
    try:
        raw = input("Enter numbers: ")
        tokens = raw.split()
        numbers = []

        for token in tokens:
            number = float(token)
            numbers.append(number)

        min_val = numbers[0]
        max_val = numbers[0]

        for n in numbers:
            if n < min_val:
                min_val = n
            if n > max_val:
                max_val = n

        print(f"Min: {min_val}, Max: {max_val}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
