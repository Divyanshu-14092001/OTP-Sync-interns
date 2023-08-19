import random


def generate_otp():
    """Generate a random 6-digit OTP"""
    digits = "0123456789"
    otp = ""
    for _ in range(6):
        otp += random.choice(digits)
    return otp


def send_otp(phone_number, otp):
    """Simulate sending OTP to a phone number (print it)"""
    print(f"OTP sent to {phone_number}: {otp}")


def verify_otp(entered_otp, otp):
    """Verify the entered OTP"""
    return entered_otp == otp


# Simulate a user entering their phone number
phone_number = input("Enter your phone number: ")

# Generate and send OTP
otp = generate_otp()
send_otp(phone_number, otp)

# Simulate a user entering the OTP for verification
entered_otp = input("Enter the OTP you received: ")

# Verify the OTP
if verify_otp(entered_otp, otp):
    print("OTP verification successful!")
else:
    print("OTP verification failed.")
