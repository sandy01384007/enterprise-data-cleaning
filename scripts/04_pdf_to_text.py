#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_pdf_to_text.py
批量将PDF转为纯文本，便于后续脱敏与向量化。
注意：扫描件PDF需要先OCR，本脚本仅处理文字型PDF。
"""

from pathlib import Path
from pypdf import PdfReader

def pdf_to_text(pdf_path, output_path=None):
    pdf_path = Path(pdf_path)
    if output_path is None:
        output_path = pdf_path.with_suffix('.txt')
    else:
        output_path = Path(output_path)

    try:
        reader = PdfReader(str(pdf_path))
        texts = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            texts.append(f"\n----- 第 {i+1} 页 -----\n{text}")
        full_text = "\n".join(texts)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f"✓ {pdf_path.name} → {output_path.name} （{len(reader.pages)} 页）")
        return True
    except Exception as e:
        print(f"✗ {pdf_path.name} 失败: {e}")
        return False

def batch_convert(folder, output_folder=None):
    folder = Path(folder)
    if output_folder:
        out_dir = Path(output_folder)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = folder / "txt_output"
        out_dir.mkdir(exist_ok=True)

    pdfs = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))
    print(f"发现 {len(pdfs)} 个PDF文件")
    success = 0
    for pdf in pdfs:
        out_file = out_dir / (pdf.stem + ".txt")
        if pdf_to_text(pdf, out_file):
            success += 1
    print(f"完成：成功 {success}/{len(pdfs)}")
    print(f"文本输出目录：{out_dir}")

if __name__ == "__main__":
    import sys
    print("=" * 60)
    print("PDF 批量转文本工具")
    print("=" * 60)
    if len(sys.argv) < 2:
        print("用法:")
        print("  单文件: python 04_pdf_to_text.py <pdf文件>")
        print("  文件夹: python 04_pdf_to_text.py <文件夹> --batch")
        sys.exit(1)

    target = sys.argv[1]
    if "--batch" in sys.argv:
        batch_convert(target)
    else:
        pdf_to_text(target)
