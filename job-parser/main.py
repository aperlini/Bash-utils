#!venv/bin/python3

from bs4 import BeautifulSoup
from simple_term_menu import TerminalMenu
import os, sys, datetime, csv, re, requests
from functools import wraps

OUTPUT_FOLDER='output'
HTML_FILES= f'{OUTPUT_FOLDER}/html'
CSV_FILES= f'{OUTPUT_FOLDER}/csv'

class Helper:

	@staticmethod
	def fetch(url):
		r = requests.get(url)
		if r.status_code == 200:
			soup = BeautifulSoup(r.content, "html.parser")
			Helper.save(soup.prettify(), f'{Helper.get_dt()}.html', HTML_FILES)
		else:
			print(f'{r.status_code} : could not fetch data from {url}')
			sys.exit(1)
	
	
	@staticmethod
	def check_path(func):
		@wraps(func)
		def wrapper_path_exists(*args, **kwargs):
			path = args[0]
			if not os.path.exists(path):
				print(f"{path} does not exist")
				sys.exit(1)
			return func(*args, **kwargs)
		return wrapper_path_exists

	@staticmethod
	@check_path
	def get_file(filepath):
		with open(filepath, encoding='utf-8') as file:
			return file.readlines()
	
	@staticmethod
	@check_path
	def get_content(filepath):
		list_entries = Helper.get_file(filepath)
		return ''.join(str(f) for f in list_entries)

	@staticmethod
	@check_path
	def show_files(path):
		return [f for f in os.listdir(path)]
	
	@staticmethod	
	def get_dt():
		now = datetime.datetime.now()
		return now.strftime("%Y%m%d-%Hh%M")
	
	@staticmethod	
	def make_if_not_exists(path):
		if os.path.exists(path) == False:
			os.makedirs(path, mode=0o775)
			
	def save(content, filename, path):
		Helper.make_if_not_exists(path)
		with open(f'{path}/{filename}', 'w', encoding='utf-8') as file:
			file.write(content)
			print(f'{filename} successfully saved!')
	

class JobParser:
	def __init__(self, file):
		self.file_content = Helper.get_content(file)
		self.joblist = []

	def results(self):
		soup = BeautifulSoup(self.file_content, "html.parser")
		wrap = soup.find('ul', class_="jobs-search__results-list")
		return wrap.find_all('li')
		
    
	def value_exist(self, value):
		return "undefined" if value is None else value.text


	def parse(self):
		
		for job in self.results():
			self.joblist.append(
				Job(
					job.find('a', class_="base-card__full-link")['href'],
					self.value_exist(job.find('h3', class_="base-search-card__title")).strip(),
					self.value_exist(job.find('h4', class_="base-search-card__subtitle").a).strip(),
					self.value_exist(job.find('span', class_="job-search-card__location")).strip(),
					self.value_exist(job.find('time', class_="job-search-card__listdate")).strip()
				)	
			)
		
	def to_csv(self):
		try:
			Helper.make_if_not_exists(CSV_FILES)
			filepath = f'{CSV_FILES}/{Helper.get_dt()}.csv'
			with open(filepath, 'w', newline='') as f:
				writer = csv.writer(f)
				writer.writerow(['posted', 'title', 'company', 'location'])
				for job in self.joblist:
					writer.writerow([job.posted, job.title, job.company, job.location])
			print(f'{filepath} successfully saved!')
		except Exception as e:
			print(f"Error : {e}")
	

class Job:
	def __init__(self, link, title, company, location, posted):
		self.link = link
		self.title = title
		self.company = company
		self.location = location
		self.posted = posted
		self.skills = []
		self.exp = None

class MenuOptions:
	def __init__(self, options=["fetch url data", "parse file"]):
		self.options = options	
		self.menu = TerminalMenu(self.options)
		self.index = None

	
	def selected_index(self):
		return self.menu.show()

if __name__ == '__main__':
	
	menu = MenuOptions()
	index = menu.selected_index()
	
	if index == 0: # fetch online data
		try:
			arg = input("url: ")
			url = str(arg)
			Helper.fetch(url)
		except Exception as e:
			print(e)
	elif index == 1: # parse and save to csv
		files = Helper.show_files(HTML_FILES)
		menu = TerminalMenu(files)
		i = menu.show()
		jobparser = JobParser(f'{HTML_FILES}/{files[i]}')
		jobparser.parse()
		jobparser.to_csv()
	else:
		print(f"{index} : unknown choice")
		exit()

