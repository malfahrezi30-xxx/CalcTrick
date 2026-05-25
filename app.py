try:
    from flask import Flask, render_template, request, session, jsonify  # type: ignore
except Exception as e:
    raise ImportError("Flask is required to run this app. Install it with: pip install Flask") from e
from calculator.arithmetic import hitung as hitung_aritmatika
from calculator.logic import hitung_logika
from calculator.transformasi import (
    konversi_basis, konversi_suhu, konversi_mata_uang,
    hitung_faktorial, hitung_fibonacci, CURRENCY_RATES, CURRENCY_NAMES
)
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "kalkulator_canggih_secret_2024"


def tambah_history(kategori, formula, result):
    """Tambahkan item ke riwayat perhitungan di session."""
    if "history" not in session:
        session["history"] = []
    history = session["history"]
    history.insert(0, {
        "kategori": kategori,
        "formula": formula,
        "result": str(result),
        "waktu": datetime.now().strftime("%H:%M:%S"),
    })
    # Batasi maksimal 20 riwayat
    session["history"] = history[:20]
    session.modified = True


# ──────────────────────────────────────────────
#  HALAMAN UTAMA
# ──────────────────────────────────────────────
@app.route("/")
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    session.modified = True
    return jsonify({"status": "ok"})


# ──────────────────────────────────────────────
#  OPERASI ARITMATIKA
# ──────────────────────────────────────────────
@app.route("/aritmatika", methods=["GET", "POST"])
def aritmatika():
    hasil = None
    if request.method == "POST":
        try:
            operasi = request.form.get("operasi", "tambah")
            a = float(request.form.get("a", 0))

            # Operasi akar hanya butuh satu input
            if operasi == "akar":
                b = None
            else:
                b = float(request.form.get("b", 0))

            hasil = hitung_aritmatika(operasi, a, b)

            if not hasil["error"] and hasil["result"] is not None:
                tambah_history("Aritmatika", hasil["formula"], hasil["result"])

        except ValueError:
            hasil = {
                "error": "Input tidak valid! Masukkan angka yang benar.",
                "result": None, "formula": "", "steps": [],
                "operasi": "", "a": None, "b": None
            }

    history = session.get("history", [])
    return render_template("aritmatika.html", hasil=hasil, history=history)


# ──────────────────────────────────────────────
#  OPERATOR LOGIKA
# ──────────────────────────────────────────────
@app.route("/logika", methods=["GET", "POST"])
def logika():
    hasil = None
    if request.method == "POST":
        try:
            operasi = request.form.get("operasi", "and")
            a = request.form.get("a", "0")

            if operasi == "not":
                b = None
            else:
                b = request.form.get("b", "0")

            hasil = hitung_logika(operasi, a, b)

            if not hasil["error"] and hasil["result"] is not None:
                tambah_history("Logika", hasil["formula"], hasil["result"])

        except Exception as e:
            hasil = {
                "error": f"Input tidak valid: {str(e)}",
                "result": None, "formula": "", "steps": [],
                "truth_table": [], "operasi": "", "a": None, "b": None
            }

    history = session.get("history", [])
    return render_template("logika.html", hasil=hasil, history=history)


# ──────────────────────────────────────────────
#  TRANSFORMASI BILANGAN
# ──────────────────────────────────────────────
@app.route("/transformasi", methods=["GET", "POST"])
def transformasi():
    hasil = None
    tab_aktif = request.form.get("tab_aktif", "basis") if request.method == "POST" else "basis"

    currencies = list(CURRENCY_RATES.keys()) + ["IDR"]
    currency_names = CURRENCY_NAMES

    if request.method == "POST":
        jenis = request.form.get("jenis", "basis")
        tab_aktif = jenis

        try:
            if jenis == "basis":
                nilai = request.form.get("nilai_basis", "0")
                dari = request.form.get("dari_basis", "dec")
                ke = request.form.get("ke_basis", "bin")
                hasil = konversi_basis(nilai, dari, ke)
                if not hasil["error"]:
                    tambah_history("Konversi Basis", hasil["formula"], hasil["result"])

            elif jenis == "suhu":
                nilai = request.form.get("nilai_suhu", "0")
                dari = request.form.get("dari_suhu", "celsius")
                ke = request.form.get("ke_suhu", "fahrenheit")
                hasil = konversi_suhu(nilai, dari, ke)
                if not hasil["error"]:
                    tambah_history("Konversi Suhu", hasil["formula"], hasil["result"])

            elif jenis == "mata_uang":
                jumlah = request.form.get("jumlah_uang", "0")
                dari = request.form.get("dari_uang", "IDR")
                ke = request.form.get("ke_uang", "USD")
                hasil = konversi_mata_uang(jumlah, dari, ke)
                if not hasil["error"]:
                    tambah_history("Konversi Mata Uang", hasil["formula"], hasil["result"])

            elif jenis == "faktorial":
                n = request.form.get("n_faktorial", "5")
                hasil = hitung_faktorial(n)
                if not hasil["error"]:
                    tambah_history("Faktorial", hasil["formula"], hasil["result"])

            elif jenis == "fibonacci":
                n = request.form.get("n_fibonacci", "10")
                hasil = hitung_fibonacci(n)
                if not hasil["error"]:
                    tambah_history("Fibonacci", hasil["formula"], hasil["result"])

        except Exception as e:
            hasil = {
                "error": f"Terjadi kesalahan: {str(e)}",
                "result": None, "formula": "", "steps": []
            }

    history = session.get("history", [])
    return render_template(
        "transformasi.html",
        hasil=hasil,
        tab_aktif=tab_aktif,
        history=history,
        currencies=currencies,
        currency_names=currency_names,
    )


# ──────────────────────────────────────────────
#  ERROR HANDLERS
# ──────────────────────────────────────────────
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html", error="Halaman tidak ditemukan!"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("index.html", error="Terjadi kesalahan server!"), 500


if __name__ == "__main__":
    app.run(debug=True)
