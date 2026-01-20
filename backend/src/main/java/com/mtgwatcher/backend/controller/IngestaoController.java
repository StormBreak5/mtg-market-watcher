package com.mtgwatcher.backend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mtgwatcher.backend.dto.IngestaoDTO;
import com.mtgwatcher.backend.service.CartaService;

@RestController
@RequestMapping("/api/ingestao")
public class IngestaoController {

    @Autowired
    private CartaService cartaService;

    @PostMapping
    public ResponseEntity<String> receberDados(@RequestBody IngestaoDTO dto) {
        try {
            cartaService.processarIngestao(dto);
            return ResponseEntity.ok("Dados processados com sucesso.");
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body("Erro ao processar: " + e.getMessage());
        }
    }
}
