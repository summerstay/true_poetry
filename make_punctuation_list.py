import re
from string import ascii_lowercase
from transformers import GPT2Tokenizer

token_file = open("tokens.txt", "r")
token_file_string = token_file.read()
raw_tokens = token_file_string.split(",")
tokens = []
nums= []
for raw_token in raw_tokens:
    try:
        token, num = raw_token.split('": ')
        tokens.append(token[2:])
        nums.append(int(num))
    except:
        pass
punctuation = {'.'}
for token, num in zip(tokens,nums):
    token=token.replace("\\u0120"," ")
    if re.search('[a-zA-Z]', token):
        pass
    else:
        punctuation.add(num)

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')  
for c in ascii_lowercase:
    token = tokenizer.encode(c)
    punctuation.add(token[0])
    token = tokenizer.encode(c.upper())
    punctuation.add(token[0])
    try:
        token = "." + tokenizer.encode(c)
        punctuation.add(token[0])
    except:
        pass
    try:
        token = "-" + tokenizer.encode(c)
        punctuation.add(token[0])
    except:
        pass
    
    
            
    
        
    
    
        
