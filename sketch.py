def top():
    print("  _______")
    print(" /       \\")
    print("/         \\")

def bottom():
    print("\         /")
    print(" \_______/")

def line():
    print('''-\"-\'-\"-\'-\"-''')

def main():
    top()
    bottom()
    print("\n")
    line()
    print("\n")
    top()
    bottom()
    print("\n")
    line()
    bottom()
    print("\n")
    top()
    line()
    bottom()

if __name__ == "__main__":
    main()
