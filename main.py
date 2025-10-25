from crud import add_contact, list_contacts, update_contact, delete_contact, search_contact
from db import close

def main():
    while True:
        print("\n====== 📇 QUẢN LÝ DANH BẠ ZODB ======")
        print("1. Thêm liên hệ")
        print("2. Xem tất cả liên hệ")
        print("3. Cập nhật liên hệ")
        print("4. Xóa liên hệ")
        print("5. Tìm kiếm liên hệ")
        print("6. Thoát")
        choice = input("Chọn (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            print("👋 Thoát chương trình...")
            break
        else:
            print("⚠️  Lựa chọn không hợp lệ!")

    close()

if __name__ == "__main__":
    main()
