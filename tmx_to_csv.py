from bs4 import BeautifulSoup
import pandas as pd


def tmx_reader(tmxfile):
	file = open(tmxfile, 'r', encoding='utf-8')
	soup = BeautifulSoup(file, 'lxml')

	lang1 = soup.findAll("tuv")[0]["xml:lang"]
	lang2 = soup.findAll("tuv")[1]["xml:lang"]

	lang = soup.findAll("seg")  # define the depth of search e.g.: lang = soup.findAll("seg")[:30]

	records = []
	for row1, row2 in zip(lang[0::2], lang[1::2]):
		r1 = row1.text.strip()
		r2 = row2.text.strip()
		records.append((r1, r2))
		
	# print(records)
	df = pd.DataFrame(records, columns=[lang1, lang2])
	df.to_csv('data.csv', index=False, encoding='utf-8', sep='\t')


if __name__ == '__main__':
	tmx_reader("en-fa.tmx")







