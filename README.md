# 🌍 Country Data Scraper

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)

[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9%2B-orange)](https://www.crummy.com/software/BeautifulSoup/)

[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-brightgreen)](https://pandas.pydata.org/)

[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A powerful and efficient web scraper that extracts comprehensive country data from **Scrapethissite.com** and exports it to multiple formats.
Perfect for learning **web scraping**, **data analysis**, and **automation**.

---

## ✨ Features

* 🔍 **Web Scraping** using BeautifulSoup4
* 
* 📊 **Data Processing** with pandas
* 
* 💾 **Multi-format Export**: Excel (.xlsx) and CSV
* 
* 📈 **Basic Analytics** included
* 
* 🛡️ **Robust Error Handling** and logging
* 
* ⚡ **Fast & Efficient** scraping loop

---

## 📦 Quick Start

### ✔️ Prerequisites

* Python **3.7+**
* `pip` package manager

### 🔧 Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/country-data-scraper.git
cd country-data-scraper
```

**2. Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# OR
venv\Scripts\activate         # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Run the scraper

```bash
python country_scraper.py
```

### Sample Output

```
Scraping country data...
Successfully scraped data for 250 countries.

First 5 countries:
        Country                 Capital              Population      Area
0       Andorra                 Andorra la Vella     84000           468.0
1       United Arab Emirates    Abu Dhabi            4975593         82880.0
2       Afghanistan             Kabul                29121286        647500.0
3       Antigua and Barbuda     St. John's           86754           443.0
4       Albania                 Tirana               2986952         28748.0

Data successfully saved to:
- countries_data.xlsx
- countries_data.csv

Basic Statistics:
Total countries: 250
Most populated country: China (1,330,044,544)
Largest country by area: Russia (17,098,242.0 km²)
```

---

## 📁 Project Structure

```
country-data-scraper/
│
├── country_scraper.py          # Main scraping script
├── requirements.txt            # Project dependencies
├── countries_data.xlsx         # Exported Excel file
├── countries_data.csv          # Exported CSV file
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

---

## 🔧 Technical Details

### Dependencies

| Package        | Version | Purpose           |
| -------------- | ------- | ----------------- |
| beautifulsoup4 | ≥4.9.0  | HTML parsing      |
| requests       | ≥2.25.0 | HTTP requests     |
| pandas         | ≥1.3.0  | Data manipulation |
| openpyxl       | ≥3.0.0  | Excel file export |

---

## 📑 Data Schema

| Field      | Type    | Description      |
| ---------- | ------- | ---------------- |
| Country    | String  | Country name     |
| Capital    | String  | Capital city     |
| Population | Integer | Total population |
| Area       | Float   | Land area (km²)  |

---

## 🧠 API Reference

### **`get_details(country_one)`**

Extracts the data for a single country.

**Returns:**
`(country_name, capital_name, population, area)`

---

### **`get_soup(url)`**

Fetches and parses the webpage.
**Returns:** BeautifulSoup object or `None` if request fails.

---

### **`get_countries(url)`**

Main scraper function.
**Returns:** List of tuples containing scraped country data.

---

## 📊 Sample Data

| Country           | Capital          | Population | Area (km²) |
| ----------------- | ---------------- | ---------- | ---------- |
| Andorra           | Andorra la Vella | 84,000     | 468.0      |
| UAE               | Abu Dhabi        | 4,975,593  | 82,880.0   |
| Afghanistan       | Kabul            | 29,121,286 | 647,500.0  |
| Antigua & Barbuda | St. John's       | 86,754     | 443.0      |
| Albania           | Tirana           | 2,986,952  | 28,748.0   |

---

## 🛠️ Development

### Setting up for contributing

```bash
git checkout -b feature/your-feature-name
```

Make your changes → Commit → Push → Open Pull Request.

### Code Style

Follows **PEP 8** guidelines.

---

## 🐛 Troubleshooting

### ❌ `ModuleNotFoundError`

Install required packages:

```bash
pip install beautifulsoup4 requests pandas openpyxl
```

### ❌ HTTP connection error

* Check internet connection
* Ensure URL is reachable
* No firewall blocking requests

### ❌ Excel export fails

```bash
pip install openpyxl
```

---

## ⚠️ Legal & Ethical Disclaimer

* This project is for **educational use only**
* Always follow website **robots.txt**
* Use proper **rate-limiting** in production
* Scrapethissite.com is intentionally scraping-friendly

---

## 📄 License

This project is licensed under the MIT License.
See the **LICENSE** file for details.

---

## 🙏 Acknowledgments

* Scrapethissite.com for practice data
* BeautifulSoup4 team
* Pandas developers
* All contributors

---

## 📞 Contact

**GitHub:** (https://github.com/deepsikha-lgtm)

**Project Link:** (https://github.com/deepsikha-lgtm/Web_Scraping.git)

---

## 🚀 Future Enhancements

* Add CLI interface
* Multi-source scraping
* Database integration
* Web UI
* API endpoints
* Docker support

---

<div align="center">

Built with ❤️ using **Python** <br>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

![Powered by BeautifulSoup4](https://img.shields.io/badge/Powered%20by-BeautifulSoup4-orange)

</div>

---
Additional Files for Your Project:

1. requirements.txt

```
beautifulsoup4>=4.9.0
requests>=2.25.0
pandas>=1.3.0
openpyxl>=3.0.0
```

2. LICENSE (MIT License)

MIT License

Copyright (c) 2024 Country Data Scraper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

3. .gitignore

# Virtual environment
venv/
env/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE
.vscode/
.idea/
*.swp
*.swo

# Data files (optional - exclude if you want to track generated data)
*.xlsx
*.csv


