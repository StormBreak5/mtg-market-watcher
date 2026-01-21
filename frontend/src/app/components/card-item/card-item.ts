import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Carta } from '../../models/carta.model';

@Component({
  selector: 'app-card-item',
  templateUrl: './card-item.html',
  styleUrl: './card-item.css',
  standalone: false
})
export class CardItem {
  @Input() carta!: Carta;
  @Output() cardClick = new EventEmitter<Carta>();

  onCardClick(): void {
    this.cardClick.emit(this.carta);
  }

  getRaridadeColor(raridade: string): string {
    const colors: { [key: string]: string } = {
      'mythic': 'warn',
      'rare': 'accent',
      'uncommon': 'primary',
      'common': ''
    };
    return colors[raridade.toLowerCase()] || '';
  }

  formatarPreco(valor: number | null): string {
    return valor ? valor.toFixed(2) : '---';
  }

  formatarData(data: string): string {
    return new Date(data).toLocaleDateString('pt-BR');
  }
}
