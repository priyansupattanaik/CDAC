import csv
from validators import validate_answer

def start_quiz():
    score = 0
    total = 0
    
    print("\n" + "="*30)
    print("         STARTING QUIZ         ")
    print("="*30)
    
    try:
        with open("questions.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            
            for row in reader:
                if not row or len(row) < 6: continue
                    
                total += 1
                question_text = row[0]
                options = row[1:5]
                correct_answer = row[5]
                
                clean_question = question_text.lstrip('1234567890. ')
                print(f"\nQ{total}: {clean_question}")
                
                for i, opt in enumerate(options, 1):
                    print(f"  {i}. {opt.strip()}")
                
                while True:
                    choice_str = input("Enter option number (1-4): ")
                    # Regex Validation requirement
                    if validate_answer(choice_str):
                        choice = int(choice_str)
                        break
                    else:
                        print("Invalid input. Please enter exactly one digit from 1 to 4.")
                
                selected_option = options[choice - 1].strip()
                if selected_option == correct_answer.strip():
                    score += 1
                    
        print("\n" + "="*30)
        return score, total
        
    except Exception as e:
        print(f"\nAn error occurred while reading the quiz: {e}")
        return 0, 0

def export_result_to_csv(username, email, score, total):
    # Requirement: Create CSV Output
    try:
        with open("results.csv", "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write row to CSV to fulfill dataset creation requirement
            writer.writerow([username, email, score, total])
    except Exception as e:
        print(f"Error exporting to CSV: {e}")