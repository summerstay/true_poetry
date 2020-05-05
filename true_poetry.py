import string as str
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F
from random import randint
import copy
import math

# text to meter
def text_to_meter(text, stress_dictionary):
    #calculates the meter of a line of text.
    if len(text)==0:
        return ''
    #capitalize the text
    s = text.upper()
    #remove any punctuation
    for ch in str.punctuation:                                                                                                     
        s = s.replace(ch, "")     
#split the text into individual words
    split_list = list(s.split(" ")) 
#find the stress for individual words
    line_stress=""
    for word in split_list:
        if word in stress_dictionary:
            line_stress = line_stress + stress_dictionary[word]
        else:
            line_stress = line_stress + "*"
    return line_stress

def rhyme_check(text1,text2,rhyme_dictionary):
    #checks whether text1 and text2 rhyme according to a pronunciation dictionary.
    if text2 =="":
        #everything rhymes with the empty text. Needed for starting condition.
        return True
    else:
        text1_words = text1.split(" ")
        last_word1 = text1_words[-1]
        text2_words = text2.split(" ")
        last_word2 = text2_words[-1]
        if last_word1 == last_word2:
            #prevent a word rhyming with itself
            return False
        elif last_word1 in rhyme_dictionary and last_word2 in rhyme_dictionary:
            if rhyme_dictionary[last_word1] == rhyme_dictionary[last_word2]:
                return True
            else:
                return False
        else:
            return False

def compare_meters(meter1,meter2):
    #checks whether meter1 is plausibly matching meter2. meter1 can include unknown ? stresses. 
    matchflag=False
    if len(meter1)<=len(meter2):
        matchflag=True
        for character1,character2 in zip(meter1,meter2):
            if (character1=="`" and character2=="`") or (character1=="~" and character2=="~") or character1=="?":
                pass
            else:
                matchflag=False
    if len(meter1)==0:
        matchflag = True  
    #If you want to force it to end on a strongly stressed word, uncomment this.
    #elif meter1[-1] == '?':
    #    matchflag = False  
    return matchflag
       
def grow_branches(sentence_so_far, probs, input_probability,past, h, prompt_length,rhyme,target_meter):
    #recursive function to find all sentence completions
    global complete_list
    global model
    global stress_dictionary
    global tokenizer
    global rhyme_dictionary
    found = 0
    sorted_probability_list = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    #has_children = False
    text_sentence = tokenizer.decode(sentence_so_far[prompt_length:])
    meter = text_to_meter(text_sentence,stress_dictionary)
    offset = randint(0,3)
    #we only want to search through "good" terms. Since the last term has to rhyme, we loosen the definition of good a little.
    if len(meter)>len(target_meter)-2:
        short_probability_list = sorted_probability_list[0+offset:200+offset]
    else:
        short_probability_list = sorted_probability_list[0+offset:50+offset]
    
    for (this_token,this_probability) in short_probability_list:
        next_probability = this_probability * input_probability
        out_sentence = copy.deepcopy(sentence_so_far)
        sentence_and_probability = (out_sentence, input_probability)
        meter_check = compare_meters(meter,target_meter)
        #this is all tokens that are just punctuation. Ugly, but it prevents endless strings of punctuation.
        foo = set(range(0, 94))
        punctuation = foo.union({438,492,526,553,650,764,834,837,986,1106,2109,2644,3228,3548,3557,4032,4480,4907,6329,7061,7874,9816,10185,11485,12248,12359,16317,17569,22135,22857,25780,34507,43179,44807,44825})
        #print(len(meter), end =" ")
        if len(meter)>=len(target_meter):
            if meter_check:
                if rhyme_check(text_sentence,rhyme,rhyme_dictionary):
                     # the line has completed successfully
                    sentence_and_probability = (out_sentence[prompt_length:], next_probability)
                    complete_list.append(sentence_and_probability)
                    print("***",end=" ") 
                    print(text_sentence)
                    return 1
                print(text_sentence, end = "\t")
                return 2
            else:
                print(text_sentence, end = "\t")
                return 2
        if next_probability < h or (not meter_check) or (sentence_so_far[-1] in punctuation and this_token in punctuation) or (len(sentence_so_far[prompt_length+1:])>30):
            pass
        else:
            next_sentence = sentence_so_far.copy()
            next_sentence.append(this_token)
            (next_probability_list,next_past) = expand_node(next_sentence,past)
            found = grow_branches(next_sentence,next_probability_list, next_probability, next_past, h,prompt_length,rhyme,target_meter)
            if found == 1:
                return 1

def expand_node(sentence, past):
    #finds probabilities for the next token using gpt-2
    global model
    if past == None:
        input_ids = torch.tensor(sentence).unsqueeze(0)
    else:
        input_ids = torch.tensor([sentence[-1]]).unsqueeze(0)
    inputs = {'input_ids': input_ids}    
    with torch.no_grad():
        logits, past = model(**inputs, past=past)
        logits[0][0][50256]=-math.inf
        logits = logits[:, -1, :]  
        probs = F.softmax(logits, dim=-1).tolist()[0]
        return (probs, past)

#create the stress dictionary    
pronounce_file = open("pronounce.txt", "r")
stress_dictionary = {}
for line in pronounce_file:
    line = line.strip("\n")
    parts = line.split(" ")
    syllable_list = parts[2:]
    word = parts[0]
    stresses=""
    if word in ["A","AN","THE","AND","BUT","OR"]:
        stresses="~"
    elif word in ["I","YOU","HE","SHE","IT","WE","THEY","MY","HIS","HER","ITS","OUR","YOUR","THEIR","OURS","YOURS","THEIRS","AM","IS","ARE","WAS","WERE","BEEN","BE","HAVE","HAS","HAD","DO","DOES","DID","WILL","WOULD","SHALL","SHOULD","MAY","MIGHT","MUST","CAN","COULD","OF","WITH","AT","FROM","TO","IN","FOR","ON","BY","LIKE","SINCE","UP","OFF","NEAR","WHICH","AS","EACH","SO","THAT","THATS"]:
        stresses="?"    
    else:
        for syllable in syllable_list:
            if syllable.endswith("1"):
                stresses=stresses+"`"
            elif syllable.endswith("0"):
                stresses=stresses+"~"
            elif syllable.endswith("2"):
                stresses=stresses+"?"
    stress_dictionary[word] = stresses

#create the rhyme dictionary
pronounce_file = open("pronounce.txt", "r")
rhyme_dictionary = {}
reverse_rhyme_dictionary = {}
for line in pronounce_file:
    line = line.strip()
    if line.startswith(';'): continue
    word, phones = line.split("  ")
    syllables = phones.split(" ")
    join_flag = 0
    outstring = ''
    for syllable in syllables:
        if join_flag == 0:
            if "1" in syllable:
                join_flag = 1
                outstring = syllable
        else:
            outstring = outstring + " " + syllable
    rhyme_dictionary[word.lower()] = outstring
    if outstring in reverse_rhyme_dictionary:
        reverse_rhyme_dictionary[outstring].append(word.lower())
    else:
        reverse_rhyme_dictionary[outstring]=[word.lower()]

#load gpt-2 (takes a few seconds)                
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')   
model = GPT2LMHeadModel.from_pretrained("poetry")
print("model loaded")

#from here on must be run every time you want to create a new poem.
leaf_list = []
branch_list = []
complete_list = []
with torch.no_grad():
    raw_prompt = input("starting prompt: ")
    probability_threshhold = 0
    prompt = tokenizer.encode(raw_prompt)
    original_length = len(prompt)
    past = None
    (probs, past) = expand_node(prompt, None) 
    #lines that don't need to rhyme are given empty strings
    rhyme = ""
    target_meter ="~`~`~`~`~`"
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    #the new line to rhyme with is the just created line
    rhyme = tokenizer.decode(complete_list[-1][0])
    #the new prompt is the previous prompt plus the new line, with newlines.
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    #this next line doesn't rhyme with anything.
    rhyme ="" 
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    rhyme = tokenizer.decode(complete_list[-1][0])
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    rhyme ="" 
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    rhyme = tokenizer.decode(complete_list[-1][0])
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    rhyme ="" 
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    rhyme = tokenizer.decode(complete_list[-1][0])
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    (probs, past) = expand_node(prompt, None) 
    grow_branches(prompt,probs,1,past,probability_threshhold,len(prompt),rhyme,target_meter)
    prompt = prompt + [198] + complete_list[-1][0] +[198]
    print(tokenizer.decode(prompt[original_length:]))
        
        
            
    
    
 