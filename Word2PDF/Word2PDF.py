from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askdirectory
from docx2pdf import convert


def openfile():
    file = askopenfile(defaultextension=".doc",
                           filetypes=[(".docx", "*.docx"), ("Word Documents", "*.doc"), ("All Files", "*.*")])
    if file!=None:
        file_field.delete(0, END)
        file_field.insert(0, file.name)
    else:
        messagebox.showerror("Word2PDF", "Select the File")


def savefile():
    locationtosave = askdirectory()
    if len(locationtosave) != 0:
        file_dest_field.delete(0, END)
        file_dest_field.insert(0, locationtosave)
    else:
        messagebox.showerror("Word2PDF", "Select Destination of the File")


def convert2pdf():
    filename = file_name_field.get()

    if len(filename) != 0:
        destination = file_dest_field.get()
        source = file_field.get()
        dest = destination + "/" + filename + ".pdf"
        file_field.delete(0, END)
        file_dest_field.delete(0, END)
        file_name_field.delete(0, END)
        convert(source, dest)
        msg = "Succesfully Converted at Location : " + destination
        messagebox.showinfo("Word2PDF", msg)
    else:
        messagebox.showerror("Word2PDF", "Check the Details You have Entered")
        
def on_click(event):
    file_name_field.configure(state=NORMAL)
    file_name_field.delete(0, END)

    # make the callback only work once
    file_name_field.unbind('<Button-1>', on_click_id)
    btn2["state"] = NORMAL


if __name__ == "__main__":
    root = Tk()
    root.title("Word to PDF Converter")
    root.configure(bg="gray")
    root.minsize(width=585, height=300)
    root.maxsize(width=585, height=300)
    headlabel = Label(root, text="Word to PDF Converter",
                      bg="DeepSkyBlue", fg="black", font="none 10 bold")
    label1 = Label(root, text="\nSource :\n", bg="gray")
    label2 = Label(root, text="\nDestination :\n", bg="gray")
    label3 = Label(root, text="\nFile Name :\n", bg="gray")

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E", ipadx="30")
    label2.grid(row=2, column=0, sticky="E", ipadx="30")
    label3.grid(row=3, column=0, sticky="E", ipadx="30")

    file_field = Entry(root, bg="SlateGray", fg="white")
    file_dest_field = Entry(root, bg="SlateGray", fg="white")
    file_name_field = Entry(root, bg="white", fg="black")

    file_field.insert(0, "Click Browse And Select the File")
    file_dest_field.insert(0, "Click Browse And Select the destination")
    file_name_field.insert(0, "Enter Name of the File")
    on_click_id = file_name_field.bind('<Button-1>', on_click)
    file_name_field.configure(state=DISABLED)
    btn = Button(root, text="Browse", command=openfile, bg="teal", activebackground="black",
                 activeforeground="white")
    btn.grid(row=1, column=2, pady=5, padx=10)
    btn1 = Button(root, text="Browse", command=savefile, bg="teal", activebackground="black",
                  activeforeground="black")
    btn1.grid(row=2, column=2, pady=5, padx=10)
    btn2 = Button(root, text="Save", command=convert2pdf, bg="teal", activebackground="black",
                  activeforeground="black")
    btn2.grid(row=4, column=1, pady=5, padx=10)
    btn2["state"] = DISABLED
    file_field.grid(row=1, column=1, ipadx="100")
    file_dest_field.grid(row=2, column=1, ipadx="100")
    file_name_field.grid(row=3, column=1, ipadx="100")
    root.mainloop()
