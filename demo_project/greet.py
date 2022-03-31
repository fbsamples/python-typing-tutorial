
def greet(subject, repeat_count):
    greeting = "Hello " + subject + "!"
    for _ in range(repeat_count):
    	print(greeting)

def main():
    repeat_count = input("Greet how many times: ")
    greet("World", repeat_count)

if __name__ == "__main__":
    main()
