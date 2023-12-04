import re

def read_file(file_path):
    try:
        with open(file_path) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

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

# Read user database from file
user_database = {line: {} for line in read_file('User_database.conf')}

# List of trusted email domains
trusted_domains = read_file('Trusted-domains.conf')

# Define the blacklist outside the classify_email function
blacklist = read_file('Disposable_email_blocklist.conf')

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
        print("This email is fully trusted.")
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
