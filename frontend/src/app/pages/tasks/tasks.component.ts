import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { ToastService } from '../../services/toast.service';

import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class TasksComponent implements OnInit {
  tasks: any[] = [];
  newTitle = '';
  newDesc = '';

  constructor(private taskService: TaskService, private toast: ToastService) {}

  ngOnInit() {
    this.loadTasks();
  }

  async loadTasks() {
    const res = await this.taskService.getTasks();
    this.tasks = res.data;
  }

  async addTask() {
    if (!this.newTitle.trim()) return;
    await this.taskService.createTask(this.newTitle, this.newDesc);
    this.toast.show('Tarea creada');
    this.newTitle = '';
    this.newDesc = '';
    this.loadTasks();
  }

  async toggle(task: any) {
    const confirmed = confirm(`¿Marcar como ${task.completed ? 'incompleta' : 'completada'}?`);
    if (!confirmed) return;
    await this.taskService.toggleTask(task.id, !task.completed);
    this.toast.show('Tarea actualizada');
    this.loadTasks();
  }

  async delete(id: number) {
    const confirmed = confirm('¿Estás seguro de eliminar esta tarea?');
    if (!confirmed) return;
    await this.taskService.deleteTask(id);
    this.toast.show('Tarea eliminada');
    this.loadTasks();
  }
}
