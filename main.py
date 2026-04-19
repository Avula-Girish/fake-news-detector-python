import pandas as pd
import matplotlib.pyplot as plt
fake=pd.read_csv("Fake.csv",nrows=500)
real=pd.read_csv("True.csv",nrows=500)

option=int(input("1. your own data 2.test code (default data)"))
if(option==1):
  data={
          'title':[],
          'text':[],
          'subject':[]
      }
  def inp():
      
      n=int(input("ENTER HOW MANY ROW OF DATA YOU WANT TO ADD: "))
      for i in range(n):
          print("data -",i+1)
          ti=str(input("ENTER TITTLE : ")).lower()
          data['title'].append(ti)
          te=str(input("ENTER TEXT : ")).lower()
          data['text'].append(te)
          sub=str(input("ENTER SUBJECT : ")).lower()
          data['subject'].append(sub)

      


  inp()
  data=pd.DataFrame(data)
else:
    data=pd.concat([fake,real],ignore_index=True)
    

#testing and finding fake or real 
  #len finding
fake["len_title"]=fake["title"].apply(len)
#print("avg fake = ",fake["len_title"].mean())
real["len_title"]=real["title"].apply(len)
avg_real=real["len_title"].mean()

  #text words
   # chatgpt code start (To avoid single character,and remove stop words)
import re

text_real = " ".join(real['text']).lower()
text_fake = " ".join(fake['text']).lower()

list_of_real_words = re.findall(r'\b[a-zA-Z]{3,}\b', text_real)
list_of_fake_words = re.findall(r'\b[a-zA-Z]{3,}\b', text_fake)
stopwords = {'the','and','for','that','with','this','from','are','was','were','have','has'}

list_of_real_words = [w for w in list_of_real_words if w not in stopwords]
list_of_fake_words = [w for w in list_of_fake_words if w not in stopwords]
  # chatgpt code end


set_of_real_words=set(list_of_real_words)

set_of_fake_words=set(list_of_fake_words)
full_fake_set=set_of_fake_words-set_of_real_words
full_fake_dict={x:list_of_fake_words.count(x) for x in full_fake_set }
x=sorted(full_fake_dict.items(),key=lambda x:x[1],reverse=True)
top_n = min(20, len(x))
f_key = [x[i][0] for i in range(top_n)]
f_val = [x[i][1] for i in range(top_n)]




#dict_of_real_words={x:list_of_real_words.count(x) for x in set_of_real_words}

#print(dict_of_real_words)




data["len_title"]=(data["title"]).apply(len)

data["rating_fake"]=0
#data.loc[cond,col]=value
#len check
data.loc[data["len_title"] >= avg_real, "rating_fake"] += 1

#text check
pattern = '|'.join(f_key)

data.loc[data["text"].str.contains(pattern, case=False, na=False), "rating_fake"] += 1

#capital letter checking
data.loc[data["text"].str.isupper()==True,"rating_fake"]+=1

counnt_rating=list(data["rating_fake"])
counnt_rating_set=[0,1,2,3]
all_rating_count=[counnt_rating.count(x) for x in counnt_rating_set]
if(all_rating_count[3]==0):
    all_rating_count.pop(3)
    colorlist=['green','yellow','orange']
    labellist=['SAFE','LOW','MODERATE']
else:
    colorlist=['green','yellow','orange',"RED"]
    labellist=['SAFE','LOW','MODERATE',"HIGH"]
print("Results saved to output_results.csv")
data[["title","text","rating_fake"]].to_csv("output_results.csv", index=False)
  


#MATPLOTLIB WORK
fig, ax=plt.subplots(2,1,figsize=(10,5))

ax[0].barh(f_key,f_val,color="red",edgecolor="black",height=0.6)

ax[0].set_title("TOP WORDS USED IN FAKE NEWS")
ax[0].set_xlabel("no of words")
ax[0].set_ylabel("words")
ax[0].invert_yaxis()
ax[1].set_title("FAKE NEWS RATING")
ax[1].pie(all_rating_count,labels=labellist,colors=colorlist,autopct='%1.1f%%')
ax[0].tick_params(axis='y', labelsize=8)
plt.subplots_adjust(left=0.3)
plt.tight_layout() 
plt.show()

 



