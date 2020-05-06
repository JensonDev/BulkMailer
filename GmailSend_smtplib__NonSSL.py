import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailData = [
    {
        'to': 'george.henry.1205@outlook.com',
        'subject': 'hi, did you receive it ? Looking for ex-friend',
        'body': "Hello George !"
    },
    {
        'to': 'cui.zheng0105@yahoo.com',
        'subject': 'hi, did you receive it ? ksa !',
        'body': "Are you ksa ?"
    },
    {
        'to': 'dongchengEE_xuejin@hotmail.com',
        'subject': 'hi, did you receive it ? meeting plan',
        'body': "Hello, Cheng \n This is Eric"
    },
    {
        'to': 'ramyi.raydan@outlook.com',
        'subject': 'hi, did you receive it ? hi',
        'body': "from upwork support center, "
    },
    {
        'to': 'nightfurrysimba@yandex.com',
        'subject': 'hi, did you receive it ? subject3',
        'body': "Hello, how are you ? \n\n This is Eric from China."
    },
    {
        'to': 'kevingilliard0205@gmail.com',
        'subject': 'hi, did you receive it ? again',
        'body': "Please don't forget the time we will meet"
    },
    {
        'to': 'nightfurrysimba@outlook.com',
        'subject': 'hi, did you receive it ? Hello there',
        'body': "Dear, freelancer. We're reaching you for the change of connections"
    },
    {
        'to': 'lazarkolarov@gmail.com',
        'subject': 'hi, did you receive it ? news',
        'body': "discount 20% !"
    },
    {
        'to': 'topstar51@outlook.com',
        'subject': 'hi, did you receive it ? uniqlo',
        'body': "Dear client!  Long live, 33! "
    },
    {
        'to': 'prodev52@yandex.com',
        'subject': 'hi, did you receive it ? mailer',
        'body': "Hello, how are you ? \n\n This is Eric from China."
    },
    {
        'to': 'cksuper0928@gmail.com',
        'subject': 'hi, did you receive it ? verification step',
        'body': "hi! great !"
    },
    {
        'to': 'ck.super0928@outlook.com',
        'subject': 'hi, did you receive it ? verify your email',
        'body': "Hello, Cksuper. How're you doing ?"
    }
]


try:
    sender_address = 'eric.burdon0105@gmail.com'
    sender_pass = 'Ihave4membersoffamily'
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
except Exception as e:
    print("Wrong Account(sender) : " + str(e))
    
for emailDatum in emailData:
    try:
        receiver_address = emailDatum['to']
        mail_content = emailDatum['body']

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = emailDatum['subject']
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        text = message.as_string()
        ret = session.sendmail(sender_address, receiver_address, text)
        print(ret)
    except Exception as e:
        print("Mail sending failure! ; " + str(e))

session.quit()
print('All mails sent !')