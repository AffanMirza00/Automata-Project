import re
import os

#  Intelligent Number & Email Extractor with DFA & NFA Demonstration

#REGEX EXTRACTOR
def extract_data(text):
    phone_pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    phones = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)

    return phones, emails


def save_results(phones, emails):
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Extracted Phone Numbers:\n")
        for p in phones:
            f.write(p + "\n")

        f.write("\nExtracted Emails:\n")
        for e in emails:
            f.write(e + "\n")

    print("\n Results saved to results.txt")


#DFA EMAIL VALIDATOR
def is_valid_email(email):
    state = "q0"

    for ch in email:
        if state == "q0":
            if ch.isalnum(): state = "q1"
            else: return False

        elif state == "q1":
            if ch.isalnum() or ch in "._": state = "q1"
            elif ch == "@": state = "q2"
            else: return False

        elif state == "q2":
            if ch.isalpha(): state = "q3"
            else: return False

        elif state == "q3":
            if ch.isalpha(): state = "q3"
            elif ch == ".": state = "q4"
            else: return False

        elif state == "q4":
            if ch.isalpha(): state = "q5"
            else: return False

        elif state == "q5":
            if ch.isalpha(): state = "q5"
            else: return False

    return state == "q5"


#DFA PHONE VALIDATOR
def is_valid_phone(num):
    state = 0

    for ch in num:
        if state == 0:
            if ch.isdigit(): state = 1
            elif ch == "(": state = 2
            else: return False

        elif state == 1:
            if ch.isdigit(): state = 1
            elif ch in "- .": state = 3
            else: return False
        
        elif state == 2:
            if ch.isdigit(): state = 2
            elif ch == ")": state = 1
            else: return False
        
        elif state == 3:
            if ch.isdigit(): state = 4
            else: return False
        
        elif state == 4:
            if ch.isdigit(): state = 4
            elif ch in "- .": state = 5
            else: return False

        elif state == 5:
            if ch.isdigit(): state = 6
            else: return False
        
        elif state == 6:
            if ch.isdigit(): state = 6
            else: return False

    return state in [1,4,6]


#NFA → DFA DEMO
def nfa_accepts(string):
    states = {"q0"}

    for ch in string:
        new_states = set()
        for s in states:
            if s == "q0":
                new_states.add("q0")
                if ch == "a": new_states.add("q1")
            elif s == "q1" and ch == "b":
                new_states.add("q2")
        states = new_states

    return "q2" in states


#Main Program
while True:
    print("\n===================================================")
    print("  INTELLIGENT EXTRACTOR + DFA/NFA AUTOMATA SYSTEM")
    print("===================================================\n")
    print("1. Extract Phone Numbers & Emails (Regex)")
    print("2. Validate Email using DFA")
    print("3. Validate Phone Number using DFA")
    print("4. Test NFA Example (string ending with 'ab')")
    print("5. Exit")

    choice = input("\nEnter option number: ")

    #Extractor 
    if choice == "1":
        method = input("\nEnter '1' for manual input or '2' for file: ")

        if method == "1":
            text = input("\nEnter text: ")

        elif method == "2":
            filename = input("Enter file name: ")
            if not os.path.exists(filename):
                print(" File not found!")
                continue
            text = open(filename,"r",encoding="utf-8").read()

        phones, emails = extract_data(text)

        print("\n Phone Numbers:")
        print(*phones if phones else ["None"], sep="\n→ ")

        print("\n Emails:")
        print(*emails if emails else ["None"], sep="\n→ ")

        save_results(phones, emails)


    #DFA Email
    elif choice == "2":
        email = input("\nEnter email to check: ")
        print("\n Valid Email (DFA Accepted)" if is_valid_email(email)
              else "\n Invalid Email")


    #DFA Phone
    elif choice == "3":
        num = input("\nEnter phone number to check: ")
        print("\n Valid Number (DFA Accepted)" if is_valid_phone(num)
              else "\n Invalid Phone Number")


    #NFA
    elif choice == "4":
        s = input("\nEnter string for NFA test: ")
        print("\n Accepted by NFA (string ends with 'ab')" if nfa_accepts(s)
              else "\n Rejected by NFA")


    #Exit
    elif choice == "5":
        print("\nThanks for using the project!")
        break

    else:
        print("Invalid choice.")

