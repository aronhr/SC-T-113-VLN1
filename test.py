import os
from random import random
import datetime

now = datetime.datetime.now()
dirname = os.path.dirname
here = dirname(dirname(os.path.abspath(__file__)))

os.makedirs(os.path.join(here, "./receipts/" + now.strftime("%Y-%m-%d")), exist_ok=True)

for i in range(1, 2):
    name = "Adam"
    ssn = "1304982499"
    if random() > .95:
        address = "221 Baker St."
    else:
        address = "Bónus"
    zipcode = "112"
    amount = "{:.2f}".format(random() * 1000)
    account = "4128 1243 2123 8012"

    # output into a multiline string
    receipt = """
                #{i}    {name}    {ssn}
                {address}
                Seattle, ----------------------------------------------------- WA {zipcode}


                ${amount} ---------------------------------------------------- Acct: {account}
                """
    output = receipt.format(i=i, name=name, ssn=ssn, address=address, zipcode=zipcode, account=account, amount=amount)

    # create file
    filename = os.path.join(here, "./receipts/" + now.strftime("%Y-%m-%d"), now.strftime("%H-%M") + ".txt")
    with open(filename, "w") as f:
        f.write(output)
