"""
    C.Marriott
    FEB 2025
    Tools.py
"""
from customtkinter import *
from tkinter import filedialog as fd

root = CTk()
root.geometry("600x500")

main_font = ("Arial", 12, "bold")
title_font = ("Arial", 25, "bold")

settings = {
    "name": "C.Marriott"
}

"""
filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
"""


def ask_for_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    print(f"Selected file: {filename}")


# Create the UI for the comments page
def comment_page(page):
    main_frame = CTkFrame(page)
    main_frame.grid(row=0, column=0, padx=5, pady=5)

    comment_row = 0

    comment_main_label = CTkLabel(main_frame, text="Generate comments in files", font=("Arial", 25, "bold"))
    comment_main_label.grid(row=comment_row, column=0, padx=5, pady=5, sticky="nw")
    comment_row += 1

    comment_select_file = CTkButton(main_frame, text="Select file", font=("Arial", 12, "bold"))
    comment_select_file.grid(row=comment_row, column=0, padx=5, pady=5, sticky="nw")
    comment_row += 1

    comment_generate_button = CTkButton(main_frame, text="Generate comment", font=("Arial", 12, "bold"))
    comment_generate_button.grid(row=comment_row, column=0, padx=5, pady=5, sticky="nw")
    comment_row += 1

    comment_tmp_label = CTkLabel(main_frame, text="-"*20, font=("Arial", 12))
    comment_tmp_label.grid(row=comment_row, column=0, padx=5, pady=5)
    comment_row += 1

    comment_output_label = CTkLabel(main_frame, text="", font=("Arial", 12))
    comment_output_label.grid(row=comment_row, column=0, padx=5, pady=5)
    comment_row += 1


# Load all the pages into the tabview
def main():
    page_frame = CTkTabview(root)
    comments_frame = page_frame.add("CreateComments")

    comment_page(comments_frame)
    page_frame.pack()


main()
root.mainloop()