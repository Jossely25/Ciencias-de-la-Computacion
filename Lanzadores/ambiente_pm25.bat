@echo off
cd c:\clases
streamlit run ambiente_pm25.py -- server.port =8506 --server.address =0.0.0.0
pause