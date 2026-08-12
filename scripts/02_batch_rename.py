#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_batch_rename.py
按知识库命名规范批量重命名文件。
命名格式：【域代码】-【类型】-【年份】-【序号】-【简短标题】.扩展名
域代码：PV=光伏，ST=储能，PD=配电，BD=商务，CO=企业
"""

import os
import re
from pathlib import Path
from datetime import datetime

DOMAIN_MAP = {
    "光伏": "PV", "pv": "PV",
    "储能": "ST", "ess": "ST", "储能系统": "ST",
    "配电": "PD",
    "商务": "BD", "投标": "BD", "合同": "BD", "报价": "BD",
    "企业": "CO", "制度": "CO", "人事": "CO", "行政": "CO"
}

TYPE_MAP = {
    "案例": "CASE", "case": "CASE",
    "规格书": "SPEC", "参数": "SPEC",
    "标准": "STD", "规范": "STD",
    "模板": "TPL", "template": "TPL",
    "图纸": "DWG", "方案": "SCH",
    "报告": "RPT", "制度": "POL"
}

def clean_title(name: str) -> str:
    """清理标题中的特殊字符，保留中文、英文、数字"""
    name = Path(name).stem
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', '', name)
    return name[:40]  # 限制长度

def suggest_new_name(old_name: str, domain_code: str, doc_type: str, year: str, seq: int) -> str:
    title = clean_title(old_name)
    ext = Path(old_name).suffix.lower()
    return f"{domain_code}-{doc_type}-{year}-{seq:03d}-{title}{ext}"

def batch_rename(folder, domain_code, doc_type, year=None, dry_run=True, start_seq=1):
    """
    dry_run=True 时只打印预览，不实际重命名
    """
    folder = Path(folder)
    if not folder.exists():
        print(f"目录不存在: {folder}")
        return

    year = year or str(datetime.now().year)
    files = sorted([f for f in folder.iterdir() if f.is_file() and not f.name.startswith('.')])
    
    print(f"{'【预览模式】' if dry_run else '【实际执行】'} 共 {len(files)} 个文件")
    print("-" * 60)
    
    seq = start_seq
    for f in files:
        new_name = suggest_new_name(f.name, domain_code, doc_type, year, seq)
        print(f"{f.name}")
        print(f"  → {new_name}")
        if not dry_run:
            target = f.parent / new_name
            if target.exists():
                print(f"  [跳过] 目标已存在")
            else:
                f.rename(target)
                print(f"  [已重命名]")
        seq += 1
        print()

if __name__ == "__main__":
    import sys
    print("=" * 60)
    print("批量重命名工具（知识库命名规范）")
    print("=" * 60)
    if len(sys.argv) < 4:
        print("用法: python 02_batch_rename.py <文件夹> <域代码> <类型代码> [--execute] [--year 2025] [--start 1]")
        print("域代码: PV / ST / PD / BD / CO")
        print("类型代码: CASE / SPEC / STD / TPL / DWG / SCH / RPT / POL")
        print("示例（预览）: python 02_batch_rename.py ./案例 PV CASE")
        print("示例（执行）: python 02_batch_rename.py ./案例 PV CASE --execute")
        sys.exit(1)

    folder = sys.argv[1]
    domain = sys.argv[2].upper()
    dtype = sys.argv[3].upper()
    dry_run = "--execute" not in sys.argv
    year = None
    start = 1
    if "--year" in sys.argv:
        idx = sys.argv.index("--year")
        year = sys.argv[idx + 1]
    if "--start" in sys.argv:
        idx = sys.argv.index("--start")
        start = int(sys.argv[idx + 1])

    batch_rename(folder, domain, dtype, year, dry_run, start)
