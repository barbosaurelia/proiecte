from flask import Flask, render_template
from app.routes.items import items
# Cream aplicatia Flask si specificam unde se afla folderele pentru sabloane HTML si fisiere statice (JS, CSS)
app = Flask(
    __name__,
    template_folder='app/templates',  # locația pentru HTML
    static_folder='app/static'        # locația pentru JS/CSS
)
# Inregistram blueprint-ul 'items' care gestioneaza rutele de tip /items
app.register_blueprint(items, url_prefix='/items')
# Definim ruta principala '/' care returneaza pagina index.html
@app.route('/')
def index():
    return render_template('index.html')

# Daca acest fisier este rulat direct, pornim serverul Flask cu modul de debug activat
if __name__ == '__main__':
    app.run(debug=True)
