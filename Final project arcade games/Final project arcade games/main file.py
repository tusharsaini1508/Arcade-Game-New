import tkinter as tk
from tkinter import messagebox

def launch_game(choice):
    try:
        if choice == 1:
            import snake
        elif choice == 2:
            import flapy 
        elif choice == 3:
            import Chesss
        elif choice == 4:
            import snake_ladder
        elif choice == 5:
            import ludo
        elif choice == 6:
            import block_game    
    except ImportError:
        messagebox.showerror("Error", "Failed to launch game. Please make sure the game files are available.")
        
def create_buttons():
    root = tk.Tk()
    root.title("Arcade Gaming System")
    
    def on_button_click(choice):
        return lambda: launch_game(choice)
    
    games = [
        ("Snake Game", 1),
        ("Flappy Game", 2),
        ("Chess", 3),
        ("Snake Ladder", 4),
        ("Ludo Game", 5),
        ("Block Game", 6)  
    ]
    
    button_colors = [
        ("#3498db", "#ffffff"),  
        ("#27ae60", "#ffffff"),  
        ("#e74c3c", "#ffffff"),  
        ("#f39c12", "#ffffff"), 
        ("#8e44ad", "#ffffff"),
        ("#34495e", "#ffffff")  
    ]
    
    for idx, (game_name, game_choice) in enumerate(games):
        bg_color, fg_color = button_colors[idx]
      
        button = tk.Button(root, text=game_name, bg=bg_color, fg=fg_color, command=on_button_click(game_choice), font=("Arial", 20))
        button.pack(pady=10, ipady=10, ipadx=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_buttons()
