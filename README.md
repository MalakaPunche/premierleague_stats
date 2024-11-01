# Premier League Stats Scraper

A Python script that scrapes Premier League team statistics from fbref.com, providing comprehensive team data in an organized format. This project builds upon [Erik-Cupsa's PL Data Scraping project](https://github.com/Erik-Cupsa/DataScraping/blob/main/PL_Data_Scraping.py) with enhanced features and reliability.

## 📋 Features

- Automated scraping of Premier League team statistics
- Individual CSV files for each team's statistics
- Combined dataset with all team statistics
- Robust error handling and retry mechanisms
- Organized file structure
- Rate limiting to respect server resources

## 🛠️ Requirements

- Python
- Dependencies:
  ```
  beautifulsoup4
  pandas
  requests
  selenium
  webdriver_manager
  ```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pl-stats-scraper.git
   cd pl-stats-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the script:
```bash
python pl_stats.py
```

### Output Structure
```
data/
├── team_stats/
│   ├── Arsenal_2024-03-20_stats.csv
│   ├── Chelsea_2024-03-20_stats.csv
│   └── ...
└── combined_2024-03-20_stats.csv
```

## 🔄 Comparison with Original Implementation

### Original Version
- Basic web scraping using `requests`
- Single output file
- Minimal error handling
- Simple execution flow

### Current Version
- Selenium WebDriver for reliable scraping
- Multiple organized output files
- Comprehensive error handling
- Structured code architecture
- Enhanced data validation

## 🔍 Technical Details

### Data Collection
- Uses Selenium WebDriver with explicit waits
- Implements retry mechanism for failed requests
- Validates data integrity before saving

### Data Storage
- Individual team files: `data/team_stats/{team_name}_{date}_stats.csv`
- Combined dataset: `data/combined_{date}_stats.csv`
- Automatic backup of previous runs

### Error Handling
- Connection error recovery
- Data validation checks
- Detailed error logging
- Graceful failure handling

## ⚠️ Important Notes

- Maintains a 5-second delay between requests
- Requires stable internet connection
- Chrome WebDriver auto-managed by webdriver_manager

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [Erik-Cupsa](https://github.com/Erik-Cupsa) for the original implementation
- [fbref.com](https://fbref.com) for providing the statistics
- Contributors and maintainers of the dependent packages

## 📊 Sample Output

```csv
Team,MP,W,D,L,GF,GA,GD,Pts,xG,xGA,xGD
Arsenal,29,20,4,5,70,24,+46,64,61.5,24.8,+36.7
...
```

## 📫 Contact

For questions or feedback, please [open an issue](https://github.com/MalakaPunche/pl-stats-scraper/issues) on GitHub.