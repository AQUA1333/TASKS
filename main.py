from accounts import SavingAccount, PremiumAccount, InvestmentAccount

sav = SavingAccount("Алексей", 5000, interest_rate=0.02, min_balance=1000)
prem = PremiumAccount("Мария", 1000, overdraft_limit=5000)
inv = InvestmentAccount("Инвестор", 10000)

print("=== ТЕСТИРОВАНИЕ ОПЕРАЦИЙ ===\n")

profit = sav.calculate_monthly_profit()
print(f"1. Накопительный счет (Алексей):")
print(f"   Прогноз прибыли за месяц: {profit}")
sav.withdraw(1000)
print(f"   После снятия 1000: {sav.get_account_info()}\n")

print(f"2. Премиум счет (Мария):")
try:
    prem.withdraw(2000)
    print(f"   После снятия 2000 (с комиссией): {prem.get_account_info()}\n")
except Exception as e:
    print(f"   Ошибка: {e}\n")

print(f"3. Инвестиционный счет (Инвестор):")
yearly_growth = inv.project_yearly_growth()
print(f"   Прогноз годового роста активов: {yearly_growth}")
print(f"   Инфо: {inv.get_account_info()}\n")

print("=== ИТОГОВАЯ СВОДКА ПО ВСЕМ СЧЕТАМ ===")
accounts_list = [sav, prem, inv]
for acc in accounts_list:
    print(acc.get_account_info())