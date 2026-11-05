import urllib.request
import re

url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Length of text:", len(raw_text))
print(raw_text[:99])

#text = "Hello, world! Is this-- a test?"
#result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
#result = [item.strip() for item in result if item.strip()]
#print(result)

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])
