# Import library
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import requests
from bs4 import BeautifulSoup

# Setup Flask app
app = Flask(__name__)

# Setup Twilio account credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Define message handling route
@app.route('/botwa', methods=['POST'])
def botwa():
    # Get incoming message
    incoming_msg = request.values.get('Body', '').lower()

    # Set recipient phone number and message
    resp = MessagingResponse()
    msg = resp.message()

    # Check for specific message and respond accordingly
    if 'hallo bot ganteng' in incoming_msg:
        msg.body('👋Hallo Juga Userku yang kucintai \' ༼ つ ◕_◕ ༽つ\'\n\nSilakan gunakan perintah berikut:\n1. Cariin Aku Foto (apapun foto yg ingin dicari)\n2. Kerjain PR Matematika ku dong\n3. Tolong Bersihin kamarku yaa 😘')
        # tambah preview
        msg.media('https://example.com/preview.jpg')
    elif 'cariin aku foto' in incoming_msg:
        # Get search query
        search_query = incoming_msg.split('cariin aku foto ')[1]

        # Perform search
        search_url = f'https://www.google.com/search?q={search_query}&tbm=isch'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')

        # Get image URL and send response
        img_url = img_tags[0]['src']
        msg.media(img_url)
    elif 'kerjain pr matematika' in incoming_msg:
        msg.body('Maaf, saya tidak bisa membantu mengerjakan PR Anda. Anda bisa mencari bantuan dari teman atau guru.')
    elif 'tolong bersihin kamarku' in incoming_msg:
        msg.body('Maaf, saya adalah program dan tidak bisa membersihkan kamar Anda. Mohon bersihkan kamar Anda sendiri atau minta bantuan dari orang lain.')
    else:
        msg.body('Maaf, saya tidak mengerti pesan Anda. Silakan gunakan perintah berikut:\n\n1. Cariin Aku Foto (apapun foto yg ingin dicari)\n2. Kerjain PR Matematika ku dong\n3. tolong Bersihin kamarku yaa 😘')

    return str(resp)

if __name__ == '__main__':
    app.run()
