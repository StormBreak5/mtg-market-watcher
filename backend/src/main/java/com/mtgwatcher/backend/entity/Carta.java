package com.mtgwatcher.backend.entity;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "cartas")
public class Carta {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private String setCode;
    private String raridade;
    private BigDecimal precoUsd;
    private BigDecimal precoEur;
    private BigDecimal precoTix;

    private LocalDateTime dataColeta;
}