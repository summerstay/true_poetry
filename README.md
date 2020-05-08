# true_poetry
Poetry generator by gpt-2 with meter and rhyme constraints. 

required imports:

string, torch, transformers, random, math, pickle

Just run true_poetry.py and type or paste in some text as a prompt and it will generate a sonnet. You should switch to 

model = GPT2LMHeadModel.from_pretrained("gpt2-xl") 

if you want it to automatically download the 11GB neural network, but Gwern's finetumed poetry model does a better job, if you have a copy.
You can modify the meter or rhyme scheme however you want.
There is still some work to be done. It likes short, one-token words too much. Sometimes the rhyming word is grammatically incorrect. The longer the poem goes, the more likely it is to degenerate.

If you have any good ideas on how to avoid passing a ton of variables or using a ton of globals in the recursive function grow_branches, I'd appreciate some help with programming style.
