import re

def check_email_address(email):
    # Define the regular expression pattern for a basic email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the search function to check if the email matches the pattern
    match = re.search(pattern, email)
    
    # Return True if a match is found, otherwise return False
    return bool(match)

# Test 10 sample email addresses
sample_emails = [
    "user@example.com",
    "john.doe123@gmail.com",
    "invalid-email",
    "missing@dotcom",
    "user@domain",
    "user@.com",
    "@example.com",
    "user@-domain.com",
    "user@domain-.com",
    "user@domain_with_underscore.com"
]

for email in sample_emails:
    result = check_email_address(email)
    print(f"{email}: {result}")
