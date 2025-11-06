@echo off
cd c:\clases
streamlit run agricultura_rendimiento.py -- server.port =8502 --server.address =0.0.0.0
pause