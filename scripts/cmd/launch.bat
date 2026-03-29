@echo off
start cmd /k uvicorn backend.main_api:app --reload
start http://127.0.0.1:8000/docs
