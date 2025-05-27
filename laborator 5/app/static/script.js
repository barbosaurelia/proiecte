// URL-ul de baza pentru rutele API (definit in Flask ca /items)
const API_URL = '/items';
// Variabila care retine daca suntem in modul de editare
let editMode = false;
// Retine denumirea produsului curent care se editeaza
let currentDenumire = null;
// Functie asincrona care incarca si afiseaza lista de produse din server (GET /items)
async function fetchItems() {
  const response = await fetch(API_URL);
  const data = await response.json();
  const table = document.getElementById('items-table');
  table.innerHTML = '';
  // Pentru fiecare produs primit, cream un rand in tabel
  data.data.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${item.denumire}</td>
      <td>${item.stoc}</td>
      <td>
        <button onclick="editItem('${item.denumire}', '${item.stoc}')">Editează</button>
        <button onclick="deleteItem('${item.denumire}')">Șterge</button>
      </td>
    `;
    table.appendChild(row);
  });
}
// Functie pentru salvarea unui produs nou sau actualizat
async function saveItem() {
   // Luam valorile din inputuri
  const denumire = document.getElementById('denumire').value.trim();
  const stoc = document.getElementById('stoc').value.trim();
  const message = document.getElementById('message');
// Verificam daca campurile sunt completate
  if (!denumire || !stoc) {
    message.textContent = "Completează toate câmpurile.";
    return;
  }
 // Obiectul pe care il trimitem catre server
  const payload = { denumire, stoc };
// Daca suntem in modul editare -> facem cerere PUT
  if (editMode) {
    const response = await fetch(`${API_URL}/${currentDenumire}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
// Afisam mesaj in functie de rezultat
    if (response.ok) {
      message.textContent = "Produs actualizat!";
    } else {
      message.textContent = "Eroare la actualizare!";
    }
 // Resetam modul editare
    editMode = false;
    currentDenumire = null;
    document.getElementById('cancel-btn').style.display = 'none';
  } else {
     // Daca suntem in modul adaugare -> facem cerere POST
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (response.status === 201) {
      message.textContent = "Produs adăugat!";
    } else {
      message.textContent = "Eroare la adăugare!";
    }
  }

  clearForm();
  fetchItems();
}
// Functie care pregateste formularul pentru editare
function editItem(denumire, stoc) {
  document.getElementById('denumire').value = denumire;
  document.getElementById('stoc').value = stoc;
  editMode = true;
  currentDenumire = denumire;
  document.getElementById('cancel-btn').style.display = 'inline';
}
// Functie care anuleaza editarea si reseteaza formularul
function cancelEdit() {
  clearForm();
  editMode = false;
  currentDenumire = null;
  document.getElementById('cancel-btn').style.display = 'none';
}
// Functie care goleste campurile din formular
function clearForm() {
  document.getElementById('denumire').value = '';
  document.getElementById('stoc').value = '';
}
// Functie care sterge un produs (DELETE /items/<denumire>)
async function deleteItem(denumire) {
  const message = document.getElementById('message');
  const response = await fetch(`${API_URL}/${denumire}`, { method: 'DELETE' });
 // Afisam mesaj in functie de rezultat
  if (response.ok) {
    message.textContent = "Produs șters!";
    fetchItems();
  } else {
    message.textContent = "Eroare la ștergere!";
  }
}

window.onload = fetchItems;
