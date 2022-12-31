import random
import math

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

otp = "So,Hello user this One Time Password is given to you for security purpose. So, " + OTP + " is your OTP. It is " \
                                                                                                "valid for only 2 " \
                                                                                                "minutes."
message = otp
