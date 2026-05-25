def hitung_logika(operasi, a, b=None):
    """
    Melakukan operasi logika bitwise dan mengembalikan hasil, rumus, tabel kebenaran, dan langkah-langkah.
    """
    result = None
    formula = ""
    steps = []
    error = None
    truth_table = []

    try:
        a_int = int(a)
        b_int = int(b) if b is not None else None

        a_bin = bin(a_int)[2:] if a_int >= 0 else bin(a_int)
        b_bin = bin(b_int)[2:] if b_int is not None and b_int >= 0 else (bin(b_int) if b_int is not None else None)

        # Ratakan panjang binary
        if b_bin is not None:
            max_len = max(len(a_bin.lstrip('-')), len(b_bin.lstrip('-')))
            a_bin_pad = a_bin.zfill(max_len)
            b_bin_pad = b_bin.zfill(max_len)
        else:
            max_len = len(a_bin.lstrip('-'))
            a_bin_pad = a_bin.zfill(max_len)
            b_bin_pad = None

        if operasi == "and":
            result = a_int & b_int
            r_bin = bin(result)[2:].zfill(max_len) if result >= 0 else bin(result)
            formula = f"{a_int} AND {b_int} = {result}"
            steps = [
                f"Operasi: AND (Bitwise)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"B = {b_int} (desimal) = {b_bin_pad} (biner)",
                f"Aturan AND: 1 AND 1 = 1, selainnya = 0",
                f"  {a_bin_pad}",
                f"  {b_bin_pad}",
                f"  {'─' * max_len}",
                f"  {r_bin}  (AND bit per bit)",
                f"Hasil biner: {r_bin}",
                f"Hasil desimal: {result}",
            ]
            truth_table = _generate_truth_table("and")

        elif operasi == "or":
            result = a_int | b_int
            r_bin = bin(result)[2:].zfill(max_len) if result >= 0 else bin(result)
            formula = f"{a_int} OR {b_int} = {result}"
            steps = [
                f"Operasi: OR (Bitwise)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"B = {b_int} (desimal) = {b_bin_pad} (biner)",
                f"Aturan OR: 0 OR 0 = 0, selainnya = 1",
                f"  {a_bin_pad}",
                f"  {b_bin_pad}",
                f"  {'─' * max_len}",
                f"  {r_bin}  (OR bit per bit)",
                f"Hasil biner: {r_bin}",
                f"Hasil desimal: {result}",
            ]
            truth_table = _generate_truth_table("or")

        elif operasi == "not":
            # NOT hanya pada A (komplemen 1)
            result = ~a_int
            r_bin = bin(result)
            formula = f"NOT {a_int} = {result}"
            steps = [
                f"Operasi: NOT (Bitwise Complement)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"Aturan NOT: membalik setiap bit (0→1, 1→0)",
                f"NOT menggunakan rumus: ~A = -(A+1) (komplemen dua)",
                f"Perhitungan: ~{a_int} = -({a_int}+1) = {result}",
                f"Hasil desimal: {result}",
                f"Representasi biner: {r_bin}",
            ]
            truth_table = _generate_truth_table("not")

        elif operasi == "xor":
            result = a_int ^ b_int
            r_bin = bin(result)[2:].zfill(max_len) if result >= 0 else bin(result)
            formula = f"{a_int} XOR {b_int} = {result}"
            steps = [
                f"Operasi: XOR (Exclusive OR)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"B = {b_int} (desimal) = {b_bin_pad} (biner)",
                f"Aturan XOR: berbeda=1, sama=0",
                f"  {a_bin_pad}",
                f"  {b_bin_pad}",
                f"  {'─' * max_len}",
                f"  {r_bin}  (XOR bit per bit)",
                f"Hasil biner: {r_bin}",
                f"Hasil desimal: {result}",
            ]
            truth_table = _generate_truth_table("xor")

        elif operasi == "nand":
            result = ~(a_int & b_int)
            r_bin = bin(result)
            and_result = a_int & b_int
            formula = f"{a_int} NAND {b_int} = {result}"
            steps = [
                f"Operasi: NAND (NOT AND)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"B = {b_int} (desimal) = {b_bin_pad} (biner)",
                f"Langkah 1 – AND: {a_int} AND {b_int} = {and_result}",
                f"  (biner AND: {bin(and_result)})",
                f"Langkah 2 – NOT: ~({and_result}) = {result}",
                f"Rumus NAND: NOT(A AND B)",
                f"Hasil desimal: {result}",
            ]
            truth_table = _generate_truth_table("nand")

        elif operasi == "nor":
            result = ~(a_int | b_int)
            r_bin = bin(result)
            or_result = a_int | b_int
            formula = f"{a_int} NOR {b_int} = {result}"
            steps = [
                f"Operasi: NOR (NOT OR)",
                f"A = {a_int} (desimal) = {a_bin_pad} (biner)",
                f"B = {b_int} (desimal) = {b_bin_pad} (biner)",
                f"Langkah 1 – OR: {a_int} OR {b_int} = {or_result}",
                f"  (biner OR: {bin(or_result)})",
                f"Langkah 2 – NOT: ~({or_result}) = {result}",
                f"Rumus NOR: NOT(A OR B)",
                f"Hasil desimal: {result}",
            ]
            truth_table = _generate_truth_table("nor")

        else:
            error = "Operasi logika tidak dikenal!"

    except ValueError as e:
        error = f"Input tidak valid: {str(e)}. Masukkan bilangan bulat."
    except Exception as e:
        error = f"Terjadi kesalahan: {str(e)}"

    return {
        "result": result,
        "formula": formula,
        "steps": steps,
        "truth_table": truth_table,
        "error": error,
        "operasi": operasi,
        "a": a,
        "b": b,
    }


def _generate_truth_table(op):
    """Generate tabel kebenaran untuk 1-bit operasi logika."""
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    table = []

    for pair in inputs:
        a, b = pair
        if op == "and":
            res = a & b
        elif op == "or":
            res = a | b
        elif op == "not":
            res = int(not bool(a))
        elif op == "xor":
            res = a ^ b
        elif op == "nand":
            res = int(not bool(a & b))
        elif op == "nor":
            res = int(not bool(a | b))
        else:
            res = 0

        if op == "not":
            table.append({"a": a, "result": res})
            if len(table) == 2:
                break
        else:
            table.append({"a": a, "b": b, "result": res})

    return table
