##importing all required libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import time
import datetime
import selenium
import os

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Run in headless mode (optional)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                         options=chrome_options)

all_teams = [] ## list to store all teams

def save_to_csv(dataframe, team_name=None, is_combined=False):
    """
    Save DataFrame to CSV with appropriate naming convention
    """
    # Create a 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    current_date = datetime.now().strftime("%Y%m%d")
    
    if is_combined:
        filename = f"data/combined_{current_date}_stats.csv"
    else:
        # Clean team name to be filesystem friendly
        clean_team_name = team_name.replace(" ", "_").lower()
        filename = f"data/{clean_team_name}_{current_date}_stats.csv"
    
    dataframe.to_csv(filename, index=False)
    print(f"Saved: {filename}")

try:
    # Navigate to the main page
    driver.get("https://fbref.com/en/comps/9/Premier-League-Stats")
    
    # Wait for the table to load
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "stats_table"))
    )
    
    # Get the page source and create BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find_all('table', class_='stats_table')[0]
    
    # Find and process links
    links = table.find_all('a')
    links = [l.get("href") for l in links]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]
    
    # Process each team
    for team_url in team_urls:
        try:
            team_name = team_url.split("/")[-1].replace("-Stats", "")
            
            # Navigate to team page
            driver.get(team_url)
            
            # Wait for stats table to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "stats_table"))
            )
            
            # Get the page source and create BeautifulSoup object
            soup = BeautifulSoup(driver.page_source, 'lxml')
            stats = soup.find_all('table', class_="stats_table")[0]
            
            # Convert to DataFrame
            team_data = pd.read_html(str(stats))[0]
            team_data["Team"] = team_name
            
            # Save individual team data
            save_to_csv(team_data, team_name=team_name)
            
            # Append to all_teams list for combined data
            all_teams.append(team_data)
            
            # Add delay
            time.sleep(5)
            
        except Exception as e:
            print(f"AAAAAAAAAAAAAA {team_name}: {str(e)}")
            continue

    # Replace the existing combined data saving:
    if all_teams:
        stat_df = pd.concat(all_teams)
        save_to_csv(stat_df, is_combined=True)
        print("Successfully created combined stats file")

except Exception as e:
    print(f"AAAAAAAAAAAAA: {str(e)}")

finally:
    # Close the browser
    driver.quit()

# driver.get("https://fbref.com/en/comps/9/Premier-League-Stats")
# html = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats').text ##getting the html from the website
# soup = BeautifulSoup(html, 'lxml')
# table = soup.find_all('table', class_ = 'stats_table')[0] ##only want the first table, therefore the first index

# links = table.find_all('a') ## finding all links in the table 
# links = [l.get("href") for l in links] ##parsing through links
# links = [l for l in links if '/squads/' in l] ##filtering through links to only get squads

# team_urls = [f"https://fbref.com{l}" for l in links] ## formatting back to links

# for team_url in team_urls: 
#     team_name = team_url.split("/")[-1].replace("-Stats", "") ##isolating the names of the teams
#     data = requests.get(team_url).text
#     soup = BeautifulSoup(data, 'lxml')
#     stats = soup.find_all('table', class_ = "stats_table")[0] ##again, only want the first table

#     if stats and stats.columns: stats.columns = stats.columns.droplevel() ##formatting the stats

#     # Assuming 'team_data' is a BeautifulSoup Tag
#     # Convert it into a DataFrame
#     team_data = pd.read_html(str(stats))[0]
#     team_data["Team"]= team_name
#     all_teams.append(team_data) ## appending the data
#     time.sleep(5) ## making sure we don't get blocked from scraping by delaying each loop by 5 seconds

# stat_df = pd.concat(all_teams) ## concatenating all of the stats
# stat_df.to_csv("stats.csv") ## importing to csv