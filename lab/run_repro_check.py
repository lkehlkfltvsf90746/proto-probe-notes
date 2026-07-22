#!/usr/bin/env python3
"""
Loopback-only skeleton for Tinyproxy CVE-2026-54387 reproduction checks.

This script does NOT claim a vulnerability by itself. It:
  - refuses non-loopback hosts;
  - sends a raw byte payload you supply;
  - prints status / bytes received for lab notes.

Usage:
  python run_repro_check.py --payload path/to.http --port 18888
"""

from __future__ import annotations

import argparse
import socket
import sys
from pathlib import Path


def assert_loopback(host: str):
    if host not in ("127.0.0.1", "localhost", "::1"):
        raise SystemExit(
            f"refusing non-loopback host {host!r}; lab only"
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=18888)
    ap.add_argument("--payload", type=Path, required=True,
                    help="raw HTTP bytes file")
    ap.add_argument("--timeout", type=float, default=3.0)
    args = ap.parse_args()
    assert_loopback(args.host)
    data = args.payload.read_bytes()
    if not data.strip():
        print("payload empty or comment-only; fill lab-confirmed bytes first",
              file=sys.stderr)
        return 2
    # skip if file is still the placeholder comment
    if data.lstrip().startswith(b"# Placeholder"):
        print("payload is still the corpus placeholder; not sending",
              file=sys.stderr)
        return 2

    print(f"connecting {args.host}:{args.port} payload_bytes={len(data)}")
    print("NOTE: observation only — compare 1.11.3 vs 1.11.4 yourself")
    with socket.create_connection((args.host, args.port), timeout=args.timeout) as s:
        s.settimeout(args.timeout)
        s.sendall(data)
        chunks = []
        try:
            while True:
                buf = s.recv(4096)
                if not buf:
                    break
                chunks.append(buf)
        except socket.timeout:
            pass
    resp = b"".join(chunks)
    print(f"received_bytes={len(resp)}")
    print(resp[:500].decode("latin1", "replace"))
    print("verdict=OBSERVATION_ONLY fill the report outcome table manually")
    return 0


if __name__ == "__main__":
    sys.exit(main())
