import { Component, OnInit, signal, Inject, PLATFORM_ID, AfterViewInit } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { CartaService } from './services/carta.service';
import { Carta } from './models/carta.model';
import { MatDialog } from '@angular/material/dialog';
import { PriceHistoryDialog } from './components/price-history-dialog/price-history-dialog';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  standalone: false,
  styleUrl: './app.css'
})
export class App implements OnInit, AfterViewInit {
  protected readonly title = signal('MTG Market Watcher');

  cartas = signal<Carta[]>([]);
  loading = signal<boolean>(true);
  error = signal<string | null>(null);

  constructor(
    private cartaService: CartaService,
    private dialog: MatDialog,
    @Inject(PLATFORM_ID) private platformId: Object
  ) { }

  ngOnInit(): void {
    // No SSR, não carrega dados inicialmente
    if (!isPlatformBrowser(this.platformId)) {
      this.loading.set(false);
      return;
    }
  }

  ngAfterViewInit(): void {
    // Carrega dados apenas no cliente (após hidratação)
    if (isPlatformBrowser(this.platformId)) {
      this.carregarCartas();
    }
  }

  carregarCartas(): void {
    this.loading.set(true);
    this.error.set(null);

    this.cartaService.getCartas().subscribe({
      next: (data) => {
        this.cartas.set(data);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Erro ao carregar cartas:', err);
        this.error.set('Erro ao carregar as cartas. Verifique se o backend está rodando.');
        this.loading.set(false);
      }
    });
  }

  abrirDetalhes(carta: Carta): void {
    this.dialog.open(PriceHistoryDialog, {
      data: carta,
      width: '800px',
      maxWidth: '95vw',
      panelClass: 'custom-dialog-container'
    });
  }
}
