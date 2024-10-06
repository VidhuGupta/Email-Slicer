def email_slicer(email):
    """
    Extracts the local part and domain of an email address.

    Args:
        email (str): The email address to slice.

    Returns:
        tuple: A tuple containing the local part and domain of the email address.
    """
    # Find the index of the '@' character
    at_index = email.find('@')

    # Extract the local part (everything before the '@')
    local_part = email[:at_index]

    # Extract the domain (everything after the '@')
    domain = email[at_index + 1:]

    return local_part, domain

# Example usage
email = str(input())
local_part, domain = email_slicer(email)
print(f"Local part: {local_part}, Domain: {domain}")
