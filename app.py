from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    a = float(data['a'])
    b = float(data['b'])
    op = data['operacion']

    if op == 'suma':
        resultado = a + b
    elif op == 'resta':
        resultado = a - b
    elif op == 'multiplicacion':
        resultado = a * b
    elif op == 'division':
        if b == 0:
            return jsonify({'error': 'División entre cero'}), 400
        resultado = a / b
    else:
        return jsonify({'error': 'Operación no válida'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run()