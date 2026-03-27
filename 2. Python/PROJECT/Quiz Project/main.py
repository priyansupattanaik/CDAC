from services import register, login, save_result, update_password, delete_account
from quiz import start_quiz, export_result_to_csv
from analytics import display_line_chart, display_bar_chart, display_pie_chart, display_histogram, display_text_summary
import db  # Auto-creates tables on import

def main():
    while True:
        try:
            print("\n" + "="*40)
            print("         WELCOME TO QUIZ SYSTEM         ")
            print("="*40)
            print("1. Register a new account")
            print("2. Login to existing account")
            print("3. Exit the application")
            print("="*40)
            
            choice = input("Enter choice (1-3): ")
            
            if choice == "1":
                register()
                
            elif choice == "2":
                quiz_user = login() # Retrieves the instantiated OOP Object
                
                if quiz_user:
                    while True:
                        print("\n" + "="*30)
                        # Requirement: Polymorphism execution
                        quiz_user.display_info()
                        
                        # Using a dictionary to pass parameters across the class (Requirement: Dictionaries)
                        stats_dict = {"total_quizzes": 1}
                        quiz_user.load_stats_from_dict(stats_dict)

                        print("="*30)
                        print("1. Take a Quiz")
                        print("2. View Analytics Menu")
                        print("3. Change Password")
                        print("4. Delete Account")
                        print("5. Logout")
                        print("="*30)
                        
                        opt = input("Enter choice (1-5): ")
                        
                        if opt == "1":
                            score, total = start_quiz()
                            if total > 0:
                                correct = score
                                wrong = total - score
                                print(f"\n=== QUIZ COMPLETED ===")
                                print(f"Correct Answers : {correct}")
                                print(f"Wrong Answers   : {wrong}")
                                print(f"Total Questions : {total}")
                                print(f"Final Score     : {correct}/{total}")
                                
                                # DB Save (CRUD Create Requirement)
                                save_result(quiz_user.user_id, score, total)
                                
                                # CSV Save (Dataset Output Requirement)
                                export_result_to_csv(quiz_user.username, quiz_user.email, score, total)
                        
                        elif opt == "2":
                            # Submenu for analytics metric selection
                            while True:
                                print("\n" + "="*30)
                                print("      ANALYTICS SUMMARY      ")
                                print("="*30)
                                display_text_summary(quiz_user.user_id)
                                print("\n--- DETAILED GRAPHS ---")
                                print("1. Performance Over Time")
                                print("2. Correct vs Wrong per Attempt")
                                print("3. Overall Correct vs Wrong Ratio")
                                print("4. Score Distribution")
                                print("5. Go Back")
                                
                                an_opt = input("Enter choice (1-5): ")
                                if an_opt == "1":
                                    display_line_chart(quiz_user.user_id)
                                elif an_opt == "2":
                                    display_bar_chart(quiz_user.user_id)
                                elif an_opt == "3":
                                    display_pie_chart(quiz_user.user_id)
                                elif an_opt == "4":
                                    display_histogram(quiz_user.user_id)
                                elif an_opt == "5":
                                    break
                                else:
                                    print("Invalid choice. Try again.")
                        
                        elif opt == "3":
                            # DB Update (CRUD Update Requirement)
                            update_password(quiz_user)
                            
                        elif opt == "4":
                            # DB Delete (CRUD Delete Requirement)
                            if delete_account(quiz_user.user_id):
                                print(f"Logging out abruptly. Goodbye {quiz_user.name}.")
                                break # Returns back to root level menu
                            
                        elif opt == "5":
                            print(f"\nLogging out... Goodbye {quiz_user.name}!")
                            break
                        
                        else:
                            print("\nInvalid choice! Please select an option from 1 to 5.")
            
            elif choice == "3":
                print("\nExiting the Quiz System... Thank you and Goodbye!")
                break
            
            else:
                print("\nInvalid choice! Please select an option from 1 to 3.")
        
        except Exception as e:
            # Exception Requirement: Explicitly wrapping the entire main block
            print(f"An unexpected critical error occurred: {e}")

if __name__ == "__main__":
    main()