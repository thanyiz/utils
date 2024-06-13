#!/usr/bin/env python3

import os
import argparse


def gen_md_file(path, file_basename):
    file_name = os.path.join(path, file_basename + ".md")
    text = ["---\n", f"annotation-target: ./{file_basename}.md\n", "---\n"]
    with open(file_name, "w", encoding="utf-8") as f:
        for line in text:
            f.write(line)


def main():
    # 创建解析器
    parser = argparse.ArgumentParser(
        description="为当前路经与子路径下的所有pdf添加Obsidian Annotator插件要求的md格式文件"
    )
    parser.add_argument("-i", "--input", type=str, default="./", help="输入文件夹路径")
    args = parser.parse_args()
    input_dir = args.input
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".pdf"):
                target_pdf_file_basename = os.path.splitext(file)[0]
                if target_pdf_file_basename + ".md" not in files:
                    gen_md_file(root, target_pdf_file_basename)


if __name__ == "__main__":
    main()
