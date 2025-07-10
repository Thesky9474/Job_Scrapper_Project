import schedule
import time
import os

def job():
    os.system("python scraper.py")
    os.system("python alert_emailer.py")

schedule.every().day.at("08:00").do(job)

print("⏱ Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)