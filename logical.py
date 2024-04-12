has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("Eligable for loan.")

print("X"*70)
has_high_income=True
has_good_credit=False
if has_high_income and has_good_credit:
    print("Eligable for loan.")
else: 
    print("Not eligable for loan.")

print("X"*70)
has_high_income=True
has_good_credit=False
if has_high_income or has_good_credit:
    print("Eligable for loan.")

print("X"*70)
has_high_income=True
has_good_credit=False
if has_high_income and not has_good_credit:
    print("Eligable for loan.")


# and == both true
# or == one must be true
# not == change true to false false to true
