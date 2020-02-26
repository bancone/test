import pyotp

totp_secret = "7vqjehxzpc3heineh6r3iewgcj7yuh4r"

def get_totp(totp_secret):
    totp = pyotp.TOTP(totp_secret)
    return totp.now()

print (get_totp(totp_secret))