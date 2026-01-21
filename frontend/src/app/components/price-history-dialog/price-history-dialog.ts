import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Carta } from '../../models/carta.model';

@Component({
  selector: 'app-price-history-dialog',
  templateUrl: './price-history-dialog.html',
  styleUrl: './price-history-dialog.css',
  standalone: false
})
export class PriceHistoryDialog {
  constructor(
    public dialogRef: MatDialogRef<PriceHistoryDialog>,
    @Inject(MAT_DIALOG_DATA) public carta: Carta
  ) { }

  onClose(): void {
    this.dialogRef.close();
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
    return new Date(data).toLocaleDateString('pt-BR') + ' ' + new Date(data).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
  }
}
