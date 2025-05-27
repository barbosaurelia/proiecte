# routes.py
from flask import Blueprint, jsonify, request
# Importam functiile de manipulare a datelor din fisierul items.py din folderul services
from ..services.items import get_items , get_item , save_item, edit_item, delete_item
# Cream un blueprint numit 'items' pentru a grupa rutele legate de obiecte (produse)
items = Blueprint('items', __name__)
# Ruta pentru /items - suporta GET si POST
@items.route('/', methods=['GET', 'POST'])
def home():
    # Daca se face o cerere GET -> returnam toate obiectele din JSON
    if request.method == 'GET':
        data = get_items()
        return jsonify({'data': data}), 200
    # Daca se face o cerere POST -> salvam un nou obiect trimis in corpul cererii
    if request.method == 'POST':
        data = request.get_json()
        save_item(data)
        return jsonify({'data':'success'}), 201

# Ruta pentru /items/<denumire> - suporta GET, PUT si DELETE
@items.route('/<string:denumire>', methods = ['GET', 'PUT', "DELETE"])
def disp(denumire):
    # Cautam obiectul dupa denumire
    item = get_item(denumire)
    if item is None:
        return jsonify({'data': "Not found"}), 404
    if request.method == "GET":
        return jsonify({'data': item}), 200
    if request.method == "PUT":
        data = request.get_json()
        edit_item(denumire, data)
        return jsonify({'data':'success'}), 200
    if request.method == "DELETE":
        delete_item(denumire)
        return jsonify({'data':'success'}), 200


