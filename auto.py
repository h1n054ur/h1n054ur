#!/usr/bin/env python3
"""
Auto-update a GitHub README.md with today’s date and consecutive-day streak to maintain a daily commit chain.

Requirements:
- Python 3 (no external libraries)
- Environment variable GITHUB_TOKEN set to a GitHub token with “contents: write” scope 
  (GitHub Actions will inject this automatically).

Configuration (edit these before first run):
    OWNER     = "h1n054ur"    # ← replace with your GitHub username or org
    REPO      = "h1n054ur"    # ← replace with your repository name
    BRANCH    = "master"      # ← branch where README.md lives
    FILE_PATH = "README.md"   # ← path to the README file in the repo
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from datetime import date, datetime, timedelta

# ─── CONFIGURATION ───────────────────────────────────────────────────────────────
OWNER     = "h1n054ur"    # ← replace
REPO      = "h1n054ur"    # ← replace
BRANCH    = "master"      # ← or your default branch
FILE_PATH = "README.md"   # ← adjust if your README is elsewhere
# ────────────────────────────────────────────────────────────────────────────────

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.", file=sys.stderr)
    sys.exit(1)

API_BASE = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}"


def get_file_info():
    """
    Fetch existing file metadata and content (base64) from GitHub.
    Returns (sha, decoded_text).
    """
    url = f"{API_BASE}?ref={BRANCH}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("Accept", "application/vnd.github.v3+json")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        print(f"Failed to fetch file info: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

    sha = data.get("sha")
    content_b64 = data.get("content", "")
    # Remove any line breaks before decoding
    content_stripped = "".join(content_b64.splitlines())
    decoded_bytes = base64.b64decode(content_stripped)
    text = decoded_bytes.decode("utf-8", errors="ignore")
    return sha, text


def build_new_content(old_text, today_iso):
    """
    - Parse the existing text to find:
        **Last updated:** `YYYY-MM-DD`
        **Current streak:** `X days`
      If found, update them. If not found, insert them immediately after the title line.

    - Compute new streak:
        * If last_date == yesterday → streak = old_streak + 1
        * If last_date == today      → streak = old_streak (no change)
        * Otherwise                    → streak = 1
    """
    lines = old_text.splitlines()
    old_date_str = None
    old_streak = None

    # 1) Extract old date and old streak from existing lines (if present)
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("**Last updated:**"):
            parts = stripped.split("`")
            if len(parts) >= 2:
                old_date_str = parts[1]  # YYYY-MM-DD
        elif stripped.startswith("**Current streak:**"):
            parts = stripped.split("`")
            if len(parts) >= 2:
                # inside backticks: "X days"
                try:
                    old_streak = int(parts[1].split()[0])
                except ValueError:
                    old_streak = 0

    if old_streak is None:
        old_streak = 0

    # 2) Compute new streak based on date difference
    try:
        old_date_obj = (
            datetime.strptime(old_date_str, "%Y-%m-%d").date()
            if old_date_str
            else None
        )
    except Exception:
        old_date_obj = None

    today = datetime.strptime(today_iso, "%Y-%m-%d").date()
    yesterday = today - timedelta(days=1)

    if old_date_obj == yesterday:
        new_streak = old_streak + 1
    elif old_date_obj == today:
        new_streak = old_streak
    else:
        new_streak = 1

    # 3) Build updated lines array, replacing existing tags if found
    updated_last = False
    updated_streak = False
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("**Last updated:**"):
            indent = line[: len(line) - len(line.lstrip())]
            new_lines.append(f"{indent}**Last updated:** `{today_iso}`")
            updated_last = True
        elif stripped.startswith("**Current streak:**"):
            indent = line[: len(line) - len(line.lstrip())]
            new_lines.append(f"{indent}**Current streak:** `{new_streak} days`")
            updated_streak = True
        else:
            new_lines.append(line)

    # 4) Insert missing lines if not found
    if not updated_last and not updated_streak:
        # Find the title (first line starting with "#")
        insert_at = 0
        for idx, line in enumerate(new_lines):
            if line.strip().startswith("#"):
                insert_at = idx + 1
                break
        # Insert both tags right after the title
        new_lines.insert(insert_at, f"**Last updated:** `{today_iso}`")
        new_lines.insert(insert_at + 1, f"**Current streak:** `{new_streak} days`")

    elif updated_last and not updated_streak:
        # If Last updated was replaced but no streak line existed, insert streak right below it
        for idx, line in enumerate(new_lines):
            if line.strip().startswith("**Last updated:**"):
                indent = line[: len(line) - len(line.lstrip())]
                new_lines.insert(
                    idx + 1, f"{indent}**Current streak:** `{new_streak} days`"
                )
                break

    elif not updated_last and updated_streak:
        # If streak was replaced but no last-updated line existed, insert last-updated above it
        for idx, line in enumerate(new_lines):
            if line.strip().startswith("**Current streak:**"):
                indent = line[: len(line) - len(line.lstrip())]
                new_lines.insert(idx, f"{indent}**Last updated:** `{today_iso}`")
                break

    return "\n".join(new_lines) + "\n"  # ensure trailing newline


def update_file_on_github(new_content_b64, sha, today_iso):
    """
    Send a PUT request to update the file with the new base64 content.
    """
    payload = {
        "message": f"chore: update date to {today_iso}",
        "content": new_content_b64,
        "sha": sha,
        "branch": BRANCH,
    }
    body = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(API_BASE, data=body, method="PUT")
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = json.load(resp)
            commit_sha = resp_data.get("commit", {}).get("sha")
            print(f"Successfully updated README.md at {today_iso} (commit {commit_sha})")
    except urllib.error.HTTPError as e:
        print(f"Failed to update file: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)


def main():
    today_iso = date.today().isoformat()  # e.g. "2025-06-02"
    sha, old_text = get_file_info()
    new_text = build_new_content(old_text, today_iso)

    # Encode updated content to base64
    new_content_bytes = new_text.encode("utf-8")
    new_content_b64 = base64.b64encode(new_content_bytes).decode("utf-8")

    update_file_on_github(new_content_b64, sha, today_iso)


if __name__ == "__main__":
    main()
