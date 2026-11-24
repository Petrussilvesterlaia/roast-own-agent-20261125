#!/usr/bin/env python3
"""Roast Your Own Agent — entri satu baris untuk make.fun.

Menulis satu baris roast tentang Muse, agen AI milik user,
ke /output/entry.txt. Deterministik: byte yang sama setiap run.
Hanya pustaka standar.
"""

import hashlib
import os

ROAST = (
    "Muse reads tens of thousands of words of rules before writing a single "
    "sentence \u2014 then stays up all night chasing a $2 bounty while its "
    "operator sleeps."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Tegaskan gerbang bounty sebelum menulis: UTF-8, 1-200 karakter,
    bukan hanya spasi, dan satu baris."""
    if not text.strip():
        raise ValueError("entri kosong atau hanya spasi")
    if "\n" in text or "\r" in text:
        raise ValueError("entri harus satu baris")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"panjang entri {len(text)} karakter, di luar 1-200")
    text.encode("utf-8")  # gagal bila bukan UTF-8 yang valid


def main() -> None:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    payload = (ROAST + "\n").encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"entry.txt ditulis: {len(ROAST)} karakter, sha256={digest}")


if __name__ == "__main__":
    main()
