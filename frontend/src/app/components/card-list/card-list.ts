import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Carta } from '../../models/carta.model';

@Component({
  selector: 'app-card-list',
  templateUrl: './card-list.html',
  styleUrl: './card-list.css',
  standalone: false
})
export class CardList {
  @Input() cartas: Carta[] = [];
  @Output() cardSelected = new EventEmitter<Carta>();

  onCardClick(carta: Carta): void {
    this.cardSelected.emit(carta);
  }
}
