// Memuat data dari local storage saat halaman dimuat
document.addEventListener('DOMContentLoaded', loadTasks);

// Menambahkan tugas baru
function addTask() {
  const taskInput = document.getElementById('taskInput');
  const taskText = taskInput.value.trim();

  if (taskText) {
    const tasks = getTasksFromStorage();
    tasks.push({ text: taskText, completed: false });
    saveTasksToStorage(tasks);
    taskInput.value = '';
    renderTasks();
  }
}

// Mengambil daftar tugas dari localStorage
function getTasksFromStorage() {
  return JSON.parse(localStorage.getItem('tasks')) || [];
}

// Menyimpan daftar tugas ke localStorage
function saveTasksToStorage(tasks) {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Menghapus tugas 
function deleteTask(index) {
  const tasks = getTasksFromStorage();
  tasks.splice(index, 1);
  saveTasksToStorage(tasks);
  renderTasks();
}

// Menandai tugas yang sudah selesai atau belum selesai
function toggleTask(index) {
  const tasks = getTasksFromStorage();
  tasks[index].completed = !tasks[index].completed;
  saveTasksToStorage(tasks);
  renderTasks();
}

// Menampilkan daftar tugas dengan checkbox
function renderTasks() {
  const taskList = document.getElementById('taskList');
  taskList.innerHTML = ''; 
  const tasks = getTasksFromStorage();

  tasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.classList.add('flex', 'items-center', 'gap-4', 'cursor-pointer', 'hover:bg-gray-200', 'p-2', 'rounded');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.completed;
    checkbox.classList.add('mr-4');
    checkbox.addEventListener('change', () => toggleTask(index)); 

    const taskText = document.createElement('span');
    taskText.textContent = task.text;
    if (task.completed) {
      taskText.style.textDecoration = 'line-through';
      taskText.style.color = 'gray';
    }

    // Menambahkan tombol hapus list
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('ml-2', 'text-red-500');
    deleteButton.addEventListener('click', (e) => {
      e.stopPropagation();
      deleteTask(index);
    });

    // Notifikasi jika task selesai
    const completedMessage = document.createElement('span');
    completedMessage.textContent = task.completed ? ' Done!' : '';
    completedMessage.classList.add('text-green-500', 'ml-2', 'font-semibold');
    
    li.appendChild(checkbox);
    li.appendChild(taskText);
    li.appendChild(deleteButton);
    li.appendChild(completedMessage);

    taskList.appendChild(li);
  });
}

// Kalkulator
function hitungKalkulator(angka1, angka2, operasi) {
  switch (operasi) {
    case "tambah": return angka1 + angka2;
    case "kurang": return angka1 - angka2;
    case "kali": return angka1 * angka2;
    case "bagi": return angka2 !== 0 ? angka1 / angka2 : "Error: Pembagian dengan nol!";
    case "pangkat": return Math.pow(angka1, angka2 !== null ? angka2 : 2);
    case "akar": return angka1 >= 0 ? Math.sqrt(angka1) : "Error: Akar dari bilangan negatif!";
    case "modulus": return angka2 !== 0 ? angka1 % angka2 : "Error: Modulus dengan nol!";
    default: return "Operasi tidak valid";
  }
}

function tampilkanHasil(hasil) {
  document.getElementById("hasil-kalkulator").innerHTML = `Hasil: ${hasil}`;
}

function ambilNilaiInput(operasi) {
  const angka1 = parseFloat(document.getElementById("angka1").value);
  const angka2 = parseFloat(document.getElementById("angka2").value);

  if (operasi === 'akar' && isNaN(angka1)) {
    tampilkanHasil("Masukkan angka pertama yang valid!");
    return null;
  }

  if (operasi === 'pangkat' && isNaN(angka1)) {
    tampilkanHasil("Masukkan angka pertama yang valid!");
    return null;
  }

  if (operasi === 'modulus' && (isNaN(angka1) || isNaN(angka2))) {
    tampilkanHasil("Masukkan kedua angka yang valid!");
    return null;
  }

  return { angka1, angka2 };
}

const operasi = {
  tambah: "btn-tambah",
  kurang: "btn-kurang",
  kali: "btn-kali",
  bagi: "btn-bagi",
  pangkat: "btn-pangkat",
  akar: "btn-akar",
  modulus: "btn-modulus"
};

Object.keys(operasi).forEach(op => {
  document.getElementById(operasi[op]).addEventListener("click", function() {
    const input = ambilNilaiInput(op);
    if (input === null) return;

    let hasil = hitungKalkulator(input.angka1, input.angka2, op);
    tampilkanHasil(hasil);
  });
});

// Validasi Form
document.getElementById('formInput').addEventListener('submit', function(e) {
  e.preventDefault();
  let valid = true;
  let message = '';

  const nama = document.getElementById('nama').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  if (nama.length <= 3) {
    valid = false;
    message += 'Name must be more than 3 characters. ';
  }

  const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailPattern.test(email)) {
    valid = false;
    message += 'Email is invalid. ';
  }

  if (password.length < 8) {
    valid = false;
    message += 'Password must be at least 8 characters.';
  }

  document.getElementById('validasiHasil').textContent = message;

  if (valid) {
    alert('Formulir valid!');
  }
});
