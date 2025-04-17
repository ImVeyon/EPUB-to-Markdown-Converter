import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import glob
import re

def clean_text(text):
    # 移除HTML锚点链接
    text = re.sub(r'\(text\d+\.html#[^)]+\)', '', text)
    # 移除连续的空行
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # 移除行首和行尾的空白字符
    text = text.strip()
    return text

def epub_to_md(epub_path, md_path):
    try:
        book = epub.read_epub(epub_path)
        text = ""
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            # 移除所有script和style标签
            for script in soup(["script", "style"]):
                script.decompose()
            text += md(str(soup))

        # 清理文本
        text = clean_text(text)

        with open(md_path, 'w', encoding='utf-8') as md_file:
            md_file.write(text)
        print(f"成功将 {epub_path} 转换为 {md_path}")
    except Exception as e:
        print(f"转换过程中出现错误: {e}")

def process_all_epubs():
    # 创建input和output目录（如果不存在）
    os.makedirs('input', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # 获取input目录下所有的epub文件
    epub_files = glob.glob('input/*.epub')
    
    if not epub_files:
        print("在input目录下没有找到EPUB文件！")
        return
        
    # 处理每个epub文件
    for epub_file in epub_files:
        # 获取文件名（不含扩展名）
        base_name = os.path.splitext(os.path.basename(epub_file))[0]
        # 构建输出文件路径
        md_file = os.path.join('output', f'{base_name}.md')
        # 转换文件
        epub_to_md(epub_file, md_file)

if __name__ == "__main__":
    process_all_epubs()
    