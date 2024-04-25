import huffman
import sys
from tkinter import*
from tkinter import ttk
import tkinter.filedialog
path = tkinter.filedialog.askopenfile(mode="r",defaultextension=".txt")
h = huffman.HuffmanCoding(path.name)
def comp():
    

    w = Tk()
    fr = ttk.Frame(w, padding=150)
    fr.grid()

    with open(path.name, mode="r", encoding="UTF-8") as file:
        preview = file.read(25)
        content = file.read()
    frequency = huffman.HuffmanCoding.make_frequency_dict(any, content)

    ttk.Label(
        fr,
        text= "File preview (25 bytes): ",
        font="Monocraft"
    ).grid(row=0, column=0)


    ttk.Label(
        fr,
        text=preview,
        font=("Monocraft", 8),
    ).grid(row=1, column=0)

    ttk.Label(
        fr,
        text="Frequency of characters: ",
        font="Monocraft"
    ).grid(row=0, column=2)

    ttk.Label(
        fr,
        text="\n".join(str(x) for x in frequency.items()),
        font=("Monocraft", 9)
    ).grid(row = 1, column=2)




    output_path = h.compress()
    ttk.Label(
        fr,
        text="Compression succesful at\n" + output_path,
        font="Monocraft"
    ).grid(row=4, column=1)

    
def decomp():
    decom_path = h.decompress(h.compress())
    w = Tk()
    fr = ttk.Frame(
        w,
        padding=200
    )
    fr.grid()

    ttk.Label(
        fr,
        text="File decompression succesful at",
        font="Monocraft"
    ).grid(row=0, column=0)

    ttk.Label(
        fr,
        text=decom_path,
        font="Monocraft"
    ).grid(row=1, column=0)
    


root = Tk()
frame = ttk.Frame(
    root,
    padding=200)

frame.grid()

ttk.Label(
    frame,
    text= "File compresser",
    font="Monocraft"
).grid(row=0, column=0)

ttk.Button(
    frame,
    text= "Compress file",
    command=comp
    ).grid(column=0, row=1)

ttk.Button(
    frame,
    text="Decompress file",
    command=decomp
).grid(column=0, row=2)
root.mainloop()

