package com.mtgwatcher.backend.service;

import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mtgwatcher.backend.entity.Carta;
import com.mtgwatcher.backend.repository.CartaRepository;

@Service
public class CartaService {

    @Autowired
    private CartaRepository repository;

    public Carta salvarOuAtualizar(Carta carta) {
        if (carta.getDataColeta() == null) {
            carta.setDataColeta(LocalDateTime.now());
        }

        return repository.save(carta);
    }
}
