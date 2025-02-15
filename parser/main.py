#!venv/bin/python3

import os, sys, re, bs4, requests
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Self

class BandcampParser:
	
	def __init__(self, url=None, artist=None, bs4_content=None, file_content=None):
		self.base_url = url
		self.artist = artist
		self.bs4_content = bs4_content
		self.file_content = file_content
		self.folder = 'output'
		self.filename = f'{self.artist}-collection.md'
		self.filepath = f'{self.folder}/{self.filename}'

	def save(self)-> Self:
		if os.path.exists(self.folder) == False:
			os.mkdir(self.folder, mode=0o775)	
		with open(self.filepath, 'w', encoding='utf-8') as file:
			file.write(self.file_content)
			print(f'{self.artist} collection successfully saved!')
			print(self.filepath)


	class Builder:

		def __init__(self, url=None, artist=None, bs4_content=None, file_content=None):
			self.base_url = url
			self.artist = ""
			self.bs4_content = ""
			self.file_content = ""
			self.albums = 'music'

		def collection(self)-> Self:
			r = requests.get(f'{self.base_url}/{self.albums}')
			soup = BeautifulSoup(r.content, "html.parser")
			artist = soup.find(id='band-name-location').find('span', 'title').text
			self.artist = re.sub(r'\s', '-', artist)
			self.bs4_content = soup.find_all('li', class_='music-grid-item')
			return self

		def parse(self)-> Self:
			self.file_content = f'# {self.artist} collection\n'
			for item in self.bs4_content:
				wrap = item.find('a')
				content = wrap.find('p').text.strip()
				title = re.sub(r"\s+", " ", content)
				self.file_content += f'- [ ] [{title}]({self.base_url}/{wrap["href"]})\n'
			return self

		
		def build(self):
			return BandcampParser(self.base_url, self.artist, self.bs4_content, self.file_content)


def main(url:str)-> None:
	try:
		BandcampParser.Builder(url).collection().parse().build().save()
	except Exception as e:
		print(e)
	finally:
		print("done")

if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print("usage: ./main.py <url>")
	else:
		base = sys.argv[1]
		main(base)


