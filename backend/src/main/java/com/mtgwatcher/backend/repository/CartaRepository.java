package com.mtgwatcher.backend.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.mtgwatcher.backend.entity.Carta;

public interface CartaRepository extends JpaRepository<Carta, Long> {

    Optional<Carta> findByNome(String nome);

}