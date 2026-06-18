text = input("Enter your text: ")

# keep only letters and spaces
cleaned_chars = []
for ch in text:
    if ch.isalpha() or ch.isspace() or ch.isdigit():
        cleaned_chars.append(ch)

cleaned_text = "".join(cleaned_chars)

choice = input("Type y for hyphen (-) or n for underscore (_): ").strip().lower()

words = cleaned_text.lower().split()

if choice == "y":
    result = "-".join(words)
elif choice == "n":
    result = "_".join(words)
else:
    result = "Invalid choice"

print("File name is:", result)