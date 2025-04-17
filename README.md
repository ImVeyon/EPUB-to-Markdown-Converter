# EPUB to Markdown Converter

一个简单的EPUB转Markdown工具，可以批量将EPUB电子书转换为Markdown格式。

## 功能特点

- 支持批量转换EPUB文件
- 自动清理HTML锚点链接等无用文字
- 保持原文件名
- 支持中文文件名

## 使用方法

1. 安装依赖：
```bash
pip install ebooklib beautifulsoup4 markdownify
```

2. 将EPUB文件放入`input`目录

3. 运行转换脚本：
```bash
python epub_to_md.py
```

4. 转换后的Markdown文件将保存在`output`目录中

## 目录结构

- `input/`: 存放待转换的EPUB文件
- `output/`: 存放转换后的Markdown文件
- `epub_to_md.py`: 转换脚本 