# InstagramUrlsScraper

This Scrapy project extracts Instagram URLs related to cafes, restaurants, and bars in USA from Google search results. The data is exported to a CSV file named `InstagramUrls.csv`.

## Features
- **Customizable Query**: Searches Instagram URLs for specific businesses (cafes, restaurants, bars) using advanced Google search queries.
- **Proxy Support**: Utilizes Zyte Smart Proxy for seamless and reliable scraping.
- **Cookie and Header Management**: Handles cookies and headers to bypass restrictions and simulate user interaction.
- **Data Cleaning**: Cleans extracted URLs to remove unnecessary query parameters.
- **Output Format**: Outputs data in CSV format for easy analysis.

## Prerequisites
1. Python 3.8+
2. Scrapy library
3. Zyte Smart Proxy API Key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/PythonicXwarraich/InstagramUrlsScraper.git
    cd InstagramScraper
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update your Zyte Smart Proxy API key in `spider.py`:
    ```python
    'ZYTE_SMARTPROXY_APIKEY': 'your_api_key_here'
    ```

2. Run the spider:
    ```bash
    scrapy crawl spidername
    ```

3. The output file `InstagramUrls.csv` will be saved in the project directory.

## Configuration Details

### Spider Settings
- **Custom Settings**:
    - `FEEDS`: Specifies the output file format and encoding.
    - `DOWNLOADER_MIDDLEWARES`: Enables Zyte Smart Proxy middleware.
    - `CONCURRENT_REQUESTS`: Limits the number of concurrent requests.
    - `DOWNLOAD_DELAY`: Adds a delay between requests to avoid being blocked.
    - `AUTOTHROTTLE_ENABLED`: Dynamically adjusts request rates.

### Google Search Query
The spider generates Google search URLs to find Instagram pages related to cafes, restaurants, and bars, excluding irrelevant links (e.g., reels, explore pages).

### Headers and Cookies
Custom headers and cookies are set to mimic a legitimate browser and bypass potential restrictions.

## File Structure
```
instaUrls/
├── spiders/
│   └── spider.py      # Main spider file
├── requirements.txt   # Dependencies
├── scrapy.cfg         # Scrapy configuration file
└── InstagramUrls.csv # Output file (generated after running the spider)
```

## Limitations
- This project is for educational purposes only. Ensure compliance with website terms of service and data usage policies.
- Data retrieval depends on Google search results and may vary.

## Troubleshooting
1. **Output File Not Generated**:
    - Ensure the spider ran successfully without errors.
    - Check the `FEEDS` settings in `spider.py`.

2. **Connection Errors**:
    - Verify the Zyte Smart Proxy API key is correct.
    - Check your internet connection.

3. **Empty Output**:
    - Verify the search query and ensure there are relevant results.

## Contribution
Feel free to contribute to this project by creating a pull request or opening an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---


