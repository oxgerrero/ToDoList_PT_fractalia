import { Injectable } from '@angular/core';
import axios from 'axios';
import { AuthService } from './auth.service';

@Injectable({ providedIn: 'root' })
export class TaskService {
  private baseUrl = 'http://localhost:8000/tasks';

  constructor(private auth: AuthService) {
    axios.interceptors.request.use((config) => {
      const token = this.auth.getToken();
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });
  }

  getTasks() {
    return axios.get(this.baseUrl);
  }

  createTask(title: string, description = '') {
    return axios.post(this.baseUrl, { title, description });
  }

  toggleTask(id: number, completed: boolean) {
    return axios.put(`${this.baseUrl}/${id}`, { completed });
  }

  deleteTask(id: number) {
    return axios.delete(`${this.baseUrl}/${id}`);
  }
}
