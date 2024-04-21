import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

# GUI Window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.title("Sweep Pro")
window.geometry("350x500")
window.resizable(width=False, height=False)

# Styles
font_light_color = "#F9FFFC"
font_green_color = "#D3FD00"
font_family_bold = "Alte Haas Grotesk Bold"
font_family_normal = "Alte Haas Grotesk Normal"
bg_transparent = "transparent"

# Nav
logo = Image.open("core/interface/assets/img/logo.png")
logo = logo.resize((25, 25), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = ctk.CTkLabel(window, image=logo, fg_color="transparent", text="")
logo_label.place(relx=0.08, rely=0.05)

mode_icon_sun_src = PhotoImage(file="core/interface/assets/img/sun.png")
mode_icon_sun = mode_icon_sun_src.subsample(10, 10)
mode_icon_moon_src = PhotoImage(file="core/interface/assets/img/moon.png")
mode_icon_moon = mode_icon_moon_src.subsample(10, 10)
mode_icon_w = 10
mode_icon_h = 10

button_mode = ctk.CTkButton(
    master=window,
    width=mode_icon_w,
    height=mode_icon_h,
    text="",
    fg_color=bg_transparent,
    text_color=font_green_color,
    image=mode_icon_sun,
    hover=False,
)
button_mode.place(relx=0.81, rely=0.041)


# Title config
keep_x = 0.080
keep_y = 0.23
org_x = 0.080
org_y = 0.32
title_font_size = -43
title_font = (font_family_bold, title_font_size)

org_label = ctk.CTkLabel(
    window,
    text="organized",
    text_color=font_light_color,
    fg_color=bg_transparent,
    font=title_font,
)
keep_label = ctk.CTkLabel(
    window,
    text="Keep",
    text_color=font_light_color,
    fg_color=bg_transparent,
    font=title_font,
)
keep_label.place(relx=keep_x, rely=keep_y)
org_label.place(relx=org_x, rely=org_y)

# Step 1 config
step_one_title_x = 0.080
step_one_title_y = 0.45

step_one_title_label = ctk.CTkLabel(
    window,
    text="Step 1: Choose your folder",
    text_color=font_light_color,
    fg_color=bg_transparent,
    font=(font_family_normal, -13),
)
step_one_title_label.place(relx=step_one_title_x, rely=step_one_title_y)

# Button folder Config
folder_icon_src = PhotoImage(file="core/interface/assets/img/folder-icon.png")
folder_icon = folder_icon_src.subsample(25, 25)

button_folder_text = ctk.CTkButton(
    master=window,
    text="Selected: /Downloads/",
    fg_color=bg_transparent,
    text_color=font_green_color,
    image=folder_icon,
    hover=False,
    font=(font_family_normal, -13),
    cursor="cross",
)
button_folder_text.place(relx=0.40, rely=0.55, anchor=ctk.CENTER)

# Step 2 config
step_two_title_x = 0.080
step_two_title_y = 0.6

step_two_title_label = ctk.CTkLabel(
    window,
    text="Step 2: Run Sweep Pro",
    text_color=font_light_color,
    fg_color=bg_transparent,
    font=(font_family_normal, -13),
)
step_two_title_label.place(relx=step_two_title_x, rely=step_two_title_y)

# Button run Config
folder_icon_src = PhotoImage(file="core/interface/assets/img/play-icon.png")
folder_icon = folder_icon_src.subsample(6, 6)
folder_icon_w = 6
folder_icon_h = 6

button_run_text = ctk.CTkButton(
    master=window,
    width=folder_icon_w,
    height=folder_icon_h,
    text="",
    fg_color=bg_transparent,
    text_color=font_green_color,
    image=folder_icon,
    hover=False,
)
button_run_text.place(relx=0.2479, rely=0.75, anchor=ctk.CENTER)

# Run
window.mainloop()
