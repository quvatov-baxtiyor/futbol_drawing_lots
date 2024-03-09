import random

# 48 ta jamoa nomlari
jamoalar = [f'jamoa{i}' for i in range(1, 45)]

# Qur'a tashlash va raqiblarni saqlash uchun bo'sh ro'yxat
raqiblar = []

while len(jamoalar) >= 2:
    # Birinchi o'yin
    raqib1 = random.choice(jamoalar)
    jamoalar.remove(raqib1)

    raqib2 = random.choice(jamoalar)
    jamoalar.remove(raqib2)

    raqiblar.append((raqib1, raqib2))

# Agar raqiblar ro'yxati bo'sh bo'lmasa
if raqiblar:
    print("O'yinlar tayyor. Raqiblar:")
    for i, (raqib1, raqib2) in enumerate(raqiblar, start=1):
        print(f"O'yin {i}: {raqib1} vs {raqib2}")
else:
    print("Raqiblar mavjud emas. Qur'a tashlashda muammo bor.")


