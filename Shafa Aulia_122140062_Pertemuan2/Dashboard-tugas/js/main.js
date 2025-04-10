//Mengimpor class
import { Task, TaskManager } from './app.js';

const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const dateInput = document.getElementById('task-date');
const taskList = document.getElementById('task-list');
const filter = document.getElementById('filter');

// Menggunakan let dan const 
const manager = new TaskManager();
let editId = null; 

// Template literals untuk rendering dinamis
const renderTasks = (tasks) => {
  taskList.innerHTML = '';
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.className = `task-item ${task.status ? 'done' : ''}`; // ← penggunaan template literals
    li.innerHTML = `
      <div class="info">
        <strong>${task.name}</strong>
        <div class="date">Deadline: ${task.deadline}</div>
      </div>
      <div>
        <button class="status" data-id="${task.id}">${task.status ? 'Belum' : 'Selesai'}</button>
        <button class="edit" data-id="${task.id}">Edit</button>
        <button class="delete" data-id="${task.id}">Hapus</button>
      </div>
    `;
    taskList.appendChild(li);
  });
};

//Menambah atau mengedit tugas
const handleAdd = (e) => {
  e.preventDefault();

  const name = input.value.trim();
  const deadline = dateInput.value;

  if (!name || !deadline) {
    alert("Nama tugas dan deadline harus diisi!");
    return;
  }

  if (editId) {
    const updatedTask = new Task(editId, name, deadline);
    manager.editTask(editId, updatedTask);
    editId = null;
  } else {
    const newTask = new Task(Date.now(), name, deadline);
    manager.addTask(newTask);
  }

  input.value = '';
  dateInput.value = '';
  renderTasks(manager.getTasks());
};

//Menghapus, mengedit, atau toggle status tugas
const handleClick = (e) => {
  const id = Number(e.target.dataset.id);

  if (e.target.classList.contains('delete')) {
    manager.deleteTask(id);
  } else if (e.target.classList.contains('edit')) {
    const task = manager.getTasks().find(t => t.id === id);
    if (task) {
      input.value = task.name;
      dateInput.value = task.deadline;
      editId = id;
    }
  } else if (e.target.classList.contains('status')) {
    manager.toggleStatus(id);
  }

  renderTasks(manager.getTasks());
};

//Filter daftar tugas
filter.addEventListener('change', () => {
  const selected = filter.value;
  const tasks = selected === 'nearest' ? manager.getNearestTasks() : manager.getTasks();
  renderTasks(tasks);
});

// menggunakan async/await untuk update waktu
const updateClock = async () => {
  const now = new Date();
  const time = now.toLocaleTimeString('id-ID');
  const date = now.toLocaleDateString('id-ID', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
  });

  document.getElementById('clock').textContent = time;
  document.getElementById('date').textContent = date;
};
setInterval(updateClock, 1000);
updateClock();

// Event listeners untuk interaksi pengguna
form.addEventListener('submit', handleAdd);
taskList.addEventListener('click', handleClick);

// Menampilkan daftar tugas awal
renderTasks(manager.getTasks());

localStorage.removeItem('tasks');
