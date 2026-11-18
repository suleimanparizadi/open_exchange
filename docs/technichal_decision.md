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


the authentications will be based on the simple JWT tokens


Login remains phone + password. OTP-only login rejected: single-factor risk (SIM swap), no security gain over existing flow, and real exchanges treat OTP as a second factor, not a primary one.



"Login uses phone_number + password. Email login rejected: it does not mitigate SIM swap (which attacks the phone channel, not the login form) and introduces email takeover as an alternate attack path. SIM swap risk is mitigated by not using SMS OTP for login and by preferring email OTP for sensitive actions. TOTP considered for Phase 6+