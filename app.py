
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/decyzja', methods=['GET'])
def decyzja():
    try:
        wiek = int(request.args.get('wiek'))
        pensja = float(request.args.get('pensja'))
    except (TypeError, ValueError):
        return jsonify({"error": "Nieprawidłowe dane wejściowe"}), 400

    if wiek > 18 and pensja > 4000:
        wynik = "TAK"
    else:
        wynik = "NIE"

    return jsonify({
        "wiek": wiek,
        "pensja": pensja,
        "decyzja": wynik
    })

if __name__ == '__main__':
    app.run(debug=True)
