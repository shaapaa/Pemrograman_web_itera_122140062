import tkinter as tk
from tkinter import ttk, messagebox, font
from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    _next_id = 1 

    def __init__(self, title):
        # Private ID
        self.__id = LibraryItem._next_id
        LibraryItem._next_id += 1
        self._title = title

    @property
    def id(self):
        """Read-only property for ID"""
        return self.__id

    @property
    def title(self):
        """Read-only property for title"""
        return self._title

    @abstractmethod
    def get_info(self):
        """Must be implemented by subclasses to return tuple of display info"""
        pass

# Subclasses implementasi Abstract Method
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title)
        self._author = author
        self._pages = pages

    def get_info(self):
        # Polymorphic untuk buku
        return (self.id, self.title, "Book", self._author, f"{self._pages} pages")

class Newspaper(LibraryItem):
    def __init__(self, title, publish_date, publisher):
        super().__init__(title)
        self._publish_date = publish_date
        self._publisher = publisher

    @property
    def publish_date(self):
        # Contoh pengguaan property untuk publish_date
        return self._publish_date

    def get_info(self):
        # Impllementasi polymorphic untuk koran
        return (
            self.id,
            self.title,
            "Newspaper",
            f"Date: {self.publish_date}",
            f"Publisher: {self._publisher}"
        )

# Library Class for Collection Management
class Library:
    def __init__(self):
        # Private list
        self._items = []

    def add_item(self, item: LibraryItem):
        """Add a LibraryItem to the collection"""
        self._items.append(item)

    def list_items(self):
        """Return list of info tuples for all items"""
        return [item.get_info() for item in self._items]

    def search(self, query):
        """Search items by title substring or exact ID"""
        q = query.lower()
        return [item.get_info() for item in self._items
                if q in item.title.lower() or q == str(item.id)]

# GUI Application 
class LibraryApp(tk.Tk):
    def __init__(self, library: Library):
        super().__init__()
        self.library = library
        self.title("Shafa's Management Perpus")
        self.configure(bg="#EBE8DB") 
        self.geometry("820x560")

        self.header_font = font.Font(family="Georgia", size=20, weight="bold", slant="italic")
        self.default_font = font.Font(family="Arial", size=11)

        self._build_ui()

    def _build_ui(self):
        # Header
        header = tk.Label(self, text="Shafa's Management Perpus", bg="#B03052", fg="white",
                          font=self.header_font, pady=12)
        header.pack(fill=tk.X)

        # Main frame
        main_frame = tk.Frame(self, bg="#EBE8DB")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # Side panel
        side = tk.Frame(main_frame, bg="#D76C82", width=230)
        side.pack(side=tk.LEFT, fill=tk.Y, padx=(0,12))

        # Buttons in side panel
        buttons = [("Tambah Buku", self._show_add_book),
                   ("Tambah Koran", self._show_add_news),
                   ("Daftar Item", self._refresh_list)]

        for text, cmd in buttons:
            btn = tk.Button(side, text=text, bg="#B03052", fg="white",
                            font=self.default_font, relief=tk.FLAT,
                            activebackground="#3D0301", activeforeground="white",
                            command=cmd)
            btn.pack(fill=tk.X, pady=8, padx=12)

        # (search + table)
        content = tk.Frame(main_frame, bg="#EBE8DB")
        content.pack(fill=tk.BOTH, expand=True)

        # Search bar
        search_frame = tk.Frame(content, bg="#EBE8DB")
        search_frame.pack(fill=tk.X, pady=(0,12))
        lbl = tk.Label(search_frame, text="Cari (judul/ID):", bg="#EBE8DB",
                       font=self.default_font)
        lbl.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame, font=self.default_font)
        self.search_entry.pack(side=tk.LEFT, padx=8)
        search_btn = tk.Button(search_frame, text="Cari", bg="#B03052", fg="white",
                               font=self.default_font, relief=tk.FLAT,
                               activebackground="#3D0301",
                               command=self._search)
        search_btn.pack(side=tk.LEFT)

        # scrollbar
        cols = ("ID","Judul","Tipe","Info 1","Info 2")
        table_frame = tk.Frame(content)
        table_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings",
                                  yscrollcommand=scrollbar.set)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor=tk.CENTER, width=130)
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)

        # Initial load of items
        self._refresh_list()

    def _popup_form(self, title, fields, callback):
        # Popup window 
        pop = tk.Toplevel(self)
        pop.title(f"Tambah {title}")
        pop.configure(bg="#EBE8DB")
        pop.geometry("360x220")

        entries = {}
        for idx, field in enumerate(fields):
            lbl = tk.Label(pop, text=f"{field}:", bg="#EBE8DB", font=self.default_font)
            lbl.grid(row=idx, column=0, sticky='w', padx=12, pady=6)
            ent = tk.Entry(pop, font=self.default_font)
            ent.grid(row=idx, column=1, padx=12, pady=6, sticky='ew')
            entries[field] = ent
        pop.columnconfigure(1, weight=1)

        def on_submit():
            try:
                callback(entries)
                pop.destroy()
                self._refresh_list()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        btn = tk.Button(pop, text="Submit", bg="#B03052", fg="white",
                        font=self.default_font, relief=tk.FLAT,
                        activebackground="#3D0301", command=on_submit)
        btn.grid(row=len(fields), column=0, columnspan=2, pady=18)

#pOPUP FORM
    def _show_add_book(self):
        self._popup_form("Buku", ["Judul","Penulis","Halaman"], self._add_book)

    def _show_add_news(self):
        self._popup_form("Koran", ["Judul","Tanggal","Penerbit"], self._add_news)

    def _add_book(self, ents):
        # Callback untuk create Book
        title = ents["Judul"].get().strip()
        author = ents["Penulis"].get().strip()
        pages = int(ents["Halaman"].get().strip())
        self.library.add_item(Book(title, author, pages))

    def _add_news(self, ents):
        # Callback untuk create Newspaper
        title = ents["Judul"].get().strip()
        date = ents["Tanggal"].get().strip()
        publisher = ents["Penerbit"].get().strip()
        self.library.add_item(Newspaper(title, date, publisher))

    def _refresh_list(self, items=None):
        # Refresh table content
        for row in self.tree.get_children():
            self.tree.delete(row)
        for itm in items or self.library.list_items():
            self.tree.insert("", tk.END, values=itm)

    def _search(self):
        q = self.search_entry.get().strip()
        if q:
            results = self.library.search(q)
            self._refresh_list(results)
        else:
            self._refresh_list()

# Main function
if __name__ == "__main__": 
    lib = Library()
    app = LibraryApp(lib)
    app.mainloop()