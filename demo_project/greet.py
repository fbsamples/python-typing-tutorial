
def greet(subject: str) -> None:
    greeting = "Hello " + subject + "!"
    print(greeting)

def main() -> None:
    repeat_count = int(input("Greet how many times: "))
    greet("World")

if __name__ == "__main__":
    main()
