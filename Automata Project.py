import re
import os


#Intelligent Number & Email Extractor

def extract_data(text):
    #REGEX patterns work like DFA/NFA recognizers

    phone_pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    phones = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)

    return phones, emails


def read_from_file():
    filename = input("\nEnter filename (example: input.txt): ")

    if not os.path.exists(filename):
        print(" File not found!\n")
        return None

    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def save_results(phones, emails):
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Extracted Phone Numbers:\n")
        for p in phones:
            f.write(p + "\n")

        f.write("\nExtracted Emails:\n")
        for e in emails:
            f.write(e + "\n")

    print("\n Results saved to 'results.txt'")


#Main Program

print("===============================================")
print(" Intelligent Phone Number & Email Extractor ")
print("===============================================\n")

while True:
    print("\nChoose input method:")
    print("1. Enter text manually")
    print("2. Read input from file")
    print("3. Exit")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        user_text = input("\nEnter your text here:\n")
        phones, emails = extract_data(user_text)

    elif choice == "2":
        file_data = read_from_file()
        if file_data is None:
            continue
        phones, emails = extract_data(file_data)

    elif choice == "3":
        print("\nThank you for using the Extractor. Goodbye!")
        break

    else:
        print(" Invalid choice! Try again.")
        continue

    #results
    print("\n Phone Numbers Found:")
    print("------------------------")
    if phones:
        for p in phones: print("→", p)
    else: print("None found.")

    print("\n Emails Found:")
    print("------------------")
    if emails:
        for e in emails: print("→", e)
    else: print("None found.")

    save_results(phones, emails)
    print("\n Extraction Completed Successfully!")


