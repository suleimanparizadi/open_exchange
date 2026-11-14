**Why separated the matching engine from Django?  
  
Different responsibility**

**and the rust engine must be focus on matching its not seconde financial backend**

**Django is almost perfect for backend but for complicated and resources consuming task like  match buyer and sellers offer task Rust engine is perfect.**



Auth and verifications:
user signup with email ,first name and last name, password and phone number. no verification need it. not allowed to trade.

after phone and email verification the user is able to trad.

lazy wallet creation:
wallet didn't create right away. the wallet create as the moment user touch buying.

def get_or_create_wallet(user, asset):
    wallet, created = Wallet.objects.get_or_create(user=user, asset=asset)
    return wallet

to keep it simple and take less processing power.

phone format is Iran-specific

separated Email and phone one time password model and services.





