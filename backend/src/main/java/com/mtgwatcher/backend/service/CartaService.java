package com.mtgwatcher.backend.service;

import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.mtgwatcher.backend.dto.IngestaoDTO;
import com.mtgwatcher.backend.entity.Carta;
import com.mtgwatcher.backend.entity.HistoricoPreco;
import com.mtgwatcher.backend.repository.CartaRepository;
import com.mtgwatcher.backend.repository.HistoricoPrecoRepository;

@Service
public class CartaService {

    @Autowired
    private CartaRepository cartaRepository;

    @Autowired
    private HistoricoPrecoRepository historicoPrecoRepository;

    @Transactional
    public void processarIngestao(IngestaoDTO dto) {// 1. Busca a carta no banco ou cria uma nova
        Carta carta = cartaRepository.findByNome(dto.getNome())
                .orElseGet(() -> criarNovaCarta(dto));

        // 2. Cria o registro de histórico de preço
        HistoricoPreco historico = new HistoricoPreco();
        historico.setCarta(carta);
        historico.setDataRegistro(LocalDateTime.now());
        historico.setValorUsd(dto.getPrecoUsd());
        historico.setValorBrl(dto.getPrecoBrl());

        // 3. Salva o histórico
        historicoPrecoRepository.save(historico);

        System.out.println("💰 Preço atualizado para: " + carta.getNome());
    }

    private Carta criarNovaCarta(IngestaoDTO dto) {
        Carta novaCarta = new Carta();
        novaCarta.setNome(dto.getNome());
        novaCarta.setSetCode(dto.getSetCode());
        novaCarta.setRaridade(dto.getRaridade());

        return cartaRepository.save(novaCarta);
    }
}
