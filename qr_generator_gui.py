import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Missing Input", "Please enter text or a URL to generate the QR code.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("temp_qr.png")

    # Display the QR code in the window
    qr_img = Image.open("temp_qr.png")
    qr_img = qr_img.resize((200, 200))  # Resize to fit the window
    img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    # Ask where to save
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Saved", f"QR code saved as:\n{save_path}")

# Create the GUI window
root = tk.Tk()
root.title("QR Code Generator 🧠📱")
root.geometry("400x400")

# Input field
label = tk.Label(root, text="Enter text or URL:", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Helvetica", 12))
entry.pack(pady=5)

# Generate button
button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Helvetica", 12), bg="black", fg="white")
button.pack(pady=10)

# Image preview
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
