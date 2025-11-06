@echo off
cd c:\clases
streamlit run economia_inflacion.py -- server.port =8505 --server.address =0.0.0.0
pause