import math


def hitung(operasi, a, b=None):
    """
    Melakukan operasi aritmatika dan mengembalikan hasil, rumus, dan langkah-langkah.
    """
    result = None
    formula = ""
    steps = []
    error = None

    try:
        if operasi == "tambah":
            result = a + b
            formula = f"{a} + {b} = {result}"
            steps = [
                f"Operasi: Penjumlahan",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A + B",
                f"Perhitungan: {a} + {b} = {result}",
            ]

        elif operasi == "kurang":
            result = a - b
            formula = f"{a} - {b} = {result}"
            steps = [
                f"Operasi: Pengurangan",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A - B",
                f"Perhitungan: {a} - {b} = {result}",
            ]

        elif operasi == "kali":
            result = a * b
            formula = f"{a} × {b} = {result}"
            steps = [
                f"Operasi: Perkalian",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A × B",
                f"Perhitungan: {a} × {b} = {result}",
            ]

        elif operasi == "bagi":
            if b == 0:
                raise ZeroDivisionError("Tidak dapat membagi dengan nol!")
            result = a / b
            result = round(result, 10)
            formula = f"{a} ÷ {b} = {result}"
            steps = [
                f"Operasi: Pembagian",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A ÷ B",
                f"Catatan: Pastikan B ≠ 0",
                f"Perhitungan: {a} ÷ {b} = {result}",
            ]

        elif operasi == "pangkat":
            result = a ** b
            formula = f"{a}^{b} = {result}"
            steps = [
                f"Operasi: Perpangkatan",
                f"Basis (a) = {a}",
                f"Eksponen (b) = {b}",
                f"Rumus: a^b (a dipangkatkan b)",
                f"Artinya: {a} dikalikan dengan dirinya sendiri sebanyak {b} kali",
                f"Perhitungan: {a}^{b} = {result}",
            ]

        elif operasi == "akar":
            if a < 0:
                raise ValueError("Tidak dapat menghitung akar dari bilangan negatif!")
            result = math.sqrt(a)
            result = round(result, 10)
            formula = f"√{a} = {result}"
            steps = [
                f"Operasi: Akar Kuadrat",
                f"Nilai A = {a}",
                f"Rumus: √A",
                f"Artinya: mencari bilangan x sehingga x² = {a}",
                f"Perhitungan: √{a} = {result}",
            ]

        elif operasi == "modulus":
            if b == 0:
                raise ZeroDivisionError("Tidak dapat membagi dengan nol!")
            result = a % b
            formula = f"{a} mod {b} = {result}"
            steps = [
                f"Operasi: Modulus (Sisa Bagi)",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A mod B",
                f"Artinya: sisa hasil bagi A dibagi B",
                f"Pembagian: {a} ÷ {b} = {a // b} sisa {a % b}",
                f"Hasil (sisa): {result}",
            ]

        elif operasi == "floor_div":
            if b == 0:
                raise ZeroDivisionError("Tidak dapat membagi dengan nol!")
            result = a // b
            formula = f"{a} // {b} = {result}"
            steps = [
                f"Operasi: Floor Division (Pembagian Bulat Bawah)",
                f"Nilai A = {a}",
                f"Nilai B = {b}",
                f"Rumus: A // B",
                f"Artinya: hasil bagi yang dibulatkan ke bawah",
                f"Perhitungan: {a} ÷ {b} = {a / b:.6f}",
                f"Dibulatkan ke bawah (floor): {result}",
            ]

        else:
            error = "Operasi tidak dikenal!"

    except ZeroDivisionError as e:
        error = str(e)
    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    # Format result
    if result is not None:
        if isinstance(result, float) and result.is_integer():
            result = int(result)

    return {
        "result": result,
        "formula": formula,
        "steps": steps,
        "error": error,
        "operasi": operasi,
        "a": a,
        "b": b,
    }
