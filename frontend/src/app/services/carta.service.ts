import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Carta } from '../models/carta.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CartaService {
  private apiUrl = 'http://localhost:8080/api/cartas';

  constructor(private http: HttpClient) { }

  getCartas(): Observable<Carta[]> {
    return this.http.get<Carta[]>(this.apiUrl);
  }
}
