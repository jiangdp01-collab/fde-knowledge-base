#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从repos_raw.json 中筛出高相关度 FDE 仓库，输出 resources.yaml（人工审校底稿）。"""
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "repos_raw.json")

# 强相关：标题 / 描述里明确出现 FDE 术语
STRONG = re.compile(
    r"forward[- ]deploy|\bfde\b|fde[- _]roadmap|fde[- _]handbook|"
    r"applied ai (engineer|delivery)|ontolog(y|ies).{0,40}palantir|palantir.{0,40}ontolog|"
    r"ai engineer.{0,30}(notebook|roadmap|interview)", re.I)
# 弱相关：仅在次要字段出现，且本身是大而泛的仓库则丢弃
NEG = re.compile(
    r"awesome-(selfhosted|go|nodejs|rust|java|flutter|ios|ml|machine-learning|design|"
    r"mcp-servers|claude-code)|public-apis|free-for-dev|system-design-primer|"
    r"developer-roadmap|project-based-learning|uBlock|pi-hole|etcd-|ultralytics|"
    r"autogen|llama\\b|Summer2027|internships", re.I)


def relevance(r):
    name = r["name"] or ""
    desc = r["description"] or ""
    blob = name + " " + desc
    strong = bool(STRONG.search(blob))
    neg = bool(NEG.search(name))
    if neg:
        return "low"
    if strong:
        # 名称直接含 fde / forward deploy 视为核心
        if re.search(r"fde|forward[- ]deploy", name, re.I):
            return "core"
        return "high"
    return "low"


def main():
    data = json.load(open(RAW, encoding="utf-8"))
    for r in data:
        r["_rel"] = relevance(r)
    keep = [r for r in data if r["_rel"] in ("core", "high")]
    keep.sort(key=lambda r: (r["_rel"] != "core", -r["stargazers_count"]))

    print("total raw=%d  core=%d  high=%d  (low dropped=%d)" % (
        len(data),
        sum(1 for r in data if r["_rel"] == "core"),
        sum(1 for r in data if r["_rel"] == "high"),
        sum(1 for r in data if r["_rel"] == "low")))
    print("-" * 100)
    for r in keep:
        print("%-5s %6d | %-52s | %-10s | %s" % (
            r["_rel"], r["stargazers_count"], r["full_name"],
            (r.get("language") or "-")[:10],
            (r["description"] or "").replace("\n", " ")[:88]))

    out = os.path.join(HERE, "filtered.json")
    json.dump(keep, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nsaved -> %s" % out)


if __name__ == "__main__":
    main()