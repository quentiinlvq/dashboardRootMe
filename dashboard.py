import time
import webbrowser

import requests
from bs4 import BeautifulSoup

def get_user_data(username):
    url = f"https://www.root-me.org/{username}?lang=fr"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Utilisateur {username} non trouvé (Erreur 404).")
        return None
    elif response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        place_tag = soup.find('div', class_='tile')
        if place_tag:
            place = place_tag.find('h3').text.strip()

        points_tag = place_tag.find_all('div', class_='small-6 medium-3 columns text-center')[1]
        if points_tag:
            points = points_tag.find('h3').text.strip()
        else:
            points = "0"

        return {
            "Username": username,
            "Place": place,
            "Points": points
        }
    else:
        print(f"Erreur avec la page de l'utilisateur {username}: {response.status_code}")
        return None

def process_user_list(usernames):
    user_data_list = []

    for username in usernames:
        data = get_user_data(username)
        if data:
            user_data_list.append(data)

        time.sleep(1.1)

    return user_data_list


usernames = ["user1", "user2"]

user_data_list = process_user_list(usernames)


def get_points_value(user_data):
    try:
        return int(user_data["Points"])
    except ValueError:
        return 0

user_data_list_sorted = sorted(user_data_list, key=get_points_value, reverse=True)

def generate_html_table(user_data_list):
    html = """
    <html>
    <head>
        <style>
            table {
                width: 50%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 16px;
                text-align: left;
            }
            th, td {
                padding: 10px;
                border: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Scores des Utilisateurs</h2>
        <table>
            <tr>
                <th>Rang</th>
                <th>Utilisateur</th>
                <th>Place</th>
                <th>Points</th>
            </tr>
    """

    for idx, user_data in enumerate(user_data_list):
        rank = idx + 1
        html += f"""
        <tr>
            <td>{rank}</td>
            <td>{user_data['Username']}</td>
            <td>{user_data['Place']}</td>
            <td>{user_data['Points']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """
    return html

html_table = generate_html_table(user_data_list_sorted)

file_path = "user_scores.html"
with open(file_path, "w") as file:
    file.write(html_table)

webbrowser.open(file_path)

print("Tableau HTML généré et sauvegardé sous 'user_scores.html'")
