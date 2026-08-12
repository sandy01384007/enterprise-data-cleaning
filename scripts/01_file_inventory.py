#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_file_inventory.py
扫描指定文件夹，生成文件盘点Excel表，辅助知识库数据清洗第一步。
"""

import os
import hashlib
from datetime import datetime
from pathlib import Path
import pandas as pd

def get_file_hash(filepath, block_size=65536):
    """计算文件MD5，用于去重参考"""
    md5 = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                md5.update(block)
        return md5.hexdigest()
    except Exception:
        return ""

def scan_directory(root_dir, output_excel="文件盘点表.xlsx"):
    root = Path(root_dir)
    if not root.exists():
        print(f"错误：目录不存在 {root_dir}")
        return

    records = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.startswith('.'):
                continue
            full_path = Path(dirpath) / name
            try:
                stat = full_path.stat()
                rel_path = full_path.relative_to(root)
                ext = full_path.suffix.lower()
                size_mb = round(stat.st_size / (1024 * 1024), 2)
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
                file_hash = get_file_hash(full_path) if stat.st_size < 50 * 1024 * 1024 else "文件过大跳过"

                # 简单域猜测
                domain_guess = ""
                name_lower = name.lower()
                if any(k in name_lower for k in ["光伏", "pv", "组件", "逆变器"]):
                    domain_guess = "光伏数据库"
                elif any(k in name_lower for k in ["储能", "ess", "pcs", "bms", "电池"]):
                    domain_guess = "储能数据库"
                elif any(k in name_lower for k in ["配电", "变压器", "开关柜", "短路"]):
                    domain_guess = "配电数据库"
                elif any(k in name_lower for k in ["投标", "标书", "偏离", "报价", "合同"]):
                    domain_guess = "商务数据库"
                elif any(k in name_lower for k in ["制度", "人事", "行政", "培训"]):
                    domain_guess = "企业数据库"

                records.append({
                    "相对路径": str(rel_path),
                    "文件名": name,
                    "扩展名": ext,
                    "大小_MB": size_mb,
                    "修改时间": mtime,
                    "建议知识域": domain_guess,
                    "MD5": file_hash,
                    "备注": ""
                })
            except Exception as e:
                records.append({
                    "相对路径": str(full_path),
                    "文件名": name,
                    "扩展名": "",
                    "大小_MB": 0,
                    "修改时间": "",
                    "建议知识域": "",
                    "MD5": "",
                    "备注": f"读取失败: {e}"
                })

    df = pd.DataFrame(records)
    # 标记可能重复（相同MD5）
    if "MD5" in df.columns:
        dup_mask = df["MD5"].duplicated(keep=False) & (df["MD5"] != "") & (df["MD5"] != "文件过大跳过")
        df.loc[dup_mask, "备注"] = df.loc[dup_mask, "备注"] + " | 可能重复"

    df.to_excel(output_excel, index=False)
    print(f"盘点完成！共 {len(df)} 个文件")
    print(f"结果已保存：{output_excel}")
    print(f"可能重复文件数：{dup_mask.sum() if 'dup_mask' in dir() else 0}")
    return df

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: python 01_file_inventory.py <要扫描的文件夹路径> [输出Excel名]")
        print("示例: python 01_file_inventory.py ./待清洗资料 盘点结果.xlsx")
        sys.exit(1)
    folder = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "文件盘点表.xlsx"
    scan_directory(folder, out)
