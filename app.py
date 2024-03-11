import streamlit as st
import pre,help
import os
import matplotlib.pyplot as plt
import emoji
from PIL import Image
#seting the APP NAME AND ICON 
img=Image.open('analyse.png')
st.set_page_config(page_title="ANALYZER",page_icon=img)
st.header("WHATSAPP--DATA--ANALYSER")

st.sidebar.title("<<WHATSAPP CHAT BOOSTER>>")

uploaded_file = st.sidebar.file_uploader("--CHOOSE A FILE--")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)
    #n_size=uploaded_file.seek(0, os.SEEK_END)
    data=bytes_data.decode("utf-8")
    df=pre.prepro(data)
    #st.text(data)

    st.dataframe(df)
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")
    selected_user=st.sidebar.selectbox("||SHOW USERLIST||",user_list)
    if st.sidebar.button("SHOW--ANALYSIS"):
        n_mes,words,n_media,n_size=help.fetch_st(selected_user,df,uploaded_file)
        col1,col2,col3,col4=st.columns(4)#CREATING COLUMNS FOR DIFFRENT DATAS
        with col1:
            st.header("^^MESSAGE COUNT^^")
            st.title(n_mes)
        with col2:
            st.header("^^TOTAL WORDS COUNT^^")
            st.title(words)
        with col3:
            st.header("^^MEDIA^^")
            st.title(n_media)
        with col4:
            st.header("DATA--Bytes")
            st.title(n_size)
        if selected_user=='overall':
        
            st.title("USER ACCURACY")
            x,new_df=help.user_accuracy(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)  # for creating columns  
            with col1:
                ax.bar(x.index,x.values,color='#006A4E')
                plt.xticks(rotation='vertical')
                st.pyplot(fig) 
            with col2:
                st.dataframe(new_df)
    # most common 
        st.title("NUMBER OF TIMES WORDS USED")
        mostcomon_df=help.comon_words(selected_user,df)
        fig,ax=plt.subplots()
        ax.barh(mostcomon_df[0],mostcomon_df[1],color="#9E1909")#barh()--for horizontal baar gragh
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        st.dataframe(mostcomon_df)
    #emoji analyse
        st.title("EMOJI---ANALYSIS")
        emoji_df=help.emoji_count(selected_user,df)
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
            st.pyplot(fig)
    #st.pyplot(fig)
        
    


