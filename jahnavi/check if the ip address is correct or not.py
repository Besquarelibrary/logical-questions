def is_valid_ip_address(ip_address):
    # Split the IP address into its components
    components = ip_address.split(".")

    # Check if the IP address has 4 components
    if len(components) != 4:
        return False

    # Check each component of the IP address
    for component in components:
        # Check if the component is a valid integer
        if not component.isdigit():
            return False

        # Check if the component is within the valid range
        value = int(component)
        if value < 0 or value > 255:
            return False

    # If all checks pass, the IP address is valid
    return True


ip = "192.168.0"
is_valid = is_valid_ip_address(ip)
print(is_valid)
