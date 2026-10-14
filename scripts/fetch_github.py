#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取 GitHub 上 FDE（Forward Deployed Engineer）相关仓库，输出结构化 JSON。"""
import json, os, re, time, urllib.request, urllib.parse

QUERIES = [
    "forward deployed engineer",
    "forward-deployed-engineer",
    "forward deployed engineering",
    "fde in:name,description",
    "forward-deployed in:name,description,readme",
    "FDE handbook",
    "applied ai engineer handbook",
    "palantir ontology FDE",
]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repos_raw.json")
HDR = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "fde-resource-hub",
    "X-GitHub-Api-Version": "2022-11-28",
}


def fetch(url):
    req = urllib.request.Request(url, headers=HDR)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            wait = 4 * (attempt + 1)
            print("  retry %s (%s)" % (type(e).__name__, e))
            time.sleep(wait)
    return None


def main():
    seen = {}
    for q in QUERIES:
        print("== query:", q)
        url = ("https://api.github.com/search/repositories?q=%s&sort=stars&order=desc&per_page=100"
               % urllib.parse.quote(q))
        data = fetch(url)
        if not data:
            continue
        for it in data.get("items", []):
            fn = it["full_name"]
            if fn in seen:
                seen[fn]["matched"] = sorted(set(seen[fn]["matched"] + [q]))
                continue
            it["matched"] = [q]
            seen[fn] = it
        print("   total=%s got=%d cum=%d" % (data.get("total_count"), len(data.get("items", [])), len(seen)))
        time.sleep(7)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(list(seen.values()), f, ensure_ascii=False, indent=1)
    print("saved", len(seen), "->", OUT)


if __name__ == "__main__":
    main()