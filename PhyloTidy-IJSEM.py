import re
import os
import sys

def format_tree_labels(input_file):
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"❌ 错误: 找不到文件 {input_file}")
        return

    print(f"📥 正在读取文件: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        svg_content = f.read()

    # 核心正则表达式解析
    pattern = r"(>\s*)([A-Z][a-z]+\s+[a-z]+)(.*?)\s+([A-Za-z0-9_.-]+)\s*(</text>)"
    
    # 替换逻辑组装
    replacement = r'\1<tspan font-style="italic">\2</tspan>\3<tspan baseline-shift="super" font-size="75%">T</tspan> (\4)\5'

    # 执行替换
    new_svg_content, count = re.subn(pattern, replacement, svg_content)

    # 自动生成输出文件名 (原文件名_Publication_Ready.svg)
    file_dir, file_name = os.path.split(input_file)
    name, ext = os.path.splitext(file_name)
    output_file = os.path.join(file_dir, f"{name}_Publication_Ready{ext}")

    # 保存为新文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_svg_content)

    print(f"🎉 处理完成！共对 {count} 个标签进行了自动化排版。")
    print(f"💾 最终出图文件已保存为: {output_file}\n")

if __name__ == "__main__":
    # sys.argv 捕获拖拽到 exe 上的文件路径
    if len(sys.argv) > 1:
        # 支持同时拖拽多个文件进行批量处理
        for file_path in sys.argv[1:]:
            if file_path.lower().endswith(".svg"):
                format_tree_labels(file_path)
            else:
                print(f"⚠️ 警告: {file_path} 不是 svg 文件，已跳过。")
    else:
        print("💡 使用说明: 请直接将需要处理的 .svg 文件拖拽到本 exe 图标上！")
    
    # 这一行非常关键，防止双击运行或处理结束后窗口瞬间闪退
    input("按回车键 (Enter) 退出程序...")