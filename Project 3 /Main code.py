import re

# Read user database from file
with open('user_database.txt') as user_db_file:
    user_database = {line.strip(): {} for line in user_db_file}

# List of trusted email domains
with open('trusted_domains.txt') as trusted_domains_file:
    trusted_domains = [line.strip() for line in trusted_domains_file]

# Define the blacklist outside the classify_email function
with open('blacklist.txt') as blacklist_file:
    blacklist = [line.strip() for line in blacklist_file]

def split_email(email):
    # Strip leading and trailing spaces from the email
    email = email.strip()

    # Define a regular expression pattern to match an email address
    email_pattern = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'

    # Use re.match to find the parts of the email address
    match = re.match(email_pattern, email)

    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None, None

def classify_email(email, blacklist):
    try:
        username, domain = split_email(email)

        if username and domain:
            # Make the comparison case-insensitive
            lowercase_email = (username + "@" + domain).lower()

            if lowercase_email in user_database:
                return "Legit email", username, domain
            elif domain in blacklist:
                return "Blacklisted email", username, domain
            elif domain in trusted_domains:
                return "Legit but not fully trusted email", username, domain
            else:
                return "Invalid email", username, domain
        else:
            return "Invalid email", None, None
    except Exception as e:
        return "Invalid email", None, None

# Allow user input
while True:
    email = input("Enter an email address (or type 'exit' to quit): ")
    
    if email.lower() == "exit":
        break
    
    classification, username, domain = classify_email(email, blacklist)
    
    if classification == "Legit email":
        print(f"Classification: {classification}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    elif classification == "Blacklisted email":
        print(f"Classification: {classification}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print("The email domain is blacklisted.")
    elif classification == "Legit but not fully trusted email":
        print(f"Classification: {classification}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print("This email is legit but not fully trusted.")
    else:
        print(f"Classification: {classification}")

