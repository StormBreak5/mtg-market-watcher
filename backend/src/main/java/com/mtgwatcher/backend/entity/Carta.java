package com.mtgwatcher.backend.entity;

import java.util.List;
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

    @OneToMany(mappedBy = "carta", cascade = CascadeType.ALL)
    @OrderBy("dataRegistro DESC")
    private List<HistoricoPreco> historicoPrecos;
}