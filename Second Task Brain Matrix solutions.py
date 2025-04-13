import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3

# DB setup
conn = sqlite3.connect('inventory.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)")
c.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", ('admin', 'admin123'))
conn.commit()

# Login check
def login():
    u, p = user.get(), pwd.get()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    if c.fetchone():
        login_win.destroy()
        open_main_window()
    else:
        messagebox.showerror("Oops!", "Wrong login.")

# Main app window
def open_main_window():
    def add():
        if not (n := name.get()) or not q.get().isdigit() or not p.get().replace('.','',1).isdigit():
            return messagebox.showerror("Oops", "Bad input")
        c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (n, int(q.get()), float(p.get())))
        conn.commit()
        load()

    def edit():
        sel = tree.focus()
        if not sel: return
        pid = tree.item(sel)['values'][0]
        new_q = simpledialog.askinteger("Qty", "New quantity?")
        new_p = simpledialog.askfloat("Price", "New price?")
        if new_q is not None and new_p is not None:
            c.execute("UPDATE products SET quantity=?, price=? WHERE id=?", (new_q, new_p, pid))
            conn.commit()
            load()

    def delete():
        sel = tree.focus()
        if not sel: return
        pid = tree.item(sel)['values'][0]
        c.execute("DELETE FROM products WHERE id=?", (pid,))
        conn.commit()
        load()

    def low_stock():
        top = tk.Toplevel(root); top.title("Low Stock")
        t = ttk.Treeview(top, columns=('ID','Name','Qty'), show='headings')
        for col in ('ID','Name','Qty'): t.heading(col, text=col)
        t.pack()
        for row in c.execute("SELECT id, name, quantity FROM products WHERE quantity < 5"):
            t.insert('', 'end', values=row)

    def summary():
        c.execute("SELECT COUNT(*), SUM(quantity), SUM(quantity * price) FROM products")
        a,b,cost = c.fetchone()
        messagebox.showinfo("Summary", f"Products: {a}\nItems: {b}\nValue: ${cost:.2f}")

    def load():
        for i in tree.get_children(): tree.delete(i)
        for row in c.execute("SELECT * FROM products"): tree.insert('', 'end', values=row)

    global root
    root = tk.Tk(); root.title("Inventory")
    name, q, p = tk.StringVar(), tk.StringVar(), tk.StringVar()

    tk.Entry(root, textvariable=name).pack()
    tk.Entry(root, textvariable=q).pack()
    tk.Entry(root, textvariable=p).pack()
    tk.Button(root, text="Add", command=add).pack()

    tree = ttk.Treeview(root, columns=('ID','Name','Qty','Price'), show='headings')
    for col in ('ID','Name','Qty','Price'): tree.heading(col, text=col)
    tree.pack()

    for t, f in [("Edit", edit), ("Delete", delete), ("Low Stock", low_stock), ("Summary", summary)]:
        tk.Button(root, text=t, command=f).pack(side='left', padx=5)

    load()
    root.mainloop()

# Login UI
login_win = tk.Tk(); login_win.title("Login")
tk.Label(login_win, text="User").grid(row=0, column=0)
user = tk.Entry(login_win); user.grid(row=0, column=1)
tk.Label(login_win, text="Pass").grid(row=1, column=0)
pwd = tk.Entry(login_win, show="*"); pwd.grid(row=1, column=1)
tk.Button(login_win, text="Login", command=login).grid(row=2, column=0, columnspan=2)
login_win.mainloop()
