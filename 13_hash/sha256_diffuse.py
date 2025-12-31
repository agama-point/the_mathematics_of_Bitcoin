#!/usr/bin/env python3
import pygame
from datetime import datetime
from pathlib import Path
import hashlib

# ============================================================
# SHA-256 (with trace and final digest)
# ============================================================

class Sha256py:
    ks = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ]

    hs = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
    ]

    M32 = 0xFFFFFFFF

    def __init__(self, m=b""):
        self.h = self.hs[:]
        self.buf = b""
        self.mlen = 0
        self.fin = False
        self.trace = [tuple(self.h)]  # initial IV state (row 0)
        if m:
            self.update(m)

    @staticmethod
    def ror(x, n):
        return ((x >> n) | (x << (32 - n))) & Sha256py.M32

    @staticmethod
    def maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    @staticmethod
    def ch(x, y, z):
        return (x & y) ^ (~x & z)

    @staticmethod
    def pad(msg_len_bytes):
        mdi = msg_len_bytes & 0x3F
        padlen = 55 - mdi if mdi < 56 else 119 - mdi
        return b'\x80' + b'\x00' * padlen + (msg_len_bytes * 8).to_bytes(8, 'big')

    def compress(self, block):
        w = [0] * 64
        w[:16] = [int.from_bytes(block[i:i+4], 'big') for i in range(0, 64, 4)]

        for i in range(16, 64):
            s0 = self.ror(w[i-15], 7) ^ self.ror(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = self.ror(w[i-2], 17) ^ self.ror(w[i-2], 19) ^ (w[i-2] >> 10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & self.M32

        a, b, c, d, e, f, g, h = self.h

        for i in range(64):
            t1 = (h
                  + (self.ror(e, 6) ^ self.ror(e, 11) ^ self.ror(e, 25))
                  + self.ch(e, f, g)
                  + self.ks[i]
                  + w[i]) & self.M32

            t2 = ((self.ror(a, 2) ^ self.ror(a, 13) ^ self.ror(a, 22))
                  + self.maj(a, b, c)) & self.M32

            h = g
            g = f
            f = e
            e = (d + t1) & self.M32
            d = c
            c = b
            b = a
            a = (t1 + t2) & self.M32

            self.trace.append((a, b, c, d, e, f, g, h))

        self.h = [(x + y) & self.M32 for x, y in zip(self.h, (a, b, c, d, e, f, g, h))]

    def update(self, m):
        self.mlen += len(m)
        m = self.buf + m
        for i in range(len(m) // 64):
            self.compress(m[i*64:(i+1)*64])
        self.buf = m[len(m) - (len(m) % 64):]

    def digest(self):
        if not self.fin:
            orig_len = self.mlen
            self.update(self.pad(orig_len))
            self.fin = True
        return b''.join(x.to_bytes(4, 'big') for x in self.h)

    def hexdigest(self):
        return ''.join(f'{b:02x}' for b in self.digest())


# ============================================================
# RENDER + EXPORT PNG
# ============================================================

PIX_X = 3
PIX_Y = 6
WIDTH  = 256 * PIX_X
HEIGHT = 66 * PIX_Y + 100  # 0 = IV, 1-64 = rounds, 65 = digest
TEXT_Y = 66 * PIX_Y + 10

def render_and_save(trace, sha_obj, message, hexdigest):
    pygame.init()
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill((0, 0, 0))

    # --- draw 66 rows ---
    for row in range(66):
        if row == 0:
            regs = trace[0]
            bg_color = (0, 0, 255)  # blue background for IV
            pygame.draw.rect(surface, bg_color, (0, 0, WIDTH, PIX_Y))
            pixel_color = (255, 255, 255)
        elif 1 <= row <= 64:
            regs = trace[row]
            pixel_color = (255, 255, 255)
        else:  # row 65 = final digest
            regs = tuple(sha_obj.h)
            pixel_color = (255, 0, 0)  # red

        xbit = 0
        for reg in regs:
            for b in range(32):
                if reg & (1 << (31 - b)):
                    x = (xbit + b) * PIX_X
                    y = row * PIX_Y
                    pygame.draw.rect(surface, pixel_color, (x, y, PIX_X, PIX_Y))
            xbit += 32

    font = pygame.font.SysFont("monospace", 19, bold=True)
    t1 = font.render(f"SHA-256(\"{message}\")", True, (200, 200, 200))
    t2 = font.render(hexdigest, True, (255, 255, 255))

    surface.blit(t1, (10, TEXT_Y))
    surface.blit(t2, (10, TEXT_Y + 22))

    outdir = Path(__file__).parent / "export_png"
    outdir.mkdir(exist_ok=True)

    ts = datetime.now().strftime("%y%m%d%H%M%S")
    outfile = outdir / f"sha{ts}.png"

    pygame.image.save(surface, outfile)
    pygame.quit()
    print("saved:", outfile)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    
    nonce = 596138
    msg = str(nonce).encode()

    #msg = b"Agama Point 209949850"
    msg = b"Agama Point 209949850 " 

    sha = Sha256py(msg)
    my_hex = sha.hexdigest()
    ref_hex = hashlib.sha256(msg).hexdigest()

    print("[ reference hashlib ]")
    print(ref_hex)
    print("[ this implementation ]")
    print(my_hex)
    assert my_hex == ref_hex, "SHA-256 mismatch!"

    # --- print pre-final hash and IV in hex ---
    pre_a, pre_b, pre_c, pre_d, pre_e, pre_f, pre_g, pre_h = sha.trace[64]
    pre_digest_hex = ''.join(f'{x:08x}' for x in (pre_a, pre_b, pre_c, pre_d,
                                                   pre_e, pre_f, pre_g, pre_h))
    print("\n[ pre-final hash (after 64th round, without IV)]")
    print(pre_digest_hex)

    H_hex = ''.join(f'{x:08x}' for x in sha.hs)
    print("\n[ initial vector H0..H7]")
    print(H_hex)

    final_regs = [(x + y) & 0xFFFFFFFF for x, y in zip(sha.hs,
                                                       (pre_a, pre_b, pre_c, pre_d,
                                                        pre_e, pre_f, pre_g, pre_h))]
    final_hex = ''.join(f'{x:08x}' for x in final_regs)
    print("\n[ final digest = H + pre-final hash]")
    print(final_hex)

    render_and_save(sha.trace, sha, msg.decode(errors="replace"), my_hex)
