// Implementasi Class
// Class Task untuk data tugas
export class Task {
  constructor(id, name, deadline, status = false) {
    this.id = id;
    this.name = name;
    this.deadline = deadline;
    this.status = status;
  }
}
export class TaskManager {
  constructor() {
    //Mengambil data dari localStorage
    this.tasks = JSON.parse(localStorage.getItem('tasks')) || [];
  }

  //Menyimpan data ke localStorage
  save() {
    localStorage.setItem('tasks', JSON.stringify(this.tasks));
  }

  //Arrow Function Menambahkan tugas
  addTask = (task) => {
    this.tasks.push(task);
    this.save();
  }

  //Arrow Function #2 Mengedit tugas berdasarkan id
  editTask = (id, updatedTask) => {
    this.tasks = this.tasks.map(task => task.id === id ? updatedTask : task);
    this.save();
  }

  //Arrow Function Menghapus tugas berdasarkan id
  deleteTask = (id) => {
    this.tasks = this.tasks.filter(task => task.id !== id);
    this.save();
  }

  //Mengubah status tugas (selesai/belum)
  toggleStatus = (id) => {
    this.tasks = this.tasks.map(task => {
      if (task.id === id) task.status = !task.status;
      return task;
    });
    this.save();
  }

  getTasks = () => this.tasks;

  // Mengambil tugas terdekat berdasarkan deadline
  getNearestTasks = () => {
    return [...this.tasks].sort((a, b) => new Date(a.deadline) - new Date(b.deadline));
  }
}
