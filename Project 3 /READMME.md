


## Overview

This tool is designed to classify email addresses based on predefined rules and databases. It serves as a quick way to assess the legitimacy and safety of an email address. Here's a brief overview of the tool's components:

### Databases

1. **User Database (`User_database.conf`):**
   - Allows users to personalize the tool by adding known, trusted email addresses for personal use.

2. **Trusted Domains (`Trusted-domains.conf`):**
   - Provides a list of domains considered trusted; however, a trusted domain does not guarantee the overall safety of an email.

3. **Disposable Email Blocklist (`Disposable_email_blocklist.conf`):**
   - Contains a blocklist of temporary and blacklisted email domains.
   - Regularly updated to include more domains.So far it has 3600 domains 


### Classification

- The tool classifies email addresses into different categories, including whether the domain is trusted. It's important to note that a trusted domain does not necessarily mean the email is safe.

- The tool also checks if the email domain is blacklisted or disposable, providing additional insights into the potential risks associated with the email.



## 1. Download and Run:

Click on each file you need to download ( Final project code.py, User_database.conf, Trusted-domains.conf, Disposable_email_blocklist.conf).
On each file page, click the "Download" button.


## 2. Run the Final project code:
```bash
 python Final project code.py
```


 ## 3. Input Email Addresses:

Follow the on-screen instructions.
Enter an email address when prompted.
Type 'exit' to stop the program.

## 4. Add Personal Safe Emails:

Open User_database.conf using a text editor.
Add emails that you consider safe for your personal use in the future.


## 5. Understand Trusted Domains:

Open Trusted-domains.conf to see the list of trusted domains.
Note that having a trusted domain doesn't guarantee the safety of an email.

## 6. Use Disposable Email Blocklist:

Disposable_email_blocklist.conf contains a blocklist of temporary and blacklisted emails.
There are more than 3600 domains in this database.

## 7. Output Explanation

The script provides three outputs:

 **Classification:**
   - Indicates whether the email is considered "Legit," "Blacklisted," or another category.

 **Username:**
   - Represents the username part of the email address.

 **Domain:**
   - Represents the domain part of the email address.
  



##Notes: 

The Disposable_email_blocklist.conf database were taken from "https://github.com/disposable-email-domains/disposable-email-domains/blob/master/README.md"




