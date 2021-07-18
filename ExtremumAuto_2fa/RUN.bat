@ECHO OFF
pip install selenium==4.0.0.a7
pip3 install selenium==4.0.0.a7

START "" %~dp0chromedriver.exe
START %~dp0/public2fa.py

