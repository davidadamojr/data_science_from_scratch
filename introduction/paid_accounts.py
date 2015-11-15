# PAID ACCOUNTS
# eyeballed, we can build a model to predict paid and unpaid users based on data we have on years of experience and payment
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"