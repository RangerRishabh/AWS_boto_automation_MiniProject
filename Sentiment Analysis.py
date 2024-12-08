import tkinter as tk
import boto3
import boto3.session

root= tk.Tk()
root.geometry("400x240")
root.title("Sentiment Analysis")
textExample=tk.Text(root, height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.Session(profile_name="Titan_user")
    client=aws_mag_con.client(service_name='comprehend',region_name="us-east-1")
    result=textExample.get("1.0","end")
    print(result)
    response = client.detect_sentiment(
    Text=result,
    LanguageCode='en')
    response2 = client.detect_key_phrases(
    Text=result,
    LanguageCode='en')
    print('The key phrases are as follows:')
    for ph in response2['KeyPhrases']:
        print(ph['Text'])
    print('The prominent sentiment is:',response['Sentiment'])
    print('The sentiment score is',response['SentimentScore'])    
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()

root.mainloop()

