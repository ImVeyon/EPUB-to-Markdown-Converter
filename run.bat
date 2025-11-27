@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 正在运行 EPUB 转 Markdown 转换程序...
echo.

python epub_to_md.py 2>nul
if errorlevel 1 (
    py epub_to_md.py 2>nul
    if errorlevel 1 (
        echo.
        echo 错误：未找到 Python 解释器
        echo 请确保已安装 Python 并添加到系统 PATH 环境变量中
        echo 或者尝试手动运行: python epub_to_md.py 或 py epub_to_md.py
        echo.
        pause
    )
)

