package com.mycompany.ejercicio1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

import gestioncursos.Asignatura;
import gestioncursos.Curso;
import gestioncursos.Evaluacion;
import gestioncursos.Estudiante;
import gestioncursos.Horario;
import gestioncursos.Profesor;

public class Main extends JFrame {
    private List<Profesor> profesores;
    private List<Asignatura> asignaturas;
    private List<Curso> cursos;
    private List<Estudiante> estudiantes;
    private List<Evaluacion> evaluaciones;

    private JTextField entryProfesorNombre, entryProfesorApellido;
    private JTextField entryAsignaturaNombre;
    private JComboBox<String> comboboxProfesor;
    private JTextField entryCursoNombre;
    private JComboBox<String> comboboxProfesorCurso;
    private JTextField entryHorarioDia, entryHorarioInicio, entryHorarioFin;
    private JTextField entryEstudianteNombre, entryEstudianteApellido, entryIdEstudiante;
    private JComboBox<String> comboboxCurso;
    private JTextField entryIdEstudianteCurso;
    private JComboBox<String> comboboxCursoEval;
    private JTextField entryIdEstudianteEval, entryNota;

    public Main() {
        profesores = new ArrayList<>();
        asignaturas = new ArrayList<>();
        cursos = new ArrayList<>();
        estudiantes = new ArrayList<>();
        evaluaciones = new ArrayList<>();
        initComponents();
    }

    private void initComponents() {
        setTitle("Sistema de Gestión de Cursos");
        setLayout(new GridLayout(30, 2));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(Color.lightGray);

        // Widgets para registrar profesores
        add(new JLabel("Registrar Profesor"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryProfesorNombre = new JTextField();
        add(entryProfesorNombre);

        add(new JLabel("Apellido:"));
        entryProfesorApellido = new JTextField();
        add(entryProfesorApellido);

        JButton btnRegistrarProfesor = new JButton("Registrar Profesor");
        btnRegistrarProfesor.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarProfesor();
            }
        });
        add(btnRegistrarProfesor);
        add(new JLabel(""));

        // Widgets para registrar asignaturas
        add(new JLabel("Registrar Asignatura"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryAsignaturaNombre = new JTextField();
        add(entryAsignaturaNombre);

        add(new JLabel("Profesor:"));
        comboboxProfesor = new JComboBox<>();
        add(comboboxProfesor);

        JButton btnRegistrarAsignatura = new JButton("Registrar Asignatura");
        btnRegistrarAsignatura.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarAsignatura();
            }
        });
        add(btnRegistrarAsignatura);
        add(new JLabel(""));

        // Widgets para registrar cursos
        add(new JLabel("Registrar Curso"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryCursoNombre = new JTextField();
        add(entryCursoNombre);

        add(new JLabel("Profesor:"));
        comboboxProfesorCurso = new JComboBox<>();
        add(comboboxProfesorCurso);

        add(new JLabel("Día:"));
        entryHorarioDia = new JTextField();
        add(entryHorarioDia);

        add(new JLabel("Hora inicio:"));
        entryHorarioInicio = new JTextField();
        add(entryHorarioInicio);

        add(new JLabel("Hora fin:"));
        entryHorarioFin = new JTextField();
        add(entryHorarioFin);

        JButton btnRegistrarCurso = new JButton("Registrar Curso");
        btnRegistrarCurso.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarCurso();
            }
        });
        add(btnRegistrarCurso);
        add(new JLabel(""));

        // Widgets para registrar estudiantes
        add(new JLabel("Registrar Estudiante"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryEstudianteNombre = new JTextField();
        add(entryEstudianteNombre);

        add(new JLabel("Apellido:"));
        entryEstudianteApellido = new JTextField();
        add(entryEstudianteApellido);

        add(new JLabel("ID Estudiante:"));
        entryIdEstudiante = new JTextField();
        add(entryIdEstudiante);

        JButton btnRegistrarEstudiante = new JButton("Registrar Estudiante");
        btnRegistrarEstudiante.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarEstudiante();
            }
        });
        add(btnRegistrarEstudiante);
        add(new JLabel(""));

        // Widgets para agregar estudiantes a cursos
        add(new JLabel("Agregar Estudiante a Curso"));
        add(new JLabel(""));

        add(new JLabel("Curso:"));
        comboboxCurso = new JComboBox<>();
        add(comboboxCurso);

        add(new JLabel("ID Estudiante:"));
        entryIdEstudianteCurso = new JTextField();
        add(entryIdEstudianteCurso);

        JButton btnAgregarEstudianteCurso = new JButton("Agregar Estudiante");
        btnAgregarEstudianteCurso.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarEstudianteACurso();
            }
        });
        add(btnAgregarEstudianteCurso);
        add(new JLabel(""));

        // Widgets para realizar evaluaciones
        add(new JLabel("Realizar Evaluación"));
        add(new JLabel(""));

        add(new JLabel("Curso:"));
        comboboxCursoEval = new JComboBox<>();
        add(comboboxCursoEval);

        add(new JLabel("ID Estudiante:"));
        entryIdEstudianteEval = new JTextField();
        add(entryIdEstudianteEval);

        add(new JLabel("Nota:"));
        entryNota = new JTextField();
        add(entryNota);

        JButton btnRealizarEvaluacion = new JButton("Realizar Evaluación");
        btnRealizarEvaluacion.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                realizarEvaluacion();
            }
        });
        add(btnRealizarEvaluacion);
        add(new JLabel(""));

        // Botón para mostrar información de los cursos
        JButton btnMostrarInfoCursos = new JButton("Mostrar Información de Cursos");
        btnMostrarInfoCursos.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarInfoCursos();
            }
        });
        add(btnMostrarInfoCursos);
        add(new JLabel(""));

        pack();
    }

    private void registrarProfesor() {
        Profesor profesor = new Profesor(entryProfesorNombre.getText(), entryProfesorApellido.getText());
        profesores.add(profesor);
        comboboxProfesor.addItem(profesor.getNombre() + " " + profesor.getApellido());
        comboboxProfesorCurso.addItem(profesor.getNombre() + " " + profesor.getApellido());
        JOptionPane.showMessageDialog(this, "Profesor registrado con éxito");
    }

    private void registrarAsignatura() {
        Profesor profesor = profesores.stream()
                .filter(p -> (p.getNombre() + " " + p.getApellido()).equals(comboboxProfesor.getSelectedItem()))
                .findFirst()
                .orElse(null);
        if (profesor != null) {
            Asignatura asignatura = new Asignatura(entryAsignaturaNombre.getText(), profesor);
            asignaturas.add(asignatura);
            JOptionPane.showMessageDialog(this, "Asignatura registrada con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Profesor no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void registrarCurso() {
        Profesor profesor = profesores.stream()
                .filter(p -> (p.getNombre() + " " + p.getApellido()).equals(comboboxProfesorCurso.getSelectedItem()))
                .findFirst()
                .orElse(null);
        if (profesor != null) {
            Horario horario = new Horario(entryHorarioDia.getText(), entryHorarioInicio.getText(), entryHorarioFin.getText());
            Curso curso = new Curso(entryCursoNombre.getText(), profesor, horario);
            cursos.add(curso);
            comboboxCurso.addItem(curso.getNombre());
            comboboxCursoEval.addItem(curso.getNombre());
            JOptionPane.showMessageDialog(this, "Curso registrado con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Profesor no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void registrarEstudiante() {
        Estudiante estudiante = new Estudiante(entryEstudianteNombre.getText(), entryEstudianteApellido.getText(), entryIdEstudiante.getText());
        estudiantes.add(estudiante);
        JOptionPane.showMessageDialog(this, "Estudiante registrado con éxito");
    }

    private void agregarEstudianteACurso() {
        Curso curso = cursos.stream()
                .filter(c -> c.getNombre().equals(comboboxCurso.getSelectedItem()))
                .findFirst()
                .orElse(null);
        Estudiante estudiante = estudiantes.stream()
                .filter(e -> e.getIdEstudiante().equals(entryIdEstudianteCurso.getText()))
                .findFirst()
                .orElse(null);
        if (curso != null && estudiante != null) {
            curso.agregarEstudiante(estudiante);
            JOptionPane.showMessageDialog(this, "Estudiante agregado al curso con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Curso o estudiante no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void realizarEvaluacion() {
        Curso curso = cursos.stream()
                .filter(c -> c.getNombre().equals(comboboxCursoEval.getSelectedItem()))
                .findFirst()
                .orElse(null);
        Estudiante estudiante = estudiantes.stream()
                .filter(e -> e.getIdEstudiante().equals(entryIdEstudianteEval.getText()))
                .findFirst()
                .orElse(null);
        if (curso != null && estudiante != null) {
            Evaluacion evaluacion = new Evaluacion(curso, estudiante, entryNota.getText());
            evaluaciones.add(evaluacion);
            JOptionPane.showMessageDialog(this, "Evaluación registrada con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Curso o estudiante no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void mostrarInfoCursos() {
        StringBuilder infoCursos = new StringBuilder();
        for (Curso curso : cursos) {
            infoCursos.append(curso.mostrarInfo()).append("\n\n");
        }
        JOptionPane.showMessageDialog(this, infoCursos.length() > 0 ? infoCursos.toString() : "No hay cursos registrados");
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

