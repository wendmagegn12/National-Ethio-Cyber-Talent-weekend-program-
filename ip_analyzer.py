def analyze_ip():
    print("=" * 50)
    print("        IP ADDRESS ANALYZER")
    print("=" * 50)
    
    # Get IP address from user
    ip = input("\nEnter an IP address: ")
    
    # Split the IP into its 4 parts (octets)
    parts = ip.split('.')
    
    # --- CHECK IF IP IS VALID ---
    # Check if it has exactly 4 parts
    if len(parts) != 4:
        print("\n[RESULT] Invalid IP: Must have 4 numbers separated by dots")
        return
    
    # Check if each part is a number between 0 and 255
    valid = True
    for part in parts:
        if not part.isdigit():
            valid = False
            break
        num = int(part)
        if num < 0 or num > 255:
            valid = False
            break
    
    if not valid:
        print("\n[RESULT] Invalid IP: Each octet must be a number between 0 and 255")
        return
    
    # If we reach here, IP is valid
    print("\n[RESULT] VALID IP ✓")
    
    # Get the first octet to determine class
    first = int(parts[0])
    
    # --- DETERMINE CLASS ---
    if first >= 1 and first <= 126:
        ip_class = "Class A"
        default_subnet = "/8 (255.0.0.0)"
    elif first == 127:
        ip_class = "Class A (Loopback - Reserved)"
        default_subnet = "/8"
    elif first >= 128 and first <= 191:
        ip_class = "Class B"
        default_subnet = "/16 (255.255.0.0)"
    elif first >= 192 and first <= 223:
        ip_class = "Class C"
        default_subnet = "/24 (255.255.255.0)"
    elif first >= 224 and first <= 239:
        ip_class = "Class D (Multicast)"
        default_subnet = "N/A"
    elif first >= 240 and first <= 255:
        ip_class = "Class E (Experimental)"
        default_subnet = "N/A"
    else:
        ip_class = "Unknown"
        default_subnet = "N/A"
    
    print(f"\nIP Class: {ip_class}")
    print(f"Default Subnet: {default_subnet}")
    
    # --- DETERMINE PUBLIC OR PRIVATE ---
    is_private = False
    
    # Private IP ranges
    if first == 10:
        is_private = True
    elif first == 172 and int(parts[1]) >= 16 and int(parts[1]) <= 31:
        is_private = True
    elif first == 192 and parts[1] == "168":
        is_private = True
    elif first == 127:
        is_private = True  # Loopback is also considered private/local
    
    if is_private:
        print("IP Type: PRIVATE")
    else:
        print("IP Type: PUBLIC")
    
    print("\n" + "=" * 50)

# Run the program
analyze_ip()