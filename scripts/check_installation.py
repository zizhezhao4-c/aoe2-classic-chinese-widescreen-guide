"""Original read-only fingerprint inspector; not a patcher or game launcher."""

import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path


REFERENCE = {
    "age2_x1.exe": (2695213, "f6c331dd78f5f8a63fbc08f49963733623482c4bd017bfc6426c6971d139a5d1"),
    "Data/interfac.drs": (54029361, "0b19013c4f68ca1b657a9fbbcc197bcd86c3201185d63f61b3dace3d90ae8091"),
    "age2_x1_myth_1366x768.exe": (2695213, "6949cbfcbc680bb45aa3bb9db56abfa098c49e13c95a6973c3662f2553a00b9a"),
    "Data/13660768.drs": (54055593, "dad1489f838163e75140d4da0d54a332cacf77f86c75194bc0356951010915c9"),
}


def inspect(directory):
    rows = []
    for relative, (expected_size, expected_sha) in REFERENCE.items():
        file = directory / relative
        if not file.is_file():
            rows.append({"file": relative, "present": False})
            continue
        digest = hashlib.sha256()
        with file.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        size = file.stat().st_size
        actual_sha = digest.hexdigest()
        rows.append({"file": relative, "present": True, "size": size,
                     "sha256": actual_sha,
                     "matches_tested_case": size == expected_size and actual_sha == expected_sha})
    codepage = ctypes.WinDLL("kernel32").GetACP() if os.name == "nt" else None
    return {"read_only": True, "current_process_ansi_codepage": codepage,
            "files": rows,
            "limits": "Fingerprint match is not a safety verdict or a universal compatibility guarantee."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-dir", type=Path, required=True)
    args = parser.parse_args()
    directory = args.game_dir.resolve(strict=True)
    if not directory.is_dir():
        parser.error("--game-dir must be a directory")
    print(json.dumps(inspect(directory), ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
