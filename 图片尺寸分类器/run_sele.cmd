@echo off
python select_pic.py
if %errorlevel%==1 (
    echo "�밲װ��Ӧģ�飡"
) else (
    echo ""
)
pause