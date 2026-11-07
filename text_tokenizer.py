import urllib.request
import re

url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Length of text: ", len(raw_text))
#print("Raw text: ", raw_text[:99])

#text = "Hello, world! Is this-- a test?"
#result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
#result = [item.strip() for item in result if item.strip()]
#print(result)

    #Text tokenizer

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print("Number of tokens: ", len(preprocessed))
#print("Token list: ", preprocessed[:30])

    #Tokens convertion into ids

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Vocab size: ", vocab_size)

vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)
    if i >= 50:
        break

class SimpleTokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab     #writes the vocab dictionary to the str_to_int attribute of the class 
        self.int_to_str = {i:s for s, i in vocab.items()}   #creates a reverse mapping from integer IDs to tokens and assigns 
                                                            #it to the int_to_str attribute of the class
    #converts an input text into a list of integer IDs based on the vocabulary mapping
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int
                        else "<|unk|>" for item in preprocessed]   #replaces any token not found in the vocabulary with the
                                                                    #unknown token "<|unk|>"
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    #converts a list of integer IDs back into a string based on the vocabulary mapping
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?_!"\']|--)\s', r'\1', text)   #removes unnecessary spaces before 
                                                                #punctuation marks and replaces them with 
                                                                #the punctuation mark itself
        return text

    #Adding a context window to the tokenizer

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"]) #unk = unknown token
vocab = {token: integer for integer, token in enumerate(all_tokens)}

print("Vocab size: ", len(vocab.items()))

tokenizer = SimpleTokenizer(vocab)

text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

text = " <|endoftext|> ".join((text1, text2))
print(text)

ids = tokenizer.encode(text)

print("Encoded ids: ", ids)
print("Decoded text: ", tokenizer.decode(ids))