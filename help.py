import pandas as pd
from collections import Counter
import os
import emoji
def fetch_st(selected_user,df,uploaded_file):
    if selected_user!='overall':
        df=df[df['user']==selected_user]
    n_messages=df.shape[0]
    words=[]
    for message in df['message']:
        words.extend(message.split())

    n_media=df[df['message']=='<Media omitted>\n'].shape[0]
    n_size=uploaded_file.seek(0, os.SEEK_END)
    return n_messages,len(words),n_media,n_size
def user_accuracy(df):
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts() / df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percent'})
    return x,df
def comon_words(selected_user,df):
    f=open('stop_hinglish.txt','r')
    stop_words=f.read()
    if selected_user!='overall':
        df=df[df['user']==selected_user]
    tep=df[df['user']!='group_notification']
    tep=df[df['message']!='<Media omitted>\n']
    words=[]
    for message in tep['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    ans_df=pd.DataFrame(Counter(words).most_common(20))
    return ans_df
def emoji_count(selected_user,df):
    if selected_user!='overall':
        df=df[df['user']==selected_user]
    emoj=[]
    for message in df['message']:
        emoj.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoj_df=pd.DataFrame(Counter(emoj).most_common(len(Counter(emoj))))
    return emoj_df
 