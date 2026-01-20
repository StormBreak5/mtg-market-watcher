package com.mtgwatcher.backend.entity;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "historico_preco")
public class HistoricoPreco {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private BigDecimal valorUsd;
    private BigDecimal valorBrl;
    private BigDecimal valorEur;
    private BigDecimal valorTix;
    private LocalDateTime dataRegistro;

    @ManyToOne
    @JoinColumn(name = "carta_id", nullable = false)
    @JsonIgnore
    private Carta carta;
}
