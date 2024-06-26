from data_loading import load_data
from data_cleaning import clean_data
from data_transformation import transform_data
from data_visualization import (
    plot_total_goals,
    plot_most_successful_teams,
    plot_goal_difference_distribution,
    plot_top_goal_scorers,
    plot_goals_by_teams_over_time,
    plot_host_countries_performance,
    plot_average_goals_per_match,
    plot_match_results_heatmap
)


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
    plot_top_goal_scorers(players, 2014)  # Example for the year 2014
    plot_goals_by_teams_over_time(matches)
    plot_host_countries_performance(cups)
    plot_average_goals_per_match(cups)
    plot_match_results_heatmap(matches)


if __name__ == "__main__":
    main()
