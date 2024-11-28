# 🏆 Root Me Rank Fetcher
A Python script to retrieve the rankings of multiple users on Root Me and generate an HTML table for easy comparison.

## 📖 Description
This script is designed for friendly competition within a group of people, allowing you to track and compare Root Me rankings. The results are presented in a clean HTML table that automatically opens in your web browser after execution.

## ⚠️ Known Limitations
Request Restrictions: Root Me imposes limits on the number of requests from the same IP. If too many requests are sent in a short period, errors may occur.
Incomplete Data: In case of server-side blocks, some rankings may not be retrieved.

## 🚀 How to Use
Clone the repository and open the dashboard.py file in a text editor.

Add the Root Me usernames you want to track at line 49 in the script as a Python list:
```bash
users = ["user1", "user2", "user3"]
```
Install the required dependencies:
```bash
pip install requests bs4 webbrowser
```
Run the script:
```bash
python dashboard.py
```
Once executed, the HTML table will automatically open in your default web browser.
