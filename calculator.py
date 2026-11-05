print("--- Kalkulator 10 Baris ---")
number1 = float(input("Mosukkan angka pertama: "))
operasi = input("Masukkan operasi (+, -, *, /, **): ")
number2 = float(input("Masukkan angka kedua: "))

if operasi == "+": print(f"Hasil: {num1 + num2}")
elif operasi == "-": print(f"Hasil: {num1 - num2}")
elif operasi == "*": print(f"Hasil: {num1 * num2}")
elif operasi == "/": print(f"Hasil: {num1 / num2}" if num2 != 0 else "Error: Dibagi 0!")
elif operasi == "**": print(f"Hasil: {num1 ** num2}") # EDIT: Menambahkan baris operasi perpangkatan
else: print("Operasi tidak valid!")
