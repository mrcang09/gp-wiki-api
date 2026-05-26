#!/usr/bin/env python3
"""
Sync the GP wiki mirror and the GP API manual mirror for the gp-wiki-api skill.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def run_script(script_name: str, force: bool) -> int:
    command = [sys.executable, str(SCRIPT_DIR / script_name)]
    if force:
        command.append("--force")
    return subprocess.call(command)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-wiki", action="store_true", help="Do not sync the wiki mirror.")
    parser.add_argument("--skip-api-manual", action="store_true", help="Do not sync the API manual mirror.")
    parser.add_argument("--force", action="store_true", help="Force re-fetch of existing local files.")
    args = parser.parse_args()

    exit_code = 0
    if not args.skip_wiki:
        exit_code = max(exit_code, run_script("sync_gp_wiki.py", args.force))
    if not args.skip_api_manual:
        exit_code = max(exit_code, run_script("sync_gp_api_manual.py", args.force))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
