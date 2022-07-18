import smtplib 
from email.mime.multipart import MIMEMultipart      #object used to send email
from email.mime.text import MIMEText                #body of email
from email.mime.image import MIMEImage              #allows us to add images
from email.mime.application import MIMEApplication  #allows us to add attachments
from email.mime.audio import MIMEAudio              #allows us to add audio files

receivers = ['Christopheremanuel97@gmail.com', 'e.cris.marie@gmail.com']

#build message contents:
msg=MIMEMultipart("related")
msg['Subject'] = "For the Love of My Life"
msg.attach(MIMEText("I will ALWAYS love you more"))

#initialize connection to our email server
smtp = smtplib.SMTP('smtp.gmail.com', port = '587') #port 587 used for all email servers

#Other ports: smtp-mail.outlook.com, smtp.mail.yahoo.com
smtp.ehlo() #send the extended hello to our server
smtp.starttls() #tell server we want to communicate with TLS encryption

smtp.login('Christopheremanuel97@gmail.com', 'S@*^tr0se') #login to our email server

#send our email message 'msg' to receiver
for i in range(len(receivers)):
    smtp.sendmail('Christopheremanuel97@gmail.com',  receivers[i], msg.as_string())

smtp.quit() #close the connection




















#THIS SECTION IS OPTIONAL
#img_data = open('image.jpg', 'rb').read() #read an image binary data
#msg.attach(MIMEImage(img_data))           #add the image to our message object

#read in attachmenst as binary
#with open('report.docx', 'rb') as f:
#    file = MIMEApplication(f.read())      #reads attachment file
#msg.attach(file)                          #add attachment file to message object
