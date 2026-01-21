with open("sample.txt","wt") as fh:
    fh.write("This is a sample text file\n")
    fh.write("it contains multiple lines\n")
try:
    with open("sample.txt","rt") as fh:
        print("Reading file content:")
        Line1=fh.readline()
        Line2=fh.readline()
        print(f"Line1: {Line1}")
        print(f"Line2: {Line2}")

except FileNotFoundError:
    print("Error: The file sample.txt was not found")
