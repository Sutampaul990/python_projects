import smtplib
from OTP_generate import OTP, message

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

email_id = input("Enter your email: ")
s.login("sutampaul373@gmail.com", "vsufbagznegyajro")
s.sendmail('&&&&&&', email_id, message)

a = input("Enter your OTP : ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
