#!/usr/bin/env python3
"""Rewrite the live sections of README.md from the GitHub API.

Sections are delimited by <!--LIVE:NAME:START--> / <!--LIVE:NAME:END--> markers.
Stdlib only; needs GITHUB_TOKEN in the environment.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = "h1n054ur"
# Public repos outside the personal account that belong on the profile.
EXTRA_REPOS = [("bts-io", "uptellis")]
README = Path(__file__).resolve().parent.parent / "README.md"
NOW = datetime.now(timezone.utc)


def graphql(query, variables=None):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={
            "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if body.get("errors"):
        sys.exit(f"GraphQL error: {body['errors']}")
    return body["data"]


def ago(iso):
    days = (NOW - datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    if days < 365:
        return f"{days // 30} mo ago"
    return f"{days // 365} yr ago"


REPO_FIELDS = """
  name nameWithOwner url description pushedAt isFork isArchived
  stargazerCount
  releases(first: 1, orderBy: {field: CREATED_AT, direction: DESC}) {
    nodes { tagName url publishedAt }
  }
"""

QUERY = f"""
query($user: String!) {{
  user(login: $user) {{
    repositories(first: 100, privacy: PUBLIC, ownerAffiliations: OWNER,
                 orderBy: {{field: PUSHED_AT, direction: DESC}}) {{
      totalCount
      nodes {{ {REPO_FIELDS} }}
    }}
    contributionsCollection {{
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar {{ totalContributions }}
    }}
  }}
  {" ".join(f'r{i}: repository(owner: "{o}", name: "{n}") {{ {REPO_FIELDS} }}' for i, (o, n) in enumerate(EXTRA_REPOS))}
}}
"""


def main():
    data = graphql(QUERY, {"user": USER})
    user = data["user"]
    repos = [r for r in user["repositories"]["nodes"] if r["name"] != USER]
    repos += [data[f"r{i}"] for i in range(len(EXTRA_REPOS)) if data.get(f"r{i}")]
    own = [r for r in repos if not r["isFork"] and not r["isArchived"]]

    releases = sorted(
        (
            (r, r["releases"]["nodes"][0])
            for r in own
            if r["releases"]["nodes"]
        ),
        key=lambda x: x[1]["publishedAt"],
        reverse=True,
    )[:5]
    release_lines = [
        f"- [**{r['name']}**]({r['url']}) [`{rel['tagName']}`]({rel['url']}) <sub>{ago(rel['publishedAt'])}</sub>"
        for r, rel in releases
    ] or ["- nothing tagged yet"]

    pushed = sorted(own, key=lambda r: r["pushedAt"], reverse=True)[:5]
    pushed_lines = [
        f"- [**{r['name']}**]({r['url']}) <sub>{ago(r['pushedAt'])}</sub>"
        for r in pushed
    ]

    c = user["contributionsCollection"]
    stars = sum(r["stargazerCount"] for r in repos if not r["isFork"])
    stats_line = (
        f"<sub>Last 12 months: <b>{c['contributionCalendar']['totalContributions']}</b> contributions · "
        f"<b>{c['totalCommitContributions']}</b> commits · "
        f"<b>{c['totalPullRequestContributions']}</b> PRs · "
        f"<b>{c['totalIssueContributions']}</b> issues · "
        f"<b>{user['repositories']['totalCount']}</b> public repos · "
        f"<b>{stars}</b> stars. Refreshed {NOW:%Y-%m-%d}.</sub>"
    )

    sections = {
        "RELEASES": "\n".join(release_lines),
        "PUSHED": "\n".join(pushed_lines),
        "STATS": stats_line,
    }

    text = README.read_text()
    for name, body in sections.items():
        pattern = re.compile(
            rf"(<!--LIVE:{name}:START-->\n).*?(\n<!--LIVE:{name}:END-->)", re.S
        )
        if not pattern.search(text):
            sys.exit(f"marker LIVE:{name} missing from README")
        text = pattern.sub(lambda m: m.group(1) + body + m.group(2), text)
    README.write_text(text)


if __name__ == "__main__":
    main()
