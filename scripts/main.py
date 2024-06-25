from data_loading import load_data
from data_cleaning import clean_data
from data_transformation import transform_data
from data_visualization import plot_total_goals, plot_most_successful_teams, plot_goal_difference_distribution

def main():
    # Load data
    matches, players, cups = load_data()
    
    # Clean data
    matches, players, cups = clean_data(matches, players, cups)
    
    # Transform data
    matches, total_goals_per_cup, winning_teams = transform_data(matches, players, cups)
    
    # Visualize data
    plot_total_goals(total_goals_per_cup)
    plot_most_successful_teams(winning_teams)
    plot_goal_difference_distribution(matches)

if __name__ == "__main__":
    main()
