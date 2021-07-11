# from datetime import datetime
# from typing import Mapping
import pandas as pd
import datetime
import smtplib         # for sending email (send email from a printer, scanner or app
import os

os.chdir(r"C:\Users\Rahul\Desktop\python\advanced python\practice")
# os.mkdir("hbd")

# details
Gmail = 'Rahul.parmar@pec.edu'
Paaswd = 'Rahul1138@PTU'


def sendemail(to, sub, msg):
    print(f"email to {to} sent with subject: {sub} and message {msg} ")
    send = smtplib.SMTP('smtp.gmail.com', 587)      # 587 server
    send.starttls()
    send.login(Gmail, Paaswd)
    send.sendmail(Gmail, to, f"{sub}\n\n{msg}")
    send.quit()


if __name__ == "__main__":
    sendemail("rahulparmar1138@gmail.com", "HBD", "test birthday message")
    # exit()
    df = pd.read_excel('birthday.xlsx', engine='openpyxl')
    # old tool : xlrd, working new tool for me: openpyxl
    # print(df)
    
    # today = datetime.datetime.now()
    today = datetime.datetime.now().strftime("%d-%m")   # struct format time
    currentyear = datetime.datetime.now().strftime("%Y")   # struct format time
    # print(today)
    # print(type(today))
    birthdaywishedalready = []
    for indeX, item in df.iterrows():        # iterrows gives you index and item of that row
        # print(indeX+1, item['Birthday'])
        
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)

        if today == bday and currentyear not in str(item['Year']):
            sendemail(item['Email'], "Happiest birthday", item['Dialogue'])
            birthdaywishedalready.append(indeX)

    # print(birthdaywishedalready)

    for i in birthdaywishedalready:
        yr = df.loc[i, 'Year']         # loc(row , column) and iloc (integer based loc)
        df.loc[i, 'Year'] = str(yr) + ',' + str(currentyear)
        # print(df.loc[i, 'Year'])

    # print(df)
    df.to_excel('birthday.xlsx', index=False)
