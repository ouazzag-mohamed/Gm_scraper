# Gm_scraper

Google Maps Scraper is a Python-based application that automates the process of extracting business information from Google Maps. The application uses selenium for web scraping, BeautifulSoup for parsing HTML content, and aiohttp for making asynchronous HTTP requests to fetch email addresses.

## Features

- *Dark Mode Interface*: Utilizing CustomTkinter for a modern dark-themed GUI.
- *Asynchronous Email Fetching*: Uses aiohttp for efficient email scraping.
- *CSV Export*: Export the scraped data to a CSV file.

## Requirements

- Python 3.x
- Required Python packages (install using pip):
  - csv
  - customtkinter
  - tkinter
  - bs4 (BeautifulSoup)
  - selenium
  - requests
  - re
  - asyncio
  - aiohttp
  - PIL (Pillow)
  - CTkMessagebox
  - os

## Installation

1.Clone the repository:
   ```sh
   git clone https://github.com/ouazzag-mohamed/Gm_scraper.git
   cd Gm_scraper
   ```

2.Install the required packages:
   * requirements
  ```sh
  pip install -r requirements.txt
  ```

## Usage

1. Run the application:
    ```sh
    python Gm_scraper.py
    ```

2. Enter the search term and location in the provided fields.

3. Click the START button to begin scraping.

4. Once the scraping is complete, you can export the data to a CSV file by clicking the Export to CSV button.

## Code Overview

### Main Components

- *CustomTkinter*: Used for creating the GUI with a dark theme.
- *Selenium*: Automates the browser to navigate and scroll through Google Maps search results.
- *BeautifulSoup*: Parses the HTML content to extract business names, phone numbers, and websites.
- *aiohttp*: Fetches email addresses asynchronously to improve performance.
- *CSV Export*: Saves the scraped data into a CSV file for easy access and analysis.

### Functions

- *scraping_data*: Initiates the scraping process using Selenium and BeautifulSoup.
- *scrap_email_by_name*: Asynchronously fetches emails for a list of business names.
- *update_table*: Updates the GUI table with the scraped data.
- *export_to_csv*: Exports the data to a CSV file.

### GUI Layout

- *Left Frame*: Contains input fields and buttons for user interaction.
  - Search term input
  - Location input
  - START button
  - Export to CSV button
- *Right Frame*: Displays the scraped data in a Treeview table.

## Screenshots

<a href="https://ibb.co/GJsJW69"><img src="https://i.ibb.co/z585XMF/Screenshot-from-2024-07-09-18-00-26.png" alt="Screenshot-from-2024-07-09-18-00-26" border="0"></a>

## Support me

<div align="center">
<a href='https://ko-fi.com/mohamedog' target='_blank'><img height='64' style='border:0px;height:64px;' src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.



## Contact

For any questions or feedback, please contact [me](mailto:ouazzagmohamed@gmail.com).

---

Happy scraping!
