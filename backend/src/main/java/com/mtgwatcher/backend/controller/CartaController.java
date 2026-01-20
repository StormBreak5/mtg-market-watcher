package com.mtgwatcher.backend.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.mtgwatcher.backend.entity.Carta;
import com.mtgwatcher.backend.repository.CartaRepository;

@RestController
@RequestMapping("/api/cartas")
@CrossOrigin(origins = "*")
public class CartaController {

    @Autowired
    private CartaRepository repository;

    @GetMapping
    public List<Carta> listarTodas() {
        return repository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Carta> buscarPorId(@PathVariable Long id) {
        return repository.findById(id)
                .map(carta -> ResponseEntity.ok(carta))
                .orElse(ResponseEntity.notFound().build());
    }
}
