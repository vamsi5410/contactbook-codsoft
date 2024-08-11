import tkinter as tk
from tkinter import messagebox

# Store contacts in a dictionary
contacts = {}

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone Number are required!")

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name}: {details['phone']}")

def search_contact():
    search_query = entry_search.get()
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        if search_query.lower() in name.lower() or search_query in details['phone']:
            listbox_contacts.insert(tk.END, f"{name}: {details['phone']}")

def update_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0].strip()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        
        if name in contacts:
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact {name} updated successfully!")
            clear_entries()
            view_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "No contact selected!")

def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0].strip()
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
            view_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "No contact selected!")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("450x550")
root.configure(bg='#f5f5f5')

# Create a frame for contact details input
frame_input = tk.Frame(root, bg='#ffffff', padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_input.pack(pady=20)

label_title = tk.Label(frame_input, text="Add / Update Contact", font=('Helvetica', 16, 'bold'), bg='#ffffff')
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Contact Entry Fields
label_name = tk.Label(frame_input, text="Name:", bg='#ffffff')
label_name.grid(row=1, column=0, sticky=tk.W, pady=5)
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=1, column=1, pady=5)

label_phone = tk.Label(frame_input, text="Phone Number:", bg='#ffffff')
label_phone.grid(row=2, column=0, sticky=tk.W, pady=5)
entry_phone = tk.Entry(frame_input, width=30)
entry_phone.grid(row=2, column=1, pady=5)

label_email = tk.Label(frame_input, text="Email:", bg='#ffffff')
label_email.grid(row=3, column=0, sticky=tk.W, pady=5)
entry_email = tk.Entry(frame_input, width=30)
entry_email.grid(row=3, column=1, pady=5)

label_address = tk.Label(frame_input, text="Address:", bg='#ffffff')
label_address.grid(row=4, column=0, sticky=tk.W, pady=5)
entry_address = tk.Entry(frame_input, width=30)
entry_address.grid(row=4, column=1, pady=5)

# Buttons for contact actions
button_add = tk.Button(frame_input, text="Add Contact", command=add_contact, width=15, bg='#4CAF50', fg='white')
button_add.grid(row=5, column=0, pady=10)

button_update = tk.Button(frame_input, text="Update Contact", command=update_contact, width=15, bg='#2196F3', fg='white')
button_update.grid(row=5, column=1, pady=10)

# Create a frame for the contact list and search
frame_list = tk.Frame(root, bg='#ffffff', padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_list.pack(pady=10)

label_search = tk.Label(frame_list, text="Search by Name or Phone:", bg='#ffffff')
label_search.grid(row=0, column=0, columnspan=2, pady=5)
entry_search = tk.Entry(frame_list, width=30)
entry_search.grid(row=1, column=0, pady=5)
button_search = tk.Button(frame_list, text="Search", command=search_contact, width=10, bg='#FF9800', fg='white')
button_search.grid(row=1, column=1, pady=5)

# Listbox for displaying contacts
listbox_contacts = tk.Listbox(frame_list, width=40, height=10)
listbox_contacts.grid(row=2, column=0, columnspan=2, pady=10)

button_view = tk.Button(frame_list, text="View All Contacts", command=view_contacts, width=20, bg='#9C27B0', fg='white')
button_view.grid(row=3, column=0, columnspan=2, pady=10)

button_delete = tk.Button(root, text="Delete Selected Contact", command=delete_contact, width=25, bg='#F44336', fg='white')
button_delete.pack(pady=20)

# Run the main event loop
root.mainloop()
