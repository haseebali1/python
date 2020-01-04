def get_formatted_name(first_name, last_name, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first_name} {middle} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
