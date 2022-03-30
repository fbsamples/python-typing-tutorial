
def greet(subject, repeat):
    greeting = "Hello " + subject + "!"
    for _ in range(repeat):
    	print(greeting)

def main():
    repeat_count = input("How many repeats: ")
    greet("World", repeat_count)

if __name__ == "__main__":
    main()
