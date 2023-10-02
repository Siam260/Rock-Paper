from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game choices
CHOICES = ['rock', 'paper', 'scissors']
WIN_CONDITIONS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

@app.route('/')
def home():
    return render_template('rps.html')

@app.route('/play', methods=['POST'])
def play_game():
    data = request.json
    player_choice = data.get('choice').lower()
    
    if player_choice not in CHOICES:
        return jsonify({'error': 'Invalid choice'}), 400
    
    computer_choice = random.choice(CHOICES)
    
    if player_choice == computer_choice:
        result = 'tie'
    elif WIN_CONDITIONS[player_choice] == computer_choice:
        result = 'win'
    else:
        result = 'lose'
    
    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)