import datetime

print("[Little-endian / Big-endian]")
n = 0x12345678  # one number

# --- BYTEs ---
le_bytes = n.to_bytes(4, byteorder="little")
be_bytes = n.to_bytes(4, byteorder="big")

print("Number:        ", hex(n))
print("Little-endian:", le_bytes.hex(" "))
print("Big-endian:   ", be_bytes.hex(" "))

# --- BITs (for first Byte) ---
def bits(b):
    return format(b, "08b")

print("\nBits (first byte):")
print("LE first byte:", bits(le_bytes[0]))
print("BE first byte:", bits(be_bytes[0]))

print("="*30)
print(" [Genesis block timestamp]")

hex_ts = "29AB5F49"
print("hex_ts: ", hex_ts)
timestamp = int(hex_ts, 16)
print("int_timestamp: ", timestamp)
dt_utc = datetime.datetime.utcfromtimestamp(timestamp)
#dt_utc = datetime.datetime(timestamp)

print("date_time UTC: ",dt_utc)

"""
[Little-endian / Big-endian]
Number:         0x12345678
Little-endian: 78 56 34 12
Big-endian:    12 34 56 78

Bits (first byte):
LE first byte: 01111000
BE first byte: 00010010
==============================
 [Genesis block timestamp]
hex_ts:  29AB5F49
int_timestamp:  699096905
date_time UTC:  1992-02-26 09:35:05
"""