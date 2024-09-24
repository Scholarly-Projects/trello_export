import requests
import csv
import os

# API Key and Token (replace with your API info)
API_KEY = 'your_api_key'
API_TOKEN = 'your_api_token'
BOARD_ID = 'your_board_id'

# Trello API URL
BASE_URL = 'https://api.trello.com/1'

# Get all cards from a specific board
def get_archived_cards(board_id):
    url = f"{BASE_URL}/boards/{board_id}/cards"
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'filter': 'closed',  # 'closed' means archived cards
    }
    response = requests.get(url, params=query)
    return response.json()

# Create CSV for each label
def export_cards_by_label(cards):
    label_card_map = {}
    
    # Organize cards by labels
    for card in cards:
        archived_date = card.get('dateLastActivity', 'Unknown date')
        card_labels = card.get('labels', [])
        
        # If no labels, skip
        if not card_labels:
            continue
        
        for label in card_labels:
            label_name = label.get('name', 'Unknown label')
            if label_name not in label_card_map:
                label_card_map[label_name] = []
            label_card_map[label_name].append({
                'name': card['name'],
                'desc': card.get('desc', 'No description'),
                'archived_date': archived_date
            })
    
    # Create directory for CSVs
    if not os.path.exists('trello_exports'):
        os.makedirs('trello_exports')

    # Export each label's cards to CSV
    for label, cards in label_card_map.items():
        filename = f"trello_exports/{label}_cards.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'desc', 'archived_date'])
            writer.writeheader()
            for card in cards:
                writer.writerow(card)
        print(f"Exported {len(cards)} cards to {filename}")

# Main Function
def main():
    print("Fetching archived cards from Trello...")
    cards = get_archived_cards(BOARD_ID)
    
    if not cards:
        print("No archived cards found.")
        return

    print(f"Found {len(cards)} archived cards. Exporting by label...")
    export_cards_by_label(cards)
    print("Export completed.")

if __name__ == "__main__":
    main()