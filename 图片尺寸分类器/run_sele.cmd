@echo off
python select_pic.py
if %errorlevel%==1 (
    echo "请安装相应模块！"
) else (
    echo ""
)
pause