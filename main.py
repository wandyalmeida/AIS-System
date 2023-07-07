import time
import os
import pandas as pd
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the download directory

# desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# ais_dir = os.path.join('C:\Temp', 'AIS')
ais_dir = 'C:\Temp\AIS'

# Create the download directory if it doesn't exist
if not os.path.exists(ais_dir):
    print('Creating folder that not exist')
    os.makedirs(ais_dir)

# Create a subdirectory with a unique name based on the current timestamp
# timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# download_dir = os.path.join(ais_dir, timestamp)
# os.makedirs(download_dir)

# Set Chrome options
options = Options()
options.add_argument('--headless')
options.add_experimental_option('prefs', {
    # "download.default_directory": download_dir,
    "download.default_directory": ais_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

options.headless = True

# Initialize the webDriver
nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the login page
nav.get('https://jmccustoms.bhassociates.ie/Login.aspx')
time.sleep(3)

print('Starting...')

# Enter the email address
email = nav.find_element(By.NAME, "ctl00$ContentPlaceHolder1$newUserID")
time.sleep(1)
email.send_keys("Username")
time.sleep(3)

# Enter the password
password = nav.find_element(By.NAME, "ctl00$ContentPlaceHolder1$newPassword")
# time.sleep(1)
password.send_keys("Password")
time.sleep(1)

# Click the login button
login_button = nav.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_trLoginTable"]/tbody/tr[2]/td/div[1]/input[3]')
login_button.click()
time.sleep(2)


# Click the first link in the side navigation menu
side_nav_link = nav.find_element(By.XPATH, '//*[@id="side_nav"]/ul/li[1]/a[1]')
side_nav_link.click()
time.sleep(3)

print('Set Filter.')
# Click the filter option
filter_option = nav.find_element(By.XPATH, '//*[@id="ctl00_ColumnMainContent"]/div/table/tbody/tr[1]/td[1]/ul/li[2]/a')
filter_option.click()
time.sleep(3)

# Select 7 days of filter
filter_7_days = nav.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dvDates"]/div/table/tbody/tr[2]/td[1]/input')
filter_7_days.click()
time.sleep(3)

print('Search files.')
# Click on search bottom
search = nav.find_element(By.XPATH, '//*[@id="dvInnerFilter"]/table/tbody/tr[9]/td/div[1]/table/tbody/tr/td[3]/input')
nav.execute_script("arguments[0].click();", search)
time.sleep(3)

print('Downloading...')
# Click the download button
download_button = nav.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnToExcel")
download_button.click()
time.sleep(7)
print('Download successful!')

print('Reading excel')
# Read Excel

ais_file = 'C:\Temp\AIS\AEPList.xls'
ais_newFile = 'C:\Temp\AIS\AEPList.xlsx'
print(ais_file)

# Read the file HTML
df = pd.read_html(ais_file)[0]

# Delete the last row
df = df.iloc[:-1]

# Save the df in a file XLSX
df.to_excel(ais_newFile, index=False, header=False)

# workbook = openpyxl.load_workbook(ais_file, read_only=True, keep_vba=False, data_only=True)
df = pd.read_excel(ais_newFile)

#
df['AIS/SAD Number'] = df['AIS/SAD Number'].str.replace(r'\s*\+\s*', '', regex=True)
#
df.to_excel(ais_newFile, index=False)

print('Bye', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')

# When the process finish close the app.
nav.quit()
