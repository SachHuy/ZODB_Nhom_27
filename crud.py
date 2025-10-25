import csv
import json
from models import Contact
from db import contacts, commit

# ------------------- CRUD cơ bản -------------------

def add_contact():
    name = input("Tên: ").strip()
    if name in contacts:
        print("⚠️  Liên hệ đã tồn tại.")
        return
    phone = input("Số điện thoại: ").strip()
    email = input("Email: ").strip()
    contacts[name] = Contact(name, phone, email)
    commit()
    print("✅ Đã thêm liên hệ mới!")

def list_contacts():
    if not contacts:
        print("📭 Không có liên hệ nào.")
    else:
        print("\n📒 Danh sách liên hệ:")
        for name, c in contacts.items():
            print(f"- {c.name} | ☎ {c.phone} | ✉ {c.email}")

def update_contact():
    name = input("Nhập tên liên hệ cần sửa: ").strip()
    if name not in contacts:
        print("❌ Không tìm thấy liên hệ.")
        return
    phone = input("Số điện thoại mới (Enter nếu giữ nguyên): ").strip()
    email = input("Email mới (Enter nếu giữ nguyên): ").strip()
    contacts[name].update(phone if phone else None, email if email else None)
    commit()
    print("✅ Đã cập nhật!")

def delete_contact():
    name = input("Nhập tên liên hệ cần xóa: ").strip()
    if name in contacts:
        del contacts[name]
        commit()
        print("🗑️  Đã xóa liên hệ.")
    else:
        print("❌ Không tìm thấy liên hệ.")

def search_contact():
    keyword = input("Nhập từ khóa tìm kiếm (tên, số điện thoại, email): ").strip().lower()
    results = []
    for c in contacts.values():
        if keyword in c.name.lower() or keyword in c.phone.lower() or keyword in c.email.lower():
            results.append(c)
    if results:
        print(f"\n🔍 Kết quả tìm kiếm ({len(results)} liên hệ):")
        for c in results:
            print(f"- {c.name} | ☎ {c.phone} | ✉ {c.email}")
    else:
        print("❌ Không tìm thấy liên hệ phù hợp.")

# ------------------- Xuất/nhập CSV -------------------

def export_csv(filename="contacts.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        for c in contacts.values():
            writer.writerow([c.name, c.phone, c.email])
    print(f"✅ Đã xuất danh bạ ra {filename}")

def import_csv(filename="contacts.csv"):
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["Name"]
                phone = row["Phone"]
                email = row["Email"]
                contacts[name] = Contact(name, phone, email)
        commit()
        print(f"✅ Đã nhập danh bạ từ {filename}")
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {filename}")

# ------------------- Xuất/nhập JSON -------------------

def export_json(filename="contacts.json"):
    data = {c.name: {"phone": c.phone, "email": c.email} for c in contacts.values()}
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Đã xuất danh bạ ra {filename}")

def import_json(filename="contacts.json"):
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            data = json.load(f)
            for name, info in data.items():
                contacts[name] = Contact(name, info.get("phone", ""), info.get("email", ""))
        commit()
        print(f"✅ Đã nhập danh bạ từ {filename}")
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {filename}")
