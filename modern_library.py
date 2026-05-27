import json
import os


DATA_FILE = "books.json"


class Library:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.books = json.load(file)
            else:
                self.books = []
        except json.JSONDecodeError:
            print("資料格式錯誤，已建立新的空資料。")
            self.books = []
        except Exception as error:
            print(f"讀取檔案失敗：{error}")
            self.books = []

    def save_books(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.books, file, ensure_ascii=False, indent=4)
        except Exception as error:
            print(f"儲存檔案失敗：{error}")

    def isbn_exists(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                return True
        return False

    def add_book(self, command):
        raw_data = command[4:].split("/")

        if len(raw_data) != 3:
            print("Format Error")
            return

        title = raw_data[0].strip()
        isbn = raw_data[1].strip()
        status = raw_data[2].strip()

        if not title or not isbn or not status:
            print("Format Error")
            return

        if self.isbn_exists(isbn):
            print("ISBN Exist")
            return

        book = {
            "title": title,
            "isbn": isbn,
            "status": status
        }

        self.books.append(book)
        print("Success")

    def show_books(self):
        for book in self.books:
            print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")

    def borrow_book(self, command):
        target_isbn = command[7:].strip()

        for book in self.books:
            if book["isbn"] == target_isbn:
                book["status"] = "borrowed"
                print("Updated")
                return

        print("Book Not Found")

    def run(self):
        print("=== 圖書管理系統 v1.0 (Modern) ===")

        while True:
            command = input("> ").strip()

            if command == "exit":
                self.save_books()
                print("系統關閉")
                break
            elif command.startswith("add "):
                self.add_book(command)
            elif command == "show":
                self.show_books()
            elif command.startswith("borrow "):
                self.borrow_book(command)
            else:
                print("Unknown Command")


if __name__ == "__main__":
    library = Library()
    library.run()