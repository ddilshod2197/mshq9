matn = input("Matn kiriting: ").lower()

unlilar = "aeiouoʻ"
unli_son = 0
unli_harflar = []

for harf in matn:
    if harf in unlilar:
        unli_son += 1
        unli_harflar.append(harf)

print(f"\nMatnda {unli_son} ta unli harf bor.")
if unli_son > 0:
    print("Ular:", ", ".join(unli_harflar))
    print("Eng ko‘p uchragan unli:", max(set(unli_harflar), key=unli_harflar.count))
else:
    print("Hech qanday unli harf topilmadi.")
