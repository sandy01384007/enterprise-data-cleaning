#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05_generate_metadata_template.py
根据文件盘点表或文件夹，生成元数据填写模板Excel，方便批量补全。
"""

from pathlib import Path
import pandas as pd
from datetime import datetime

META_COLUMNS = [
    "原文件名",
    "新文件名（按规范）",
    "标题",
    "一级知识域",
    "二级分类",
    "文件类型",
    "语言",
    "项目地点",
    "容量_MW",
    "权限等级",
    "标签",
    "摘要",
    "责任人",
    "状态",
    "vietnam_specific",
    "备注"
]

DOMAIN_OPTIONS = "光伏数据库 / 储能数据库 / 配电数据库 / 商务数据库 / 企业数据库"
TYPE_OPTIONS = "案例报告 / 规格书 / 标准 / 合同模板 / 制度 / 图纸说明 / 其他"
PERM_OPTIONS = "public / internal / restricted / confidential"
STATUS_OPTIONS = "有效 / 过期 / 草稿"

def generate_from_folder(folder, output="元数据填写模板.xlsx"):
    folder = Path(folder)
    files = [f for f in folder.iterdir() if f.is_file() and not f.name.startswith('.')]
    
    rows = []
    for f in files:
        rows.append({
            "原文件名": f.name,
            "新文件名（按规范）": "",
            "标题": Path(f.name).stem,
            "一级知识域": "",
            "二级分类": "",
            "文件类型": "",
            "语言": "zh-CN",
            "项目地点": "",
            "容量_MW": "",
            "权限等级": "internal",
            "标签": "",
            "摘要": "",
            "责任人": "",
            "状态": "有效",
            "vietnam_specific": "false",
            "备注": ""
        })
    
    df = pd.DataFrame(rows, columns=META_COLUMNS)
    
    # 添加说明sheet
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='元数据填写', index=False)
        
        guide = pd.DataFrame({
            "字段": META_COLUMNS,
            "填写说明": [
                "原始文件名，勿改",
                "按 域代码-类型-年份-序号-标题 格式填写",
                "中文主标题",
                DOMAIN_OPTIONS,
                "参考知识域分类表",
                TYPE_OPTIONS,
                "zh-CN / en / vi / multi",
                "如：越南-平阳省",
                "数值，无则空",
                PERM_OPTIONS,
                "逗号分隔关键词",
                "100字内摘要",
                "内容维护责任人",
                STATUS_OPTIONS,
                "true / false（是否含越南本地要求）",
                "其他说明"
            ]
        })
        guide.to_excel(writer, sheet_name='填写说明', index=False)
    
    print(f"已生成元数据模板：{output}")
    print(f"共 {len(rows)} 条记录，请打开Excel填写后用于入库。")

if __name__ == "__main__":
    import sys
    print("=" * 60)
    print("元数据填写模板生成器")
    print("=" * 60)
    if len(sys.argv) < 2:
        print("用法: python 05_generate_metadata_template.py <文件夹路径> [输出Excel名]")
        sys.exit(1)
    folder = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "元数据填写模板.xlsx"
    generate_from_folder(folder, out)
