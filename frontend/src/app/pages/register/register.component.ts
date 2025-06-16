import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { ToastService } from '../../services/toast.service';

import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule]
})
export class RegisterComponent {
  username = '';
  password = '';

  constructor(private auth: AuthService, private router: Router, private toast: ToastService) {}

  onSubmit() {
    const strong = /^(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(this.password);
    if (!strong) {
      this.toast.show('Contraseña no segura');
      return;
    }

    this.auth.register(this.username, this.password)
      .then(() => {
        this.toast.show('Usuario registrado');
        this.router.navigate(['/login']);
      })
      .catch(() => this.toast.show('Error al registrar'));
  }
}
