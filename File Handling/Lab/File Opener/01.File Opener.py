try:
    with open("text.txt", "r") as f:
        print("File found")
except FileNotFoundError:
    print("File not found")