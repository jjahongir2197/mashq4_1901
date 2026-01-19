class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_free = True

    def info(self):
        status = "Bo‘sh" if self.is_free else "Band"
        return f"{self.room_number} | {self.room_type} | {self.price} so‘m | {status}"


class Customer:
    def __init__(self, passport_id, name):
        self.passport_id = passport_id
        self.name = name
        self.room = None
        self.days = 0

    def info(self):
        if self.room:
            return f"{self.name} | Xona: {self.room.room_number} | {self.days} kun"
        return f"{self.name} | Xona yo‘q"


class Hotel:
    def __init__(self):
        self.rooms = []
        self.customers = {}
        self.balance = 0

    # ---------- ROOM ----------
    def add_room(self, room):
        self.rooms.append(room)
        print("Xona qo‘shildi")

    def show_rooms(self):
        if not self.rooms:
            print("Xonalar yo‘q")
        for r in self.rooms:
            print(r.info())

    def free_rooms(self):
        free = [r for r in self.rooms if r.is_free]
        if not free:
            print("Bo‘sh xonalar yo‘q")
        for r in free:
            print(r.info())

    # ---------- CUSTOMER ----------
    def add_customer(self, customer):
        self.customers[customer.passport_id] = customer
        print("Mijoz ro‘yxatga olindi")

    def show_customers(self):
        if not self.customers:
            print("Mijozlar yo‘q")
        for c in self.customers.values():
            print(c.info())

    # ---------- BOOKING ----------
    def book_room(self, passport_id, room_number, days):
        if passport_id not in self.customers:
            print("Mijoz topilmadi")
            return

        for room in self.rooms:
            if room.room_number == room_number and room.is_free:
                room.is_free = False
                customer = self.customers[passport_id]
                customer.room = room
                customer.days = days
                cost = days * room.price
                self.balance += cost
                print("Xona band qilindi")
                print("To‘lov:", cost, "so‘m")
                return

        print("Xona band yoki mavjud emas")

    # ---------- CHECK OUT ----------
    def checkout(self, passport_id):
        if passport_id in self.customers:
            customer = self.customers[passport_id]
            if customer.room:
                customer.room.is_free = True
                customer.room = None
                customer.days = 0
                print("Mijoz chiqib ketdi")
            else:
                print("Bu mijozda xona yo‘q")

    # ---------- REPORT ----------
    def report(self):
        print("\n--- HOTEL HISOBOTI ---")
        print("Xonalar soni:", len(self.rooms))
        print("Mijozlar soni:", len(self.customers))
        print("Balans:", self.balance, "so‘m")
        print("----------------------")


# ================= MAIN MENU =================

hotel = Hotel()

# DASTLABKI XONALAR
hotel.add_room(Room(101, "Single", 200000))
hotel.add_room(Room(102, "Double", 350000))
hotel.add_room(Room(201, "Lux", 600000))

while True:
    print("\n===== HOTEL BOSHQARUV TIZIMI =====")
    print("1. Xonalarni ko‘rish")
    print("2. Bo‘sh xonalar")
    print("3. Mijoz qo‘shish")
    print("4. Mijozlar ro‘yxati")
    print("5. Xona band qilish")
    print("6. Mijozni chiqarish")
    print("7. Hisobot")
    print("0. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        hotel.show_rooms()

    elif choice == "2":
        hotel.free_rooms()

    elif choice == "3":
        pid = input("Passport ID: ")
        name = input("Ism: ")
        hotel.add_customer(Customer(pid, name))

    elif choice == "4":
        hotel.show_customers()

    elif choice == "5":
        pid = input("Passport ID: ")
        room = int(input("Xona raqami: "))
        days = int(input("Kunlar soni: "))
        hotel.book_room(pid, room, days)

    elif choice == "6":
        pid = input("Passport ID: ")
        hotel.checkout(pid)

    elif choice == "7":
        hotel.report()

    elif choice == "0":
        print("Dastur yakunlandi")
        break

    else:
        print("Noto‘g‘ri tanlov")
