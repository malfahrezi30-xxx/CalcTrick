import math

# Rate mata uang statis (per 1 IDR)
CURRENCY_RATES = {
    "USD": 0.000063,
    "EUR": 0.000058,
    "SGD": 0.000085,
    "MYR": 0.000297,
    "JPY": 0.0093,
    "GBP": 0.000050,
    "SAR": 0.000236,
    "AUD": 0.000097,
}

CURRENCY_NAMES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "SGD": "Singapore Dollar",
    "MYR": "Malaysian Ringgit",
    "JPY": "Japanese Yen",
    "GBP": "British Pound",
    "SAR": "Saudi Riyal",
    "AUD": "Australian Dollar",
}


def konversi_basis(nilai, dari, ke):
    """Konversi bilangan antar basis: dec, bin, oct, hex."""
    result = None
    formula = ""
    steps = []
    error = None

    basis_nama = {"dec": "Desimal (10)", "bin": "Biner (2)", "oct": "Oktal (8)", "hex": "Heksadesimal (16)"}
    basis_int = {"dec": 10, "bin": 2, "oct": 8, "hex": 16}

    try:
        # Parse input ke desimal dulu
        nilai_str = str(nilai).strip().lower().replace("0x", "").replace("0b", "").replace("0o", "")
        nilai_dec = int(nilai_str, basis_int[dari])

        # Konversi ke target
        if ke == "dec":
            result = str(nilai_dec)
        elif ke == "bin":
            result = bin(nilai_dec)[2:]
        elif ke == "oct":
            result = oct(nilai_dec)[2:]
        elif ke == "hex":
            result = hex(nilai_dec)[2:].upper()

        formula = f"{nilai} ({basis_nama[dari]}) = {result} ({basis_nama[ke]})"

        # Langkah detail: selalu lewat desimal
        if dari != "dec":
            steps.append(f"Langkah 1 – Konversi {basis_nama[dari]} → Desimal:")
            steps.append(f"  Nilai input: {nilai}")
            if dari == "bin":
                # Tampilkan proses konversi biner ke desimal
                digits = nilai_str
                step_detail = " + ".join(
                    [f"{d}×2^{len(digits)-i-1}" for i, d in enumerate(digits)]
                )
                step_vals = " + ".join(
                    [str(int(d) * (2 ** (len(digits) - i - 1))) for i, d in enumerate(digits)]
                )
                steps.append(f"  {step_detail}")
                steps.append(f"  = {step_vals} = {nilai_dec}")
            elif dari == "oct":
                digits = nilai_str
                step_detail = " + ".join(
                    [f"{d}×8^{len(digits)-i-1}" for i, d in enumerate(digits)]
                )
                step_vals = " + ".join(
                    [str(int(d) * (8 ** (len(digits) - i - 1))) for i, d in enumerate(digits)]
                )
                steps.append(f"  {step_detail}")
                steps.append(f"  = {step_vals} = {nilai_dec}")
            elif dari == "hex":
                hex_map = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
                digits = nilai_str.lower()
                step_detail = " + ".join(
                    [f"{d.upper()}({hex_map.get(d, d)})×16^{len(digits)-i-1}" for i, d in enumerate(digits)]
                )
                steps.append(f"  {step_detail} = {nilai_dec}")
        else:
            steps.append(f"Nilai desimal: {nilai_dec}")

        if ke != "dec":
            steps.append(f"Langkah {'2' if dari != 'dec' else '1'} – Konversi Desimal → {basis_nama[ke]}:")
            if ke == "bin":
                n = nilai_dec
                remainders = []
                temp = n
                while temp > 0:
                    remainders.append(f"  {temp} ÷ 2 = {temp // 2} sisa {temp % 2}")
                    temp //= 2
                if not remainders:
                    remainders.append("  0")
                steps.extend(remainders)
                steps.append(f"  Baca sisa dari bawah ke atas: {result}")
            elif ke == "oct":
                n = nilai_dec
                remainders = []
                temp = n
                while temp > 0:
                    remainders.append(f"  {temp} ÷ 8 = {temp // 8} sisa {temp % 8}")
                    temp //= 8
                if not remainders:
                    remainders.append("  0")
                steps.extend(remainders)
                steps.append(f"  Baca sisa dari bawah ke atas: {result}")
            elif ke == "hex":
                n = nilai_dec
                remainders = []
                temp = n
                hex_chars = "0123456789ABCDEF"
                while temp > 0:
                    remainders.append(f"  {temp} ÷ 16 = {temp // 16} sisa {hex_chars[temp % 16]}")
                    temp //= 16
                if not remainders:
                    remainders.append("  0")
                steps.extend(remainders)
                steps.append(f"  Baca sisa dari bawah ke atas: {result}")

        steps.append(f"Hasil akhir: {nilai} ({basis_nama[dari]}) = {result} ({basis_nama[ke]})")

    except ValueError:
        error = f"Nilai '{nilai}' tidak valid untuk basis {basis_nama.get(dari, dari)}!"
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {"result": result, "formula": formula, "steps": steps, "error": error}


def konversi_suhu(nilai, dari, ke):
    """Konversi suhu: celsius, fahrenheit, kelvin, reamur."""
    result = None
    formula = ""
    steps = []
    error = None

    suhu_nama = {
        "celsius": "Celsius (°C)",
        "fahrenheit": "Fahrenheit (°F)",
        "kelvin": "Kelvin (K)",
        "reamur": "Réaumur (°Ré)",
    }

    try:
        nilai = float(nilai)

        # Konversi ke Celsius dulu (sebagai perantara)
        if dari == "celsius":
            c = nilai
        elif dari == "fahrenheit":
            c = (nilai - 32) * 5 / 9
        elif dari == "kelvin":
            c = nilai - 273.15
        elif dari == "reamur":
            c = nilai * 5 / 4
        else:
            raise ValueError("Satuan asal tidak dikenal!")

        # Konversi dari Celsius ke tujuan
        if ke == "celsius":
            result = c
            formula_str = f"{nilai} → {result:.4f}"
        elif ke == "fahrenheit":
            result = c * 9 / 5 + 32
            formula_str = f"(°C × 9/5) + 32"
        elif ke == "kelvin":
            result = c + 273.15
            formula_str = f"°C + 273.15"
        elif ke == "reamur":
            result = c * 4 / 5
            formula_str = f"°C × 4/5"
        else:
            raise ValueError("Satuan tujuan tidak dikenal!")

        result = round(result, 4)
        formula = f"{nilai} {suhu_nama[dari]} = {result} {suhu_nama[ke]}"

        # Langkah detail
        if dari == ke:
            steps = [
                f"Satuan asal dan tujuan sama: {suhu_nama[dari]}",
                f"Hasil: {result} {suhu_nama[ke]}",
            ]
        else:
            steps = [f"Konversi: {suhu_nama[dari]} → {suhu_nama[ke]}"]
            if dari != "celsius":
                steps.append(f"Langkah 1 – Konversi {suhu_nama[dari]} → Celsius:")
                if dari == "fahrenheit":
                    steps.append(f"  °C = (°F - 32) × 5/9")
                    steps.append(f"  °C = ({nilai} - 32) × 5/9 = {c:.4f}°C")
                elif dari == "kelvin":
                    steps.append(f"  °C = K - 273.15")
                    steps.append(f"  °C = {nilai} - 273.15 = {c:.4f}°C")
                elif dari == "reamur":
                    steps.append(f"  °C = °Ré × 5/4")
                    steps.append(f"  °C = {nilai} × 5/4 = {c:.4f}°C")
                langkah2 = "Langkah 2"
            else:
                steps.append(f"  Nilai Celsius: {c:.4f}°C")
                langkah2 = "Langkah 1"

            if ke != "celsius":
                steps.append(f"{langkah2} – Konversi Celsius → {suhu_nama[ke]}:")
                if ke == "fahrenheit":
                    steps.append(f"  °F = (°C × 9/5) + 32")
                    steps.append(f"  °F = ({c:.4f} × 9/5) + 32 = {result}°F")
                elif ke == "kelvin":
                    steps.append(f"  K = °C + 273.15")
                    steps.append(f"  K = {c:.4f} + 273.15 = {result} K")
                elif ke == "reamur":
                    steps.append(f"  °Ré = °C × 4/5")
                    steps.append(f"  °Ré = {c:.4f} × 4/5 = {result}°Ré")

            steps.append(f"Hasil akhir: {nilai} {suhu_nama[dari]} = {result} {suhu_nama[ke]}")

    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {"result": result, "formula": formula, "steps": steps, "error": error}


def konversi_mata_uang(jumlah, dari, ke):
    """Konversi mata uang. Dari IDR ke mata uang lain atau sebaliknya."""
    result = None
    formula = ""
    steps = []
    error = None

    try:
        jumlah = float(jumlah)
        dari = dari.upper()
        ke = ke.upper()

        if dari == ke:
            result = jumlah
            formula = f"{jumlah:,.2f} {dari} = {result:,.2f} {ke}"
            steps = [f"Mata uang asal dan tujuan sama: {dari}", f"Hasil: {result:,.2f} {ke}"]
        elif dari == "IDR":
            if ke not in CURRENCY_RATES:
                raise ValueError(f"Mata uang '{ke}' tidak tersedia!")
            rate = CURRENCY_RATES[ke]
            result = jumlah * rate
            result = round(result, 4)
            formula = f"IDR {jumlah:,.0f} = {ke} {result:,.4f}"
            steps = [
                f"Konversi: IDR → {ke} ({CURRENCY_NAMES.get(ke, ke)})",
                f"Jumlah: IDR {jumlah:,.0f}",
                f"Rate: 1 IDR = {rate} {ke} (rate statis)",
                f"Rumus: Jumlah IDR × Rate",
                f"Perhitungan: {jumlah:,.0f} × {rate} = {result:,.4f}",
                f"Hasil: {ke} {result:,.4f}",
            ]
        elif ke == "IDR":
            if dari not in CURRENCY_RATES:
                raise ValueError(f"Mata uang '{dari}' tidak tersedia!")
            rate = CURRENCY_RATES[dari]
            result = jumlah / rate
            result = round(result, 2)
            formula = f"{dari} {jumlah:,.4f} = IDR {result:,.2f}"
            steps = [
                f"Konversi: {dari} ({CURRENCY_NAMES.get(dari, dari)}) → IDR",
                f"Jumlah: {dari} {jumlah:,.4f}",
                f"Rate: 1 IDR = {rate} {dari}, maka 1 {dari} = {1/rate:,.2f} IDR",
                f"Rumus: Jumlah {dari} ÷ Rate",
                f"Perhitungan: {jumlah:,.4f} ÷ {rate} = IDR {result:,.2f}",
                f"Hasil: IDR {result:,.2f}",
            ]
        else:
            # Konversi lewat IDR
            if dari not in CURRENCY_RATES or ke not in CURRENCY_RATES:
                raise ValueError(f"Konversi {dari} → {ke} tidak tersedia!")
            rate_dari = CURRENCY_RATES[dari]
            rate_ke = CURRENCY_RATES[ke]
            idr = jumlah / rate_dari
            result = idr * rate_ke
            result = round(result, 4)
            formula = f"{dari} {jumlah:,.4f} = {ke} {result:,.4f}"
            steps = [
                f"Konversi: {dari} → {ke} (via IDR)",
                f"Langkah 1: {dari} → IDR",
                f"  {jumlah:,.4f} {dari} ÷ {rate_dari} = IDR {idr:,.2f}",
                f"Langkah 2: IDR → {ke}",
                f"  IDR {idr:,.2f} × {rate_ke} = {result:,.4f} {ke}",
                f"Hasil: {ke} {result:,.4f}",
            ]

    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {"result": result, "formula": formula, "steps": steps, "error": error,
            "currencies": list(CURRENCY_RATES.keys()) + ["IDR"],
            "currency_names": CURRENCY_NAMES}


def hitung_faktorial(n):
    """Hitung faktorial n!"""
    result = None
    formula = ""
    steps = []
    error = None

    try:
        n = int(n)
        if n < 0:
            raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif!")
        if n > 20:
            raise ValueError("Masukkan bilangan ≤ 20 untuk menghindari angka yang terlalu besar!")

        result = math.factorial(n)
        formula = f"{n}! = {result}"

        if n == 0:
            steps = [
                "n = 0",
                "Definisi: 0! = 1",
                f"Hasil: 0! = 1",
            ]
        else:
            perkalian = " × ".join([str(i) for i in range(n, 0, -1)])
            steps = [
                f"n = {n}",
                f"Rumus Faktorial: n! = n × (n-1) × (n-2) × ... × 2 × 1",
                f"{n}! = {perkalian}",
            ]
            # Hitung bertahap
            running = 1
            for i in range(1, n + 1):
                running *= i
                if i < n:
                    steps.append(f"  {i}! = {running}")
            steps.append(f"{n}! = {result}")

    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {"result": result, "formula": formula, "steps": steps, "error": error}


def hitung_fibonacci(n):
    """Hitung deret Fibonacci hingga suku ke-n."""
    result = None
    formula = ""
    steps = []
    deret = []
    error = None

    try:
        n = int(n)
        if n < 1:
            raise ValueError("Masukkan bilangan bulat positif (≥ 1)!")
        if n > 50:
            raise ValueError("Masukkan bilangan ≤ 50 untuk efisiensi!")

        # Hitung deret Fibonacci
        a, b = 0, 1
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b

        result = deret[-1]
        formula = f"F({n}) = {result}"
        deret_str = ", ".join(map(str, deret))

        steps = [
            f"n = {n} (suku ke-{n})",
            f"Rumus Fibonacci: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)",
            f"Deret: {deret_str}",
        ]

        # Tampilkan proses penambahan
        if n >= 3:
            steps.append("Proses penghitungan:")
            for i in range(2, min(n, 10)):
                steps.append(f"  F({i}) = F({i-1}) + F({i-2}) = {deret[i-1]} + {deret[i-2]} = {deret[i]}")
            if n > 10:
                steps.append(f"  ... (dilanjutkan hingga suku ke-{n})")

        steps.append(f"Suku ke-{n}: F({n-1}) = {result}")

    except ValueError as e:
        error = str(e)
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {"result": result, "formula": formula, "steps": steps, "deret": deret, "error": error}
