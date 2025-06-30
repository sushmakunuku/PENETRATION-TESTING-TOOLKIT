from modules import port_scanner, brute_forcer

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Select a module to run (1-2): ").strip()

    if choice == '1':
        target = input("Enter target IP or hostname: ").strip()
        start_port = int(input("Enter start port (default 1): ") or "1")
        end_port = int(input("Enter end port (default 1024): ") or "1024")
        open_ports = port_scanner.scan_ports(target, start_port, end_port)
        if open_ports:
            print(f"Open ports on {target}: {open_ports}")
        else:
            print("No open ports found.")

    elif choice == '2':
        url = input("Enter login URL: ").strip()
        username = input("Enter username: ").strip()
        password_file = input("Enter path to password list file: ").strip()
        try:
            with open(password_file, 'r') as f:
                passwords = [line.strip() for line in f]
        except FileNotFoundError:
            print("Password file not found.")
            return
        brute_forcer.brute_force_login(url, username, passwords)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
