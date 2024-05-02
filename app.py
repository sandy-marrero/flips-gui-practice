import subprocess
import tkinter as tk
from tkinter import filedialog
import os
import sys

def apply_ips_patch():
    rom_file_path = rom_file_path_entry.get()
    ips_patch_file_path = ips_patch_file_path_entry.get()

    if not rom_file_path or not ips_patch_file_path:
        result_label.config(text="Please select both ROM and IPS Patch files")
        return

    if getattr(sys, 'frozen', False):
        flips_executable = os.path.join(sys._MEIPASS, 'flips.exe')
    else:
        flips_executable = 'flips.exe' 

    original_file_name = os.path.basename(rom_file_path)
    patched_rom_file_name = f"patched_{original_file_name}"
    patched_rom_file_path = os.path.join(os.path.dirname(rom_file_path), patched_rom_file_name)

    try:
        subprocess.run([flips_executable, '--apply', ips_patch_file_path, rom_file_path, patched_rom_file_path], check=True)
        result_label.config(text=f"Patch applied successfully to {rom_file_path}")
        result_label.config(text=f"Patched ROM saved as {patched_rom_file_path}")
    except subprocess.CalledProcessError:
        result_label.config(text="Error applying the patch")

app = tk.Tk()
app.title("IPS Patcher")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="IPS Patcher", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

rom_label = tk.Label(frame, text="Select ROM file:")
rom_label.grid(row=1, column=0, sticky="w")

rom_file_path_entry = tk.Entry(frame, width=30)
rom_file_path_entry.grid(row=1, column=1, padx=10, pady=10)

rom_button = tk.Button(frame, text="Browse", command=lambda: rom_file_path_entry.insert(0, filedialog.askopenfilename(title="Select ROM file", filetypes=[("ROM Files", "*.smc *.gba *.gbc")])))
rom_button.grid(row=1, column=2)

ips_label = tk.Label(frame, text="Select IPS Patch file:")
ips_label.grid(row=2, column=0, sticky="w")

ips_patch_file_path_entry = tk.Entry(frame, width=30)
ips_patch_file_path_entry.grid(row=2, column=1, padx=10, pady=10)

ips_button = tk.Button(frame, text="Browse", command=lambda: ips_patch_file_path_entry.insert(0, filedialog.askopenfilename(title="Select IPS Patch file", filetypes=[("IPS Files", "*.ips")])))
ips_button.grid(row=2, column=2)

patch_button = tk.Button(frame, text="Apply IPS Patch", command=apply_ips_patch)
patch_button.grid(row=3, column=0, columnspan=3, pady=10)

result_label = tk.Label(frame, text="", padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=3)

app.mainloop()
