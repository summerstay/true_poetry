# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:22:59 2020

@author: Doug
"""


aaa=[]
aab=[]
aba=[]
abb=[]
baa=[]
bab=[]
bba=[]
bbb=[]
aa=[]
ab=[]
ba=[]
bb=[]
a=[]
b=[]
for term in stress_dictionary:
    stress = stress_dictionary[term]
    fullword =tokenizer.encode(term.lower(),add_prefix_space=True)
    word = fullword[0]
    if len(stress) > 0:
        if stress[0] == '~' or stress[0] == '?':
            if len(stress)>1:
                if stress[1]=='~' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            aaa.append(word)                            
                        elif stress[2]=='`' or stress[2]=='?':
                            aab.append(word)                           
                    else:
                        aa.append(word)
                        aaa.append(word)
                        aab.append(word)                     
                elif stress[1]=='`' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            aba.append(word)                           
                        elif stress[2]=='`' or stress[2]=='?':
                            abb.append(word)                           
                    else:
                        ab.append(word)
                        abb.append(word)
                        aba.append(word)                     
            else:
                a.append(word)
                aa.append(word)
                ab.append(word)
                aaa.append(word)
                aab.append(word)               
                aba.append(word)
                abb.append(word)
        elif stress[0] == '`' or stress[0] == '?':
            if len(stress)>1:
                if stress[1]=='~' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            baa.append(word)
                        elif stress[2]=='`' or stress[2]=='?':
                            bab.append(word)
                    else:
                        ba.append(word)
                        baa.append(word)
                        bab.append(word)                                           
                elif stress[1]=='`' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            bba.append(word)                                 
                        elif stress[2]=='`' or stress[2]=='?':
                            bbb.append(word)                         
                    else:
                        bb.append(word)
                        bba.append(word)
                        bbb.append(word)    
            else:
                b.append(word)
                ba.append(word)
                bb.append(word)
                baa.append(word)
                bab.append(word)               
                bba.append(word)
                bbb.append(word)          

for term in stress_dictionary:
    stress = stress_dictionary[term]
    fullword =tokenizer.encode(term.title(),add_prefix_space=True)
    word = fullword[0]
    if len(stress) > 0:
        if stress[0] == '~' or stress[0] == '?':
            if len(stress)>1:
                if stress[1]=='~' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            aaa.append(word)                            
                        elif stress[2]=='`' or stress[2]=='?':
                            aab.append(word)                           
                    else:
                        aa.append(word)
                        aaa.append(word)
                        aab.append(word)                     
                elif stress[1]=='`' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            aba.append(word)                           
                        elif stress[2]=='`' or stress[2]=='?':
                            abb.append(word)                           
                    else:
                        ab.append(word)
                        abb.append(word)
                        aba.append(word)                     
            else:
                a.append(word)
                aa.append(word)
                ab.append(word)
                aaa.append(word)
                aab.append(word)               
                aba.append(word)
                abb.append(word)
        elif stress[0] == '`' or stress[0] == '?':
            if len(stress)>1:
                if stress[1]=='~' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            baa.append(word)
                        elif stress[2]=='`' or stress[2]=='?':
                            bab.append(word)
                    else:
                        ba.append(word)
                        baa.append(word)
                        bab.append(word)                                           
                elif stress[1]=='`' or stress[1]=='?':
                    if len(stress)>2:
                        if stress[2]=='~' or stress[2]=='?':
                            bba.append(word)                                 
                        elif stress[2]=='`' or stress[2]=='?':
                            bbb.append(word)                         
                    else:
                        bb.append(word)
                        bba.append(word)
                        bbb.append(word)    
            else:
                b.append(word)
                ba.append(word)
                bb.append(word)
                baa.append(word)
                bab.append(word)               
                bba.append(word)
                bbb.append(word)          
                
                
a=list(set(a))

aa=list(set(aa))

aaa=list(set(aaa))

ab=list(set(ab))

ba=list(set(ba))

bb=list(set(bb))

b=list(set(b))

aab=list(set(aab))

aba=list(set(aba))

abb=list(set(abb))

baa=list(set(baa))

bab=list(set(bab))

bba=list(set(bba))

bbb=list(set(bbb))

stress_tokens={}

stress_tokens['~']=a

stress_tokens['`']=b

stress_tokens['~~']=aa

stress_tokens['~`']=ab

stress_tokens['`~']=ba

stress_tokens['``']=bb

stress_tokens['~~~']=aaa

stress_tokens['~~`']=aab

stress_tokens['~`~']=aba

stress_tokens['~``']=abb

stress_tokens['`~~']=baa

stress_tokens['`~`']=bab

stress_tokens['``~']=bba

stress_tokens['```']=bbb

stress_tokens['?']=set(a).union(set(b))


stress_tokens['~?']=set(ab).union(set(aa))

stress_tokens['`?']=set(bb).union(set(ba))

stress_tokens['??']=set(bb).union(set(ba)).union(set(ab)).union(set(aa))


stress_tokens['~~?']=set(aab).union(set(aaa))

stress_tokens['~`?']=set(abb).union(set(aba))

stress_tokens['~??']=set(abb).union(set(aba)).union(set(aab)).union(set(aaa))


stress_tokens['`~?']=set(bab).union(set(baa))

stress_tokens['``?']=set(bbb).union(set(bba))

stress_tokens['`??']=set(bbb).union(set(bba)).union(set(bab)).union(set(baa))


stress_tokens['?~?']=set(bab).union(set(baa)).union(set(aab)).union(set(aaa))

stress_tokens['?`?']=set(bbb).union(set(bba)).union(set(abb)).union(set(aba))

stress_tokens['???']=set(bbb).union(set(bba)).union(set(bab)).union(set(baa)).union(set(abb)).union(set(aba)).union(set(aab)).union(set(aaa))

stress_tokens['??~']=set(bba).union(set(baa)).union(set(aba)).union(set(aaa))

stress_tokens['??`']=set(bbb).union(set(bab)).union(set(abb)).union(set(aab))

pickle.dump( stress_tokens, open( "stress_tokens.p", "wb" ) )

