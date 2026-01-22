import { HttpClient } from '@angular/common/http';
import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { Carta } from '../models/carta.model';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CartaService {
  private apiUrl = 'http://localhost:8080/api/cartas';

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) private platformId: Object
  ) { }

  getCartas(): Observable<Carta[]> {
    // Se estiver no servidor (SSR), retorna array vazio
    // Os dados serão carregados no cliente
    if (!isPlatformBrowser(this.platformId)) {
      return of([]);
    }
    
    return this.http.get<Carta[]>(this.apiUrl);
  }
}
