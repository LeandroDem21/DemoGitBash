import os
import subprocess
import time
import webbrowser
import requests
import winreg

git_dir = r "C:\Users\CC6\Desktop\docs"
if not os.path.exists(git_dir):
    os.makedirs(git_dir)
    print(f"Created directory: {git_dir}")

repos = [name for name in os.listdir(git.dir)
         if os.path.isdir(os.path.join(git_dir, name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]

if respos:
    print("found the following Github respository")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx . {repo}}")