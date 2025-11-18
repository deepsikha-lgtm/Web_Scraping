# 🌍 Country Data Scraper

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)

[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9%2B-orange)](https://www.crummy.com/software/BeautifulSoup/)

[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-brightgreen)](https://pandas.pydata.org/)

[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A powerful and efficient web scraper that extracts comprehensive country data from [Scrapethissite.com](https://www.scrapethissite.com/pages/simple/) and exports it to multiple formats. Perfect for learning web scraping, data processing, and automation.

## ✨ Features

- 🔍 **Web Scraping**: Extract country data using BeautifulSoup4

- 📊 **Data Processing**: Clean and transform data with pandas

- 💾 **Multiple Formats**: Export to Excel (.xlsx) and CSV

- 📈 **Data Analytics**: Generate insightful statistics

- 🛡️ **Error Handling**: Robust error handling and logging

- ⚡ **Fast & Efficient**: Optimized scraping operations

## 📦 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**

```
git clone https://github.com/yourusername/country-data-scraper.git
cd country-data-scraper
```

Set up virtual environment

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

Install dependencies

```
pip install -r requirements.txt

Run the Scraper

python country_scraper.py
```

🚀 Usage

Basic Usage

Run the main script to scrape all country data:

python country_scraper.py

Expected Output

Scraping country data...
Successfully scraped data for 250 countries

First 5 countries:

        Country                 Capital                 Population      Area
0       Andorra                 Andorra la Vella        84000           468.0
1       United Arab Emirates    Abu Dhabi               4975593         82880.0
2       Afghanistan             Kabul                   29121286        647500.0
3       Antigua and Barbuda     St. John's              86754           443.0
4       Albania                 Tirana                  2986952         28748.0

Data successfully saved to:

- countries_data.xlsx (Excel format)
- countries_data.csv (CSV format)

Basic Statistics:

Total countries: 250

Most populated country: China (1,330,044,544)

Largest country by area: Russia (17,098,242.0 km²)

📁 Project Structure

country-data-scraper/
│
├── country_scraper.py          # Main scraping script
├── requirements.txt            # Project dependencies
├── countries_data.xlsx         # Generated Excel file
├── countries_data.csv          # Generated CSV file
├── LICENSE                     # MIT License
└── README.md                   # Project documentation

🔧 Technical Details

Dependencies

Package	Version	Purpose

beautifulsoup4	≥4.9.0	HTML parsing and data extraction
requests	≥2.25.0	HTTP requests
pandas	≥1.3.0	Data manipulation and export
openpyxl	≥3.0.0	Excel file handling

Data Schema

The scraper extracts the following fields for each country:

Field	        Type	Description
Country	        String	Name of the country
Capital	        String	Capital city name
Population	Integer	Total population count
Area	        Float	Land area in square kilometers

API Reference

get_details(country_one)
Extracts data from a single country HTML element.

Parameters:

country_one (BeautifulSoup element): HTML element containing country data

Returns:

Tuple: (country_name, capital_name, population, area)

get_soup(url)
Fetches and parses webpage content.

Parameters:

url (str): Target URL to scrape

Returns:

BeautifulSoup object or None if request fails

get_countries(url)
Main function to extract all countries data.

Parameters:

url (str): Target URL to scrape

Returns:

List of tuples containing country data

📊 Sample Data

Country	                Capital	                Population	Area (km²)
Andorra         	Andorra la Vella	84,000	        468.0
United Arab Emirates	Abu Dhabi	        4,975,593	82,880.0
Afghanistan	        Kabul	                29,121,286	647,500.0
Antigua and Barbuda	St. John's	        86,754	        443.0
Albania	                Tirana	                2,986,952	28,748.0

🛠️ Development

Setting Up Development Environment
Fork the repository

Create a feature branch

``
git checkout -b feature/your-feature-name
```

Make your changes

Run tests (if available)

Submit a pull request

Code Style

This project follows PEP 8 guidelines. Please ensure your code is properly formatted.

🤝 Contributing

We welcome contributions! Please see our Contributing Guide for details.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

🐛 Troubleshooting

Common Issues

Issue: ModuleNotFoundError

# Solution: Install missing dependencies

```
pip install beautifulsoup4 requests pandas openpyxl
```

Issue: HTTP Connection Errors

Check your internet connection

Verify the target URL is accessible

Ensure no firewall is blocking requests

Issue: Excel Export Fails

# Solution: Install openpyxl explicitly

```
pip install openpyxl
```

Getting Help

📖 Check this README

🐛 Search existing GitHub Issues

💬 Create a new issue with detailed description

⚠️ Legal & Ethical Considerations

This project is for educational purposes only

Always respect website robots.txt and terms of service

The target website is specifically designed for web scraping practice

Implement proper rate limiting in production environments

Be respectful of server resources

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

Scrapethissite.com for providing a safe scraping environment

Beautiful Soup team for excellent HTML parsing

Pandas team for powerful data processing

Contributors and users of this project

📞 Contact

GitHub: /deepsikha-lgtm

Project Link: https://github.com/deepsikha-lgtm/Web_Scraping.git

🚀 Future Enhancements

Add command-line arguments

Support for multiple data sources

Database integration

Web interface

API endpoints

Docker containerization

```
<div align="center">

Built with ❤️ using Python

https://img.shields.io/badge/Made%2520with-Python-1f425f.svg

https://img.shields.io/badge/Powered%2520by-BeautifulSoup4-orange

</div>
```

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

# OS

.DS_Store
Thumbs.db
