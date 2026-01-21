with open("output.txt","wt") as fh:
    user_input1 = input("Enter text to write to the file: ")
    with open("output.txt", 'w') as fh:
        fh.write(user_input1 + "\n")
    print(f"Data successfully written to {fh}.\n")


    user_input2 = input("Enter additional text to append: ")
    with open("output.txt", 'a') as fh:
        fh.write(user_input2 + "\n")
    print("Data successfully appended.\n")

    print(f"Final content of {fh}:")
    with open("output.txt", 'r') as fh:
        print(fh.read())
