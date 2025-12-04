# test_app.py
from app import tambah, kurang

def test_tambah_berhasil():
    assert tambah(1, 2) == 3
    assert tambah(-1, 1) == 0
    assert tambah(0, 0) == 0

def test_kurang_gagal():
    # Ini akan disengaja gagal untuk demonstrasi CI/CD
    assert kurang(5, 2) == 4 # seharusnya 3. Tes ini PASTI GAGAL