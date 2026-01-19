package com.mtgwatcher.backend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mtgwatcher.backend.entity.Carta;
import com.mtgwatcher.backend.service.CartaService;

@RestController
@RequestMapping("/api/ingestao")
public class IngestaoController {

    @Autowired
    private CartaService cartaService;

    @PostMapping
    public ResponseEntity<String> receberDados(@RequestBody Carta carta) {
        try {
            Carta cartaSalva = cartaService.salvarOuAtualizar(carta);
            return ResponseEntity.ok("Carta salva com sucesso: " + cartaSalva.getNome());
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body("Erro ao processar: " + e.getMessage());
        }
    }
}
