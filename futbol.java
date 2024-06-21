package com.mycompany.ejercicio1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

import gestionmundial.Equipo;
import gestionmundial.Estadio;
import gestionmundial.Grupo;
import gestionmundial.Jugador;
import gestionmundial.Mundial;
import gestionmundial.Partido;

public class Main extends JFrame {
    private List<Jugador> jugadores;
    private List<Equipo> equipos;
    private List<Estadio> estadios;
    private List<Grupo> grupos;

    private JTextField entryJugadorNombre, entryJugadorEdad, entryJugadorPosicion;
    private JTextField entryEquipoNombre, entryEquipoEntrenador;
    private JComboBox<String> comboboxEquipo, comboboxJugador;
    private JTextField entryEstadioNombre, entryEstadioCiudad, entryEstadioCapacidad;
    private JTextField entryGrupoNombre;
    private JComboBox<String> comboboxGrupo, comboboxEquipoGrupo;

    public Main() {
        jugadores = new ArrayList<>();
        equipos = new ArrayList<>();
        estadios = new ArrayList<>();
        grupos = new ArrayList<>();
        initComponents();
    }

    private void initComponents() {
        setTitle("Sistema de Gestión de Mundial");
        setLayout(new GridLayout(30, 2));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(Color.lightGray);

        // Widgets para registrar jugadores
        add(new JLabel("Registrar Jugador"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryJugadorNombre = new JTextField();
        add(entryJugadorNombre);

        add(new JLabel("Edad:"));
        entryJugadorEdad = new JTextField();
        add(entryJugadorEdad);

        add(new JLabel("Posición:"));
        entryJugadorPosicion = new JTextField();
        add(entryJugadorPosicion);

        JButton btnRegistrarJugador = new JButton("Registrar Jugador");
        btnRegistrarJugador.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarJugador();
            }
        });
        add(btnRegistrarJugador);
        add(new JLabel(""));

        // Widgets para registrar equipos
        add(new JLabel("Registrar Equipo"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryEquipoNombre = new JTextField();
        add(entryEquipoNombre);

        add(new JLabel("Entrenador:"));
        entryEquipoEntrenador = new JTextField();
        add(entryEquipoEntrenador);

        JButton btnRegistrarEquipo = new JButton("Registrar Equipo");
        btnRegistrarEquipo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarEquipo();
            }
        });
        add(btnRegistrarEquipo);
        add(new JLabel(""));

        // Widgets para agregar jugadores a equipos
        add(new JLabel("Agregar Jugador a Equipo"));
        add(new JLabel(""));

        add(new JLabel("Equipo:"));
        comboboxEquipo = new JComboBox<>();
        add(comboboxEquipo);

        add(new JLabel("Jugador:"));
        comboboxJugador = new JComboBox<>();
        add(comboboxJugador);

        JButton btnAgregarJugador = new JButton("Agregar Jugador");
        btnAgregarJugador.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarJugadorAEquipo();
            }
        });
        add(btnAgregarJugador);
        add(new JLabel(""));

        // Widgets para registrar estadios
        add(new JLabel("Registrar Estadio"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryEstadioNombre = new JTextField();
        add(entryEstadioNombre);

        add(new JLabel("Ciudad:"));
        entryEstadioCiudad = new JTextField();
        add(entryEstadioCiudad);

        add(new JLabel("Capacidad:"));
        entryEstadioCapacidad = new JTextField();
        add(entryEstadioCapacidad);

        JButton btnRegistrarEstadio = new JButton("Registrar Estadio");
        btnRegistrarEstadio.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarEstadio();
            }
        });
        add(btnRegistrarEstadio);
        add(new JLabel(""));

        // Widgets para registrar grupos
        add(new JLabel("Registrar Grupo"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryGrupoNombre = new JTextField();
        add(entryGrupoNombre);

        JButton btnRegistrarGrupo = new JButton("Registrar Grupo");
        btnRegistrarGrupo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarGrupo();
            }
        });
        add(btnRegistrarGrupo);
        add(new JLabel(""));

        // Widgets para agregar equipos a grupos
        add(new JLabel("Agregar Equipo a Grupo"));
        add(new JLabel(""));

        add(new JLabel("Grupo:"));
        comboboxGrupo = new JComboBox<>();
        add(comboboxGrupo);

        add(new JLabel("Equipo:"));
        comboboxEquipoGrupo = new JComboBox<>();
        add(comboboxEquipoGrupo);

        JButton btnAgregarEquipo = new JButton("Agregar Equipo");
        btnAgregarEquipo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarEquipoAGrupo();
            }
        });
        add(btnAgregarEquipo);
        add(new JLabel(""));

        // Widgets para generar fixture
        JButton btnGenerarFixture = new JButton("Generar Fixture");
        btnGenerarFixture.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                generarFixture();
            }
        });
        add(btnGenerarFixture);
        add(new JLabel(""));

        // Botón para mostrar información de los equipos
        JButton btnMostrarInfoEquipos = new JButton("Mostrar Información de Equipos");
        btnMostrarInfoEquipos.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarInfoEquipos();
            }
        });
        add(btnMostrarInfoEquipos);
        add(new JLabel(""));

        pack();
    }

    private void registrarJugador() {
        String nombre = entryJugadorNombre.getText();
        int edad = Integer.parseInt(entryJugadorEdad.getText());
        String posicion = entryJugadorPosicion.getText();
        Jugador jugador = new Jugador(nombre, edad, posicion);
        jugadores.add(jugador);
        comboboxJugador.addItem(jugador.getNombre());
        JOptionPane.showMessageDialog(this, "Jugador registrado con éxito");
    }

    private void registrarEquipo() {
        String nombre = entryEquipoNombre.getText();
        String entrenador = entryEquipoEntrenador.getText();
        Equipo equipo = new Equipo(nombre, entrenador);
        equipos.add(equipo);
        comboboxEquipo.addItem(equipo.getNombre());
        comboboxEquipoGrupo.addItem(equipo.getNombre());
        JOptionPane.showMessageDialog(this, "Equipo registrado con éxito");
    }

    private void agregarJugadorAEquipo() {
        String equipoNombre = (String) comboboxEquipo.getSelectedItem();
        String jugadorNombre = (String) comboboxJugador.getSelectedItem();
        Equipo equipo = equipos.stream().filter(e -> e.getNombre().equals(equipoNombre)).findFirst().orElse(null);
        Jugador jugador = jugadores.stream().filter(j -> j.getNombre().equals(jugadorNombre)).findFirst().orElse(null);
        if (equipo != null && jugador != null) {
            equipo.agregarJugador(jugador);
            JOptionPane.showMessageDialog(this, "Jugador agregado al equipo con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Equipo o jugador no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void registrarEstadio() {
        String nombre = entryEstadioNombre.getText();
        String ciudad = entryEstadioCiudad.getText();
        int capacidad = Integer.parseInt(entryEstadioCapacidad.getText());
        Estadio estadio = new Estadio(nombre, ciudad, capacidad);
        estadios.add(estadio);
        JOptionPane.showMessageDialog(this, "Estadio registrado con éxito");
    }

    private void registrarGrupo() {
        String nombre = entryGrupoNombre.getText();
        Grupo grupo = new Grupo(nombre);
        grupos.add(grupo);
        comboboxGrupo.addItem(grupo.getNombre());
        JOptionPane.showMessageDialog(this, "Grupo registrado con éxito");
    }

    private void agregarEquipoAGrupo() {
        String grupoNombre = (String) comboboxGrupo.getSelectedItem();
        String equipoNombre = (String) comboboxEquipoGrupo.getSelectedItem();
        Grupo grupo = grupos.stream().filter(g -> g.getNombre().equals(grupoNombre)).findFirst().orElse(null);
        Equipo equipo = equipos.stream().filter(e -> e.getNombre().equals(equipoNombre)).findFirst().orElse(null);
        if (grupo != null && equipo != null) {
            grupo.agregarEquipo(equipo);
            JOptionPane.showMessageDialog(this, "Equipo agregado al grupo con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Grupo o equipo no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void generarFixture() {
        Mundial mundial = new Mundial();
        grupos.forEach(mundial::registrarGrupo);
        estadios.forEach(mundial::registrarEstadio);
        List<Partido> fixture = mundial.generarFixture();
        StringBuilder fixtureInfo = new StringBuilder();
        for (Partido partido : fixture) {
            fixtureInfo.append(partido.mostrarResultado()).append("\n\n");
        }
        JOptionPane.showMessageDialog(this, fixtureInfo.length() > 0 ? fixtureInfo.toString() : "No hay partidos para mostrar");
    }

    private void mostrarInfoEquipos() {
        StringBuilder infoEquipos = new StringBuilder();
        for (Equipo equipo : equipos) {
            infoEquipos.append(equipo.mostrarInfo()).append("\n\n");
        }
        JOptionPane.showMessageDialog(this, infoEquipos.length() > 0 ? infoEquipos.toString() : "No hay equipos registrados");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
}

