import tkinter as tk
from tkinter import messagebox

class BookShopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Shop Management")
        self.root.geometry("800x600")
        self.root.config(bg="#2c3e50")  # تغيير خلفية التطبيق إلى داكنة

        # تعيين أيقونة للتطبيق
        self.root.iconbitmap(r"E:\student\favicon.ico")  # تأكد من مسار الأيقونة الخاص بك

        # تعريف قائمة الكتب
        self.books = []

        # إنشاء إطار للفورم (Title, Author, Price)
        self.form_frame = tk.Frame(self.root, bg="#34495e", bd=10, relief="solid")
        self.form_frame.place(x=50, y=50, width=350, height=500)

        # Title Label و Field
        title_label = tk.Label(self.form_frame, text="Title", bg="#34495e", fg="white", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)
        self.title_var = tk.StringVar()
        self.title_entry = tk.Entry(self.form_frame, textvariable=self.title_var, width=30, font=("Arial", 12), bd=3, bg="#2c3e50", fg="white", relief="solid")
        self.title_entry.pack(pady=5)

        # Author Label و Field
        author_label = tk.Label(self.form_frame, text="Author", bg="#34495e", fg="white", font=("Arial", 12, "bold"))
        author_label.pack(pady=10)
        self.author_var = tk.StringVar()
        self.author_entry = tk.Entry(self.form_frame, textvariable=self.author_var, width=30, font=("Arial", 12), bd=3, bg="#2c3e50", fg="white", relief="solid")
        self.author_entry.pack(pady=5)

        # Price Label و Field
        price_label = tk.Label(self.form_frame, text="Price", bg="#34495e", fg="white", font=("Arial", 12, "bold"))
        price_label.pack(pady=10)
        self.price_var = tk.StringVar()
        self.price_entry = tk.Entry(self.form_frame, textvariable=self.price_var, width=30, font=("Arial", 12), bd=3, bg="#2c3e50", fg="white", relief="solid")
        self.price_entry.pack(pady=5)

        # إضافة أزرار في مكان آخر (إطار منفصل)
        self.buttons_frame = tk.Frame(self.root, bg="#34495e", bd=10)
        self.buttons_frame.place(x=450, y=50, width=300, height=400)

        # إضافة زر "Add Book"
        self.add_button = tk.Button(self.buttons_frame, text="Add Book", command=self.add_book, width=20, height=2, font=("Arial", 10, "bold"), bg="#27ae60", fg="white", relief="raised")
        self.add_button.pack(pady=10)

        # إضافة زر "Delete Book"
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Book", command=self.delete_book, width=20, height=2, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", relief="raised")
        self.delete_button.pack(pady=10)

        # إضافة زر "Search Book"
        self.search_button = tk.Button(self.buttons_frame, text="Search Book", command=self.search_book, width=20, height=2, font=("Arial", 10, "bold"), bg="#3498db", fg="white", relief="raised")
        self.search_button.pack(pady=10)

        # إضافة زر "Edit Book"
        self.edit_button = tk.Button(self.buttons_frame, text="Edit Book", command=self.edit_book, width=20, height=2, font=("Arial", 10, "bold"), bg="#f39c12", fg="white", relief="raised")
        self.edit_button.pack(pady=10)

        # عرض الكتب (قائمة الكتب)
        self.book_list_frame = tk.Frame(self.root, bg="#34495e", bd=5)
        self.book_list_frame.place(x=50, y=300, width=700, height=250)

        # تعديل قائمة الكتب
        self.book_list = tk.Listbox(self.book_list_frame, height=10, width=50, font=("Arial", 12), bd=5, bg="#2c3e50", fg="white", selectbackground="#3498db", selectforeground="white")
        self.book_list.pack(pady=10)

        self.display_books()

    def display_books(self):
        self.book_list.delete(0, tk.END)
        for idx, book in enumerate(self.books, start=1):
            self.book_list.insert(tk.END, f"{idx}. {book['title']} by {book['author']} - ${book['price']}")

    def add_book(self):
        title = self.title_var.get()
        author = self.author_var.get()
        price = self.price_var.get()

        if title and author and price:
            try:
                price = float(price)
                self.books.append({"title": title, "author": author, "price": price})
                self.display_books()
                messagebox.showinfo("Success", "Book added successfully!")
                self.clear_inputs()
            except ValueError:
                messagebox.showerror("Error", "Invalid price value!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_book(self):
        selected = self.book_list.curselection()
        if selected:
            book_index = selected[0]
            self.books.pop(book_index)
            self.display_books()
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showerror("Error", "No book selected!")

    def search_book(self):
        keyword = self.title_var.get().lower()
        if keyword:
            results = [book for book in self.books if keyword in book['title'].lower() or keyword in book['author'].lower()]
            self.book_list.delete(0, tk.END)
            for idx, book in enumerate(results, start=1):
                self.book_list.insert(tk.END, f"{idx}. {book['title']} by {book['author']} - ${book['price']}")
            if not results:
                messagebox.showinfo("Info", "No matching books found.")
        else:
            messagebox.showerror("Error", "Enter a keyword to search!")

    def edit_book(self):
        selected = self.book_list.curselection()
        if selected:
            book_index = selected[0]
            title = self.title_var.get()
            author = self.author_var.get()
            price = self.price_var.get()

            if title and author and price:
                try:
                    price = float(price)
                    self.books[book_index] = {"title": title, "author": author, "price": price}
                    self.display_books()
                    messagebox.showinfo("Success", "Book updated successfully!")
                    self.clear_inputs()
                except ValueError:
                    messagebox.showerror("Error", "Invalid price value!")
            else:
                messagebox.showerror("Error", "All fields are required for editing!")
        else:
            messagebox.showerror("Error", "No book selected!")

    def clear_inputs(self):
        self.title_var.set("")
        self.author_var.set("")
        self.price_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookShopGUI(root)
    root.mainloop()
