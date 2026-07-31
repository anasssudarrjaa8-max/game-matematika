from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)


# ==========================================
# HALAMAN UTAMA
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# MEMBUAT SOAL
# ==========================================

@app.route("/soal")
def soal():

    jenis = request.args.get("jenis", "campuran")

    # Jika campuran
    if jenis == "campuran":
        operasi = random.choice(["+", "-", "×"])

    else:
        operasi = jenis


    # ======================================
    # PENJUMLAHAN
    # ======================================

    if operasi == "+":

        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)

        jawaban = angka1 + angka2


    # ======================================
    # PENGURANGAN
    # ======================================

    elif operasi == "-":

        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, angka1)

        jawaban = angka1 - angka2


    # ======================================
    # PERKALIAN
    # ======================================

    elif operasi == "×":

        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)

        jawaban = angka1 * angka2


    return jsonify({

        "angka1": angka1,

        "angka2": angka2,

        "operasi": operasi,

        "jawaban": jawaban

    })


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)