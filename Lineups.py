import requests
import pandas as pd


def get_lineup(game_pk):
    url = f"https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error retrieving game {game_pk}")
        return None

    data = response.json()

    def extract_players(team_data):
        players = []
        for player_id, p in team_data['players'].items():
            if 'battingOrder' in p:
                players.append({
                    'name': p['person']['fullName'],
                    'position': p['position']['abbreviation'],
                    'batting_order': p['battingOrder'],
                    'team': team_data['team']['name']
                })
        return players

    home_lineup = extract_players(data['teams']['home'])
    away_lineup = extract_players(data['teams']['away'])

    return home_lineup + away_lineup

lineup = get_lineup(745907)
print(lineup)