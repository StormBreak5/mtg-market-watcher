package com.mtgwatcher.backend.dto;

import java.math.BigDecimal;

import lombok.Data;

@Data
public class IngestaoDTO {
    private String nome;
    private String setCode;
    private String raridade;
    private BigDecimal precoUsd;
    private BigDecimal precoBrl;
    private BigDecimal precoEur;
    private BigDecimal precoTix;
}
