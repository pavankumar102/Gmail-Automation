import smtplib 
import config

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(config.EMAIL_ADDRESS,config.PASSWORD)
server.sendmail("pavan10283@gmail.com",
                "pk820393@gmail.com",
                "hello, u have done" )
print("Mail sent successfully")
server.quit()