import re

def validate_with_regex(value: str, regex_pattern: str, should_match: bool = True) -> bool:
    
    # Compile the regex pattern
    pattern = re.compile(regex_pattern)
    
    # Check if the value satisfies the regex pattern
    if bool(pattern.match(value)) == should_match:
        return True
    else:
        return False

# Example usage:
phone_number = "1234567890"
phone_number_regex = r"\d{10}"  # Regular expression to match 10 digits
should_match = True

# Validate phone number using the regex pattern
is_valid = validate_with_regex(phone_number, phone_number_regex, should_match)

# Print the validation result
print("Validation Result:", is_valid)
