def main():
    name = input("What's your name? ")
    if len(name) > 1:
        first, last = name.split()
        print(f"hello, {first}")
    else:
        print(f"hello, {name}")

if __name__ == "__main__":
    main()