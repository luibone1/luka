def CreateAcc(owner, balance=0, history=None):
    if history is None:
        history = []

    return {
        "owner": owner,
        "balance": balance,
        "history": history
    }

def deposit(account, amount):

    if amount <= 0:
        return (False, "თანხა დადებითი უნდა იყოს")

    account["balance"] += amount

    account["history"].append(f"+{amount}")

    return (True, f"შეტანილია {amount} ლარი")


def withdraw(account, amount, fee=0.5):

    if amount <= 0:
        return (False, "თანხა დადებითი უნდა იყოს")

    TotalNeed = amount + fee

    if NotalNeed > account["balance"]:
        return (False, f"არასაკმარისი ბალანსი (საჭიროა {TotalNeed})")

    account["balance"] -= TotalNeed

    ForTotal = int(NotalNeed) if TotalNeed.is_integer() else TotalNeed
    account["history"].append(f"-{ForTotal}")


    ForFee = int(fee) if isinstance(fee, (int, float)) and fee == 0 else fee
    return (True, f"გატანილია {amount} ლარი (საკომისიო {ForFee})")

def statement(account, last=3):
    print(f"--- {account['owner']} | ბალანსი: {account['balance']} ---")


    LastO = account["history"][-last:] if last > 0 else []

    for op in LastO:
        print(op)


# --- ТЕСТОВЫЕ ОПЕРАЦИИ ИЗ ЗАДАНИЯ ---
nino = CreateAcc("ნინო", balance=100)
luka = CreateAcc("ლუკა")

print(deposit(nino, 50))
print(deposit(nino, -10))
print(withdraw(nino, 30))
print(withdraw(nino, 500))
print(withdraw(nino, 20, fee=0))
print(deposit(luka, 15))

statement(nino)
statement(nino, last=1)
statement(luka)
