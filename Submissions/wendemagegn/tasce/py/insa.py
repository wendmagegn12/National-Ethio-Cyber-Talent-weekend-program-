import tkinter as tk
from tkinter import messagebox
import ipaddress

def check_ip():
    """Validate IP, determine class and default network bits."""
    ip_str = entry_ip.get().strip()
    if not ip_str:
        messagebox.showwarning("Input Error", "Please enter an IP address.")
        return

    try:
        ip_obj = ipaddress.IPv4Address(ip_str)
    except ipaddress.AddressValueError:
        messagebox.showerror("Invalid IP", f"'{ip_str}' is not a valid IPv4 address.")
        return

    ip_int = int(ip_obj)
    first_octet = ip_int >> 24

    # ---------- SPECIAL CASE: first octet 255 ----------
    if first_octet == 255:
        # Custom handling – e.g., treat as a broadcast address
        result = f"IP Address: {ip_str}\n"
        result += "Valid: Yes\n"
        result += "Special: This is a broadcast/reserved address (first octet 255).\n"
        result += "Class: N/A\n"
        result += "Default Network Bits: N/A\n"
        label_result.config(text=result)
        return
    # ------------------------------------------------

    # Original class determination
    if 0 <= first_octet <= 127:
        ip_class = "A"
        bits = 8
    elif 128 <= first_octet <= 191:
        ip_class = "B"
        bits = 16
    elif 192 <= first_octet <= 223:
        ip_class = "C"
        bits = 24
    elif 224 <= first_octet <= 239:
        ip_class = "D (Multicast)"
        bits = "N/A (Class D has no default network bits)"
    elif 240 <= first_octet <= 255:
        ip_class = "E (Experimental)"
        bits = "N/A (Class E is reserved)"
    else:
        ip_class = "Unknown"
        bits = "N/A"

    if first_octet == 127:
        ip_class = "A (Loopback)"

    result = f"IP Address: {ip_str}\n"
    result += f"Valid: Yes\n"
    result += f"Class: {ip_class}\n"
    if isinstance(bits, int):
        # Show default subnet mask as well
        mask = '.'.join(str((0xffffffff << (32 - bits)) >> (24 - i) & 0xff) for i in range(4))
        result += f"Default Network Bits: /{bits} (subnet mask: {mask})\n"
    else:
        result += f"Default Network Bits: {bits}\n"

    label_result.config(text=result)

# GUI setup (same as before)
root = tk.Tk()
root.title("IPv4 Address Checker")
root.geometry("500x350")
root.resizable(False, False)

tk.Label(root, text="Enter an IPv4 address (e.g., 192.168.1.1):", font=("Arial", 12)).pack(pady=10)
entry_ip = tk.Entry(root, width=30, font=("Arial", 12))
entry_ip.pack(pady=5)
tk.Button(root, text="Check IP", command=check_ip, font=("Arial", 12), bg="lightblue").pack(pady=10)
label_result = tk.Label(root, text="", justify=tk.LEFT, font=("Arial", 11), bg="lightyellow", relief=tk.SUNKEN, padx=10, pady=10)
label_result.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()