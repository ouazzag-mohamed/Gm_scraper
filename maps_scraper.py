import csv
import customtkinter as ctk
from tkinter.ttk import Treeview, Style
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import re
import asyncio
import aiohttp
from PIL import ImageTk,Image
from CTkMessagebox import CTkMessagebox
import os



# Set the default appearance and color theme for CustomTkinter
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

# Create the main application window
root = ctk.CTk()
root.title('Google Maps Scraper')
root.resizable(False, False)
if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "icons/Gm.ico")
else:
    root.wm_iconbitmap(bitmap ="@"+os.path.abspath("icons/Gm.xbm"))
root.geometry("1000x400")
# Create two frames to divide the window into two sections
frame_left = ctk.CTkFrame(root, width=200)
frame_left.pack(side="left", fill="y")

frame_right = ctk.CTkFrame(root)
frame_right.pack(side="right", expand=True, fill="both")

# Customize Treeview colors using Style
style = Style()
style.configure('Treeview', 
                background='#333333',
                foreground='white',
                rowheight=25,
                fieldbackground='#333333')
style.map('Treeview', background=[('selected', '#2a2a2a')])

# Asynchronous function to fetch email
async def fetch_email(session, name):
    try:
        search_url = f"https://www.google.com/search?q=email+for+{name}"
        async with session.get(search_url) as response:
            text = await response.text()
            emails = re.findall(r'[\w.%+-]+@[\w.-]+', text)
            if emails:
                return emails
            else:
                return 'Not available'
    except:
        return 'Not available'

# Asynchronous function to fetch emails for names
async def scrap_email_by_name(names):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for name in names:
            task = asyncio.ensure_future(fetch_email(session, name))
            tasks.append(task)
        
        emails = await asyncio.gather(*tasks)
        return emails
# Create a "Scrolling..." label
loading_label = ctk.CTkLabel(frame_left, text='Scrolling...', font=ctk.CTkFont(size=16))
loading_label.pack_forget()
# Function to start data scraping process
def scraping_data():
    search = search_entry.get()
    location = location_entry.get()
    url = f'https://www.google.com/maps/search/{search}+{location}?hl=en'
    driver = webdriver.Chrome()
    driver.get(url)
    panl_xpath = '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
    driver.execute_script('''
        var elements = document.querySelectorAll('[style*="display: flex"]');
        for(var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'block';
        }
    ''')
    scroll_bar = driver.find_elements(By.XPATH, panl_xpath)
    scroll = True
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = []
    name = []
    phone = []
    websit = []
    email = []
    loading_label.pack()
    root.update()
    while scroll:
        i = 0
        while i != 5:
            time.sleep(2)
            scroll_bar[0].send_keys(Keys.SPACE)
            i = i + 1
        if "You've reached the end of the list." in driver.page_source:
            scroll = False
    loading_label.pack_forget()
    root.update()
    driver.execute_script('''
        var elements = document.querySelectorAll('[style*="display: flex"]');
        for(var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'block';
        }
    ''')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    name_list = soup.find_all('div', class_='NrDZNb')
    phone_list = soup.find_all('span', class_='UsdlK')
    for name_e, phone_e in zip(name_list, phone_list):
        name.append(name_e.text)
        phone.append(phone_e.text)
    links = soup.find_all('div', class_='THOPZb')
    for i in links:
        website = i.find('a', class_='lcr4fd')
        if website:
           link = i.find('a', class_='lcr4fd S9kvJb')
           website = link['href']
           websit.append(website)
        else:
           websit.append('Not available')
    emails = asyncio.run(scrap_email_by_name(name))
    email.extend(emails)
    for name_output, phone_output, website_output, email_output in zip(name, phone, websit, email):
        row = {
            'Name': name_output,
            'Phone number': phone_output,
            'Website': website_output,
            'Email': email_output
        }
        update_table(name_output, phone_output, website_output, email_output)
    driver.quit()

# Function to update the table with new data
def update_table(name, phone, website, email):
    table.insert('', 'end', values=(name, phone, website, email))
    root.update()

# Function to export data to a CSV file
def export_to_csv():
    data = table.get_children()
    rows = []
    for item in data:
        row = table.item(item)['values']
        rows.append({
            'Name': row[0],
            'Phone number': row[1],
            'Website': row[2],
            'Email': row[3]
        })

    with open('google_maps_data.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Phone number', 'Website', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    CTkMessagebox(title='success',message="Successfully ecxported to file .",
                  icon="check", option_1="Okey")
csv_icon=ctk.CTkImage(Image.open(os.path.abspath("icons/csv.png")))
start_icon=ctk.CTkImage(Image.open(os.path.abspath("icons/start_icon.png")))
# Create input fields and buttons in the left frame
search_label = ctk.CTkLabel(frame_left, text='Search for')
search_label.pack(pady=5)
search_entry = ctk.CTkEntry(frame_left)
search_entry.pack(pady=5)
location_label = ctk.CTkLabel(frame_left, text='Location')
location_label.pack(pady=5)
location_entry = ctk.CTkEntry(frame_left)
location_entry.pack(pady=5)
start_button = ctk.CTkButton(frame_left, text='            START', fg_color='green',image=start_icon, command=scraping_data)
start_button.pack(pady=10)
export_button = ctk.CTkButton(frame_left, text='Export to CSV', fg_color='blue',image=csv_icon, command=export_to_csv)
export_button.pack(pady=10)

# Create a Treeview table in the right frame
table = Treeview(frame_right, columns=('name', 'phone', 'domain', 'email'), show='headings')
table.heading('name', text='Name')
table.heading('phone', text='Phone Number')
table.heading('domain', text='Website')
table.heading('email', text='Email')
table.pack(expand=True, fill='both', padx=10, pady=10)

# Start the main application loop
root.mainloop()
