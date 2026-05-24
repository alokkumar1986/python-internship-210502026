def is_even(n: int) -> bool:
    return n % 2 == 0


def main() -> None:
    try:
        value = input("Enter an integer: ")
        n = int(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if is_even(n):
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")


if __name__ == "__main__":
    main()


