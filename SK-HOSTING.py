#!/usr/bin/env python3
import importlib.util
import os

SO_FILE = "hosting.cpython-312.so"
MODULE_NAME = "ftplib"  

if not os.path.exists(SO_FILE):
    print(f"❌ {SO_FILE} not found!")
    exit(1)

spec = importlib.util.spec_from_file_location(MODULE_NAME, SO_FILE)
fuck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fuck)

# Run main function
if hasattr(fuck, "start_menu"):
    fuck.start_menu()
elif hasattr(fuck, "main_apv"):
    fuck.main_apv()
else:
    print("❌ main() function not found in .so module")