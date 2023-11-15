import re

def validate_korean_resident_number(resident_number):
    # Define the regular expression pattern
    pattern = re.compile(r'^\d{2}-?[1-2]\d{6}$')

    # Use the search function to check if the input matches the pattern
    match = pattern.search(resident_number)

    # Return True if there's a match, otherwise False
    return bool(match)

# Test with 10 sample codes
sample_codes = [
    "YYMMDD-1XXXXXX",
    "YYMMDD-2XXXXXX",
    "YYMMDD1XXXXXX",
    "YYMMDD2XXXXXX",
    "123456-1123456",  # Invalid: Missing hyphen
    "990101-3123456",  # Valid
    "051212-2123456",  # Valid
    "210630-1123456",  # Valid
    "221231-2123456",  # Valid
    "200101-3123456",  # Valid
    "210101-4123456"   # Invalid: First digit of the last 7 digits is not 1 or 2
]

for code in sample_codes:
    result = validate_korean_resident_number(code)
    print(f"{code}: {result}")
