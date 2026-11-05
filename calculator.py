print("--- Kalkulator 10 Baris ---")
num1 = float(input("Masukkan angka pertama: "))
op = input("Masukkan operasi (+, -, *, /, **): ") # EDIT: Menambahkan opsi pangkat (**)
num2 = float(input("Masukkan angka kedua: "))

if op == "+": print(f"Hasil: {num1 + num2}")
elif op == "-": print(f"Hasil: {num1 - num2}")
elif op == "*": print(f"Hasil: {num1 * num2}")
elif op == "/": print(f"Hasil: {num1 / num2}" if num2 != 0 else "Error: Dibagi 0!") # EDIT: Proteksi pembagian nol
elif op == "**": print(f"Hasil: {num1 ** num2}") # EDIT: Menambahkan baris operasi perpangkatan
else: print("Operasi tidak valid!")
