import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from services import get_user_data

def display_text_summary(user_id):
    df = get_dataframe(user_id)
    if df is None: return
    
    total_quizzes = len(df)
    total_correct = df['Score'].sum()
    total_wrong = (df['Total'] - df['Score']).sum()
    avg_score = df['Score'].mean()
    accuracy = (total_correct / (total_correct + total_wrong)) * 100 if (total_correct + total_wrong) > 0 else 0
    
    print(f"Total Quizzes Attempted: {total_quizzes}")
    print(f"Total Correct Answers  : {total_correct}")
    print(f"Total Wrong Answers    : {total_wrong}")
    print(f"Average Score          : {round(avg_score, 2)}")
    print(f"Overall Accuracy       : {round(accuracy, 2)}%")

def get_dataframe(user_id):
    raw_data = get_user_data(user_id)
    if not raw_data:
        print("\nNo attempts yet. Cannot generate graph.")
        return None   
    user_data = pd.DataFrame(raw_data, columns=["Name", "Score", "Total"])
    if len(user_data) == 0:
        print("\nNo data to display.")
        return None
    return user_data

def display_line_chart(user_id):
    try:
        df = get_dataframe(user_id)
        if df is None: return
            
        attempts = range(1, len(df) + 1)
        scores = df["Score"]
        
        plt.figure(figsize=(8, 5))
        plt.plot(attempts, scores, marker='o', linestyle='-', color='b')
        plt.title('Performance Over Time')
        plt.xlabel('Attempt #')
        plt.ylabel('Score')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error generating line chart: {e}")

def display_bar_chart(user_id):
    try:
        df = get_dataframe(user_id)
        if df is None: return
            
        attempts = range(1, len(df) + 1)
        corrects = df["Score"]
        wrongs = df["Total"] - df["Score"]
        x_pos = np.arange(len(attempts))
        
        plt.figure(figsize=(8, 5))
        # Stacked bar chart showing Correct and Wrong
        plt.bar(x_pos, corrects, color='#66b3ff', label='Correct')
        plt.bar(x_pos, wrongs, bottom=corrects, color='#ff9999', label='Wrong')
        plt.xticks(x_pos, attempts)
        plt.title('Correct vs Wrong per Attempt')
        plt.ylabel('Number of Questions')
        plt.xlabel('Attempt #')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error generating bar chart: {e}")

def display_pie_chart(user_id):
    try:
        df = get_dataframe(user_id)
        if df is None: return
            
        total_correct = df['Score'].sum()
        total_wrong = (df['Total'] - df['Score']).sum()
        
        labels = ['Total Correct', 'Total Wrong']
        sizes = [total_correct, total_wrong]
        colors = ['#66b3ff', '#ff9999']

        if total_correct > 0 or total_wrong > 0:
            plt.figure(figsize=(6, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
            plt.title('Overall Correct vs Wrong Ratio')
            plt.show()
        else:
            print("Not enough data to draw pie chart.")
    except Exception as e:
        print(f"Error generating pie chart: {e}")

def display_histogram(user_id):
    try:
        df = get_dataframe(user_id)
        if df is None: return
            
        scores = df["Score"]
        
        plt.figure(figsize=(8, 5))
        plt.hist(scores, bins=5, color='orange', edgecolor='black')
        plt.title('Score Distribution')
        plt.xlabel('Score Ranges')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error generating histogram: {e}")