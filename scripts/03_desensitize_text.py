#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_desensitize_text.py
文本脱敏脚本：自动替换常见敏感信息（身份证、手机号、邮箱、金额、银行卡等）。
注意：基于正则，无法覆盖所有上下文，处理后必须人工复核！
"""

import re
from pathlib import Path

# 脱敏规则（按优先级）
RULES = [
    # 中国身份证（18位）
    (r'\b[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]\b', '【身份证号】'),
    # 手机号
    (r'\b1[3-9]\d{9}\b', '【手机号】'),
    # 邮箱
    (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '【邮箱】'),
    # 银行卡（简单16-19位连续数字，谨慎）
    (r'\b\d{16,19}\b', '【银行卡号】'),
    # 常见金额表达（可按需调整）
    (r'(?:人民币|RMB|￥|¥)\s*[\d,]+(?:\.\d+)?(?:万|亿)?', '【金额】'),
    (r'[\d,]+\.\d{2}\s*元', '【金额】'),
    # 固定电话
    (r'\b0\d{2,3}-?\d{7,8}\b', '【电话】'),
]

def desensitize_text(text: str) -> str:
    result = text
    for pattern, repl in RULES:
        result = re.sub(pattern, repl, result)
    return result

def process_file(input_path, output_path=None):
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.parent / (input_path.stem + "_脱敏" + input_path.suffix)
    else:
        output_path = Path(output_path)

    if input_path.suffix.lower() not in ['.txt', '.md', '.csv']:
        print(f"暂仅支持 .txt / .md / .csv，当前文件: {input_path.suffix}")
        print("请先将Word/PDF转为文本后再处理。")
        return

    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    cleaned = desensitize_text(content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"已处理: {input_path.name}")
    print(f"输出至: {output_path}")
    # 简单统计替换次数
    for pattern, repl in RULES:
        count = len(re.findall(pattern, content))
        if count > 0:
            print(f"  - 替换 {repl}: {count} 处")

def process_folder(folder, suffix="_脱敏"):
    folder = Path(folder)
    for f in folder.glob("*.*"):
        if f.suffix.lower() in ['.txt', '.md', '.csv'] and suffix not in f.stem:
            process_file(f)

if __name__ == "__main__":
    import sys
    print("=" * 60)
    print("文本脱敏工具（身份证 / 手机 / 邮箱 / 金额等）")
    print("警告：必须人工复核结果！脚本无法理解上下文。")
    print("=" * 60)
    if len(sys.argv) < 2:
        print("用法:")
        print("  单文件: python 03_desensitize_text.py <文件路径>")
        print("  文件夹: python 03_desensitize_text.py <文件夹路径> --folder")
        sys.exit(1)

    target = sys.argv[1]
    if "--folder" in sys.argv:
        process_folder(target)
    else:
        process_file(target)
