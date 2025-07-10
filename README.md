# 💼 JobScraper_Upgraded

A Python-based automated web scraping project that collects job/internship listings from [Internshala](https://internshala.com/), analyzes data, and sends email alerts for top picks. It also provides a powerful Streamlit dashboard for visual exploration.

## 🚀 Features

- 🔍 **Web Scraper**: Scrapes Python internships from multiple pages of Internshala.
- 📥 **CSV Export**: Saves listings (title, company, location, stipend, duration) to `internshala_jobs.csv`.
- 📊 **Dashboard**: Visualize top locations and stipend distribution using Streamlit.
- 📧 **Email Alerts**: Sends top internships (based on stipend) to your inbox daily.
- 🔄 **Automated Scheduling**: Ready to run with `cron`, GitHub Actions, or AWS Lambda.
- ☁️ **AWS-ready**: Easily extendable to AWS S3 + Secrets Manager.

## 🛠 Tech Stack

- Python 3
- BeautifulSoup & Requests
- Pandas, Matplotlib, Seaborn
- Streamlit (for dashboard)
- smtplib (for email)
- Cron or `schedule` (for automation)

## 📂 Project Structure

Job_Scrapper_Project/
├── scraper.py
├── alert_emailer.py
├── dashboard.py
├── config.json
├── internshala_jobs.csv
├── requirements.txt
└── README.md

## ✅ How to Run Locally

1. **Clone repo**
2. **Create virtual environment**
3. **Install requirements**
4. **Run scraper, email, and dashboard**

Instructions in detail above...

## 🔐 Security Note

Keep email credentials secret using config or environment variables.

## 🙌 Contribution

Fork ⭐ and PRs are welcome.

## 📄 License

MIT License
