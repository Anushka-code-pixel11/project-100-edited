class Atm(object):
    def __init__(self,pin,cardnumber):
        self.cardnumber = cardnumber
        self.pin = pin

    def cashWithdrawl(self):
        print("Cash withdrawed")

    def balanceEnquiry(self):
        print("enquiry done")
    
aud = Atm("1234", "1848 7684 9283 2981")
print(aud.pin)
aud.balanceEnquiry()