#!/usr/bin/env python3
"""Reassemble and verify the opaque approved ZIP without extracting it."""
import argparse
import hashlib
import json
import os
from pathlib import Path


def main() -> int:
    base = Path(__file__).resolve().parent
    manifest = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=base / manifest["archive"]["filename"])
    args = parser.parse_args()
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".partial")
    total = 0
    digest = hashlib.sha256()
    try:
        with temporary.open("wb") as assembled:
            for item in manifest["chunks"]:
                chunk_path = base / item["path"]
                data = chunk_path.read_bytes()
                if len(data) != item["size"]:
                    raise ValueError(f"Chunk {item['index']} has the wrong size")
                if hashlib.sha256(data).hexdigest() != item["sha256"]:
                    raise ValueError(f"Chunk {item['index']} failed SHA-256 verification")
                assembled.write(data)
                digest.update(data)
                total += len(data)
        expected = manifest["archive"]
        if total != expected["size"]:
            raise ValueError(f"Archive size mismatch: expected {expected['size']}, got {total}")
        if digest.hexdigest() != expected["sha256"]:
            raise ValueError("Archive SHA-256 mismatch")
        os.replace(temporary, output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    print(f"Verified {total} bytes; SHA-256 {digest.hexdigest()}")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
