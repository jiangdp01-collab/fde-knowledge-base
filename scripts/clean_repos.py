#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""二次清洗：剔除 Full Disk Encryption / 频域均衡等同缩写噪音，输出干净候选集。"""
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "filtered.json"), encoding="utf-8"))

# 明确属于其它领域的 FDE（与 Forward Deployed Engineer 无关）
NOISE = re.compile(
    r"full[- ]disk[- ]encrypt|android-fde|fde-crack|bruteforce|initramfs|"
    r"filevault|rekey|phase[- ]noise|fractional differential|haar wavelet|"
    r"yubikey|yubico|X11|headless-fde|functional data engineering|"
    r"airflow-tutorial|SC-FDE|OFDM|face|d365cc", re.I)

clean = []
for r in src:
    blob = (r["name"] or "") + " " + (r["description"] or "")
    if NOISE.search(blob):
        continue
    clean.append(r)

# star 门槛：噪声清掉后保留 >=4 星的（不足部分人工补充）
out = [r for r in clean if r["stargazers_count"] >= 4]
low = [r for r in clean if r["stargazers_count"] < 4]

print("clean=%d  (>=4★: %d,  <4★: %d 已折叠待审)" % (len(clean), len(out), len(low)))
print("=" * 108)
for r in out:
    print("%6d | %-54s | %-11s | %s" % (
        r["stargazers_count"], r["full_name"],
        (r.get("language") or "-")[:11],
        (r["description"] or "").replace("\n", " ")[:84]))

json.dump(out, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nsaved -> candidates.json")