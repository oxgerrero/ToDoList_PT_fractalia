import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private baseUrl = 'http://localhost:8000';
  private tokenKey = 'jwt';

  async login(username: string, password: string) {
    const res = await axios.post(`${this.baseUrl}/login`, new URLSearchParams({ username, password }));
    const token = res.data.access_token;
    localStorage.setItem(this.tokenKey, token);
  }

  async register(username: string, password: string) {
    await axios.post(`${this.baseUrl}/register`, { username, password });
  }

  logout() {
    localStorage.removeItem(this.tokenKey);
  }

  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }
}
