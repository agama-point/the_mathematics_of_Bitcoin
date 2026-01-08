import socket
import struct
import time
import hashlib
import random
import subprocess
import platform

# ============================================================
# BASIC NETWORK CHECK
# ============================================================

def ping_test(host="8.8.8.8"):
    print("[*] Checking external network connectivity (ping test)...")

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print("[+] Internet connectivity OK")
            return True
        else:
            print("[-] Ping failed")
            return False

    except Exception as e:
        print("[-] Ping test error:", e)
        return False


# ============================================================
# BITCOIN PROTOCOL CONSTANTS
# ============================================================

MAGIC_MAINNET = b"\xf9\xbe\xb4\xd9"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def sha256d(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def make_message(command, payload):
    command = command.ljust(12, b"\x00")
    length = struct.pack("<I", len(payload))
    checksum = sha256d(payload)[:4]
    return MAGIC_MAINNET + command + length + checksum + payload

def make_version_payload():
    version = 70016
    services = 0
    timestamp = int(time.time())

    addr_recv = struct.pack("<Q", 0) + b"\x00" * 26
    addr_from = struct.pack("<Q", 0) + b"\x00" * 26

    nonce = random.getrandbits(64)
    user_agent = b"/matematika-bitcoinu:0.1/"
    ua_len = len(user_agent)

    start_height = 0
    relay = 0

    return struct.pack(
        "<iQQ26s26sQB",
        version,
        services,
        timestamp,
        addr_recv,
        addr_from,
        nonce,
        ua_len
    ) + user_agent + struct.pack("<i?", start_height, relay)

def read_message(sock):
    header = sock.recv(24)
    if len(header) < 24:
        return None, None

    _, command, length, _ = struct.unpack("<4s12sI4s", header)
    payload = sock.recv(length)

    return command.strip(b"\x00"), payload


# ============================================================
# NODE PROBE
# ============================================================

def probe_node(ip, port=8333, timeout=5):
    status = {
        "T": False,   # TCP connected
        "V": False,   # VERSION built & sent
        "A": False,   # ACTIVE (handshake complete)
        "ua": "?"
    }

    try:
        sock = socket.create_connection((ip, port), timeout=timeout)
        sock.settimeout(timeout)
        status["T"] = True

        payload = make_version_payload()
        sock.sendall(make_message(b"version", payload))
        status["V"] = True

        start = time.time()
        got_version = False
        got_verack = False

        while time.time() - start < timeout:
            command, payload = read_message(sock)
            if not command:
                break

            if command == b"version":
                ua_len = payload[80]
                status["ua"] = payload[81:81 + ua_len].decode(errors="ignore")
                got_version = True

            elif command == b"verack":
                got_verack = True
                break

        sock.close()

        if got_version and got_verack:
            status["A"] = True

    except Exception:
        pass

    return status


# ============================================================
# MAIN
# ============================================================
# delta P: "213.168.187.27"?

if __name__ == "__main__":
    print("=== Bitcoin P2P Node Connectivity Demo ===")

    if not ping_test():
        print("[-] Aborting: no internet connectivity")
        exit(1)

    nodes = [
        "85.244.66.202",
        "86.58.49.166",
        "89.106.27.78",
        "91.134.69.108",
        "93.192.232.94",
        "94.208.144.103",
        "103.47.56.194",
        "213.168.187.127",
        "50.54.173.220",
        "50.126.92.170",
        "184.174.95.183",
        "203.11.72.3"
    ]

    print("Legend: T = TCP connected | V = VERSION sent | A = handshake OK")
    print("\n---------------------------------------------------")

    for ip in nodes:
        result = probe_node(ip)

        T = "T" if result["T"] else "*"
        V = "V" if result["V"] else "*"
        A = "A" if result["A"] else "*"
        ua = result["ua"]

        #print(f"{ip}:8333 | {T}  {V}  {A} | {ua}")
        node_label = f"{ip}:8333"
        print(f"{node_label:<21} | {T}  {V}  {A} | {result['ua']}")

    print("---------------------------------------------------")
    print("Legend: T = TCP connected | V = VERSION sent | A = handshake OK")
"""
=== Bitcoin P2P Node Connectivity Demo ===
[*] Checking external network connectivity (ping test)...
[+] Internet connectivity OK
Legend: T = TCP connected | V = VERSION sent | A = handshake OK

---------------------------------------------------
85.244.66.202:8333    | T  V  A | /Satoshi:29.1.0/
86.58.49.166:8333     | T  V  A | /Satoshi:28.1.0/
89.106.27.78:8333     | T  V  A | /Satoshi:29.2.0/Knots:20251110/
91.134.69.108:8333    | T  V  A | /Satoshi:27.0.0/
93.192.232.94:8333    | T  V  A | /Satoshi:29.0.0/
94.208.144.103:8333   | T  V  A | /Satoshi:30.0.0/
103.47.56.194:8333    | T  V  A | /Satoshi:29.2.0/Knots:20251110/
213.168.187.127:8333  | *  *  * | ?
50.54.173.220:8333    | T  V  A | /Satoshi:30.0.0/
50.126.92.170:8333    | T  V  A | /Satoshi:30.0.0/
184.174.95.183:8333   | T  V  A | /Satoshi:29.2.0/Knots:20251110/
203.11.72.3:8333      | T  V  A | /Satoshi:29.2.0/Knots:20251110/
---------------------------------------------------
Legend: T = TCP connected | V = VERSION sent | A = handshake OK

"""