#!venv/bin/python3

from bs4 import BeautifulSoup
import os, sys, datetime, re, requests

folder='output'

class Helper:
	
	@staticmethod
	def fetch(url):
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		now = datetime.datetime.now()
		filename = f'{now.strftime("%Y%m%d-%Hh%M")}.html'
		Helper.save(soup.prettify(), filename)
	
	@staticmethod
	def getfile(filepath):
		with open(filepath, encoding='utf-8') as file:
			return file.readlines()

	def save(content, filename):
		if os.path.exists(folder) == False:
			os.mkdir(folder, mode=0o775)	
		with open(f'{folder}/{filename}', 'w', encoding='utf-8') as file:
			file.write(content)
			print(f'{filename} successfully saved!')
	

class JobParser:
	def __init__(self, results):
		self.results = results
		self.joblist = []

    
	def value_exist(self, value):
		return "undefined" if value is None else value.text


	def parse(self):
		for job in self.results:
			self.joblist.append(
				Job(
					job.find('a', class_="base-card__full-link")['href'],
					self.value_exist(job.find('h3', class_="base-search-card__title")).strip(),
					self.value_exist(job.find('h4', class_="base-search-card__subtitle").a).strip(),
					self.value_exist(job.find('span', class_="job-search-card__location")).strip(),
					self.value_exist(job.find('time', class_="job-search-card__listdate")).strip()
				)	
			)
	

	def links(self):
		return [job.link for job in self.joblist]	
	

class Job:
	def __init__(self, link, title, company, location, posted):
		self.link = link
		self.title = title
		self.company = company
		self.location = location
		self.posted = posted
		self.skills = []
		self.exp = None


def main(url:str):
	try:
		Helper.fetch(url)
	except Exception as e:
		print(e)
	finally:
		print("done")

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("usage : ./main.py <url>")
	else:
		main(sys.argv[1])





