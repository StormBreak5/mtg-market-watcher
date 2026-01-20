export interface HistoricoPreco {
    id: number;
    valorUsd: number;
    valorBrl: number;
    valorEur: number;
    valorTix: number;
    dataRegistro: string;
}

export interface Carta {
    id: number;
    nome: string;
    setCode: string;
    raridade: string;
    historicoPrecos: HistoricoPreco[];
}