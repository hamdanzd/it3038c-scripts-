import re
import requests

def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

# Replace with the actual URLs of your databases
user_database_url = 'https://example.com/User_database.conf'
trusted_domains_url = 'https://example.com/Trusted-domains.conf'
blacklist_url = 'https://example.com/Disposable_email_blocklist.conf'

# Read user database from online URL
user_database = {line: {} for line in fetch_data_from_url(user_database_url)}

# List of trusted email domains
trusted_domains = fetch_data_from_url(trusted_domains_url)

# Define the blacklist outside the classify_email function
blacklist = fetch_data_from_url(blacklist_url)

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

