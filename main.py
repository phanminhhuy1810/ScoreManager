students = []

def them_sinh_vien(ten, diem):
    sinh_vien = {"ten": ten, "diem": diem}
    students.append(sinh_vien)

def hien_thi_tat_ca():
    print("\n--- DANH SÁCH SINH VIÊN ---")
    for sv in students:
        print(f"Tên: {sv['ten']} | Điểm: {sv['diem']}")

def tinh_trung_binh():
    if len(students) == 0:
        print("Chưa có sinh viên nào!")
        return
    tong = 0
    for sv in students:
        tong += sv["diem"]
    trung_binh = tong / len(students)
    print(f"\nĐiểm trung bình: {trung_binh:.2f}")

# Thêm thử vài sinh viên
them_sinh_vien("An", 8.5)
them_sinh_vien("Bình", 7.0)
them_sinh_vien("Chi", 9.2)

hien_thi_tat_ca()
tinh_trung_binh()