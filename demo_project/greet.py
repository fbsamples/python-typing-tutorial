
def greet(subject: str) -> None:
    greeting = "Hello " + subject + "!"
    print(greeting)

def main() -> None:
    greet("World")

if __name__ == "__main__":
    main()
