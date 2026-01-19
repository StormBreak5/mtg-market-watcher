package com.mtgwatcher.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.mtgwatcher.backend.entity.Carta;

public interface CartaRepository extends JpaRepository<Carta, Long> {

}