import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { ToastService } from '../../services/toast.service';

import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule]
})
export class LoginComponent {
  username = '';
  password = '';

  constructor(private auth: AuthService, private router: Router, private toast: ToastService) {}

  async onSubmit() {
    try {
      await this.auth.login(this.username, this.password);
      this.toast.show('Inicio de sesión exitoso');
      this.router.navigate(['/tasks']);
    } catch {
      this.toast.show('Usuario o contraseña incorrectos');
    }
  }
}
