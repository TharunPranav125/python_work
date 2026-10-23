name = "tharun"
message = f"Hello {name.title()}, would you like to learn some Python today!!\n\n"
print(message)

name = "tharun"
print(name.title())
print(name.upper())
print(name.lower())
print("\n")

name = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
qoute = f'{name.title()} once said, "{message}"'
print(qoute)
print("\n")

name = " tharun "
print("\t")
print(name.lstrip())
print("\n")
print("\t")
print(name.rstrip())
print("\n")
print("\t")
print(name.strip())

url = 'python_notes.txt'
print(url.removesuffix(".txt"))