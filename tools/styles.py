# version 1.1.1 style utils

import os

def load_styles(app):
    
    # ===== Default Style Configuration =====
    
    default_style_name = "classic"
    current_style_name = default_style_name
        
    style_txt_path = os.path.join("data", "style.txt")
    
    # ===== Load style.txt =====
    
    file_data = []
    if os.path.exists(style_txt_path):
        try:
            with open(style_txt_path, "r", encoding="utf-8") as file:
                file_data = file.readlines()

            if len(file_data) < 10:
                print("Style file is missing data (less than 10 lines). Using default style.")

            else:
                
                available_styles = [s.strip().lower() for s in file_data[9].split("%")]
                candidate_style_from_line_5 = file_data[6].strip().lower()
                candidate_style_from_line_3 = file_data[3].strip().lower()

                if candidate_style_from_line_5 in available_styles:
                    current_style_name = candidate_style_from_line_5
                elif candidate_style_from_line_3 in available_styles:
                    current_style_name = candidate_style_from_line_3
                else:
                    print(f"Specified styles from style.txt (line 5/3) not found in available styles (line 10). Using default style: '{default_style_name}'.")

        except Exception as e:
            print(f"Error reading or parsing style.txt: {e}. Using default style.")

    else:
        print("style.txt not found. Using default style.")

    # ===== Load stylesheet =====
    
    style_file_path = os.path.join("data", "styles", f"{current_style_name}.qss")

    try:
        with open(style_file_path, "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())
            print(f"Loaded style: {current_style_name}")
    except FileNotFoundError:
        print(f"Style file not found: {style_file_path}. Falling back to empty stylesheet.")
        app.setStyleSheet("") 
    except Exception as e:
        print(f"An unexpected error occurred while loading stylesheet '{style_file_path}': {e}. Falling back to empty stylesheet.")
        app.setStyleSheet("") 