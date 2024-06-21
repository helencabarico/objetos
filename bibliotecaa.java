package com.mycompany.ejercicio1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import biblioteca.Biblioteca;
import biblioteca.Libro;
import biblioteca.Prestamo;
import biblioteca.Autor;
import biblioteca.Usuario;
import biblioteca.Categoria;

public class Main extends JFrame {
    private Biblioteca biblioteca;
    private JTextField entryTitulo, entryIdLibro, entryAutorNombre, entryAutorApellido, entryCategoria;
    private JTextField entryUsuarioNombre, entryUsuarioApellido, entryIdUsuario;
    private JTextField entryIdPrestamoLibro, entryIdPrestamoUsuario, entryFechaPrestamo, entryFechaDevolucion;

    public Main() {
        biblioteca = new Biblioteca();
        initComponents();
    }

    private void initComponents() {
        setTitle("Biblioteca");
        setLayout(new GridLayout(20, 2));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(Color.lightGray);

        // Widgets para registrar libros
        add(new JLabel("Registrar Libro"));
        add(new JLabel(""));

        add(new JLabel("Título:"));
        entryTitulo = new JTextField();
        add(entryTitulo);

        add(new JLabel("ID:"));
        entryIdLibro = new JTextField();
        add(entryIdLibro);

        add(new JLabel("Autor Nombre:"));
        entryAutorNombre = new JTextField();
        add(entryAutorNombre);

        add(new JLabel("Autor Apellido:"));
        entryAutorApellido = new JTextField();
        add(entryAutorApellido);

        add(new JLabel("Categoría:"));
        entryCategoria = new JTextField();
        add(entryCategoria);

        JButton btnRegistrarLibro = new JButton("Registrar Libro");
        btnRegistrarLibro.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarLibro();
            }
        });
        add(btnRegistrarLibro);
        add(new JLabel(""));

        // Widgets para registrar usuarios
        add(new JLabel("Registrar Usuario"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryUsuarioNombre = new JTextField();
        add(entryUsuarioNombre);

        add(new JLabel("Apellido:"));
        entryUsuarioApellido = new JTextField();
        add(entryUsuarioApellido);

        add(new JLabel("ID Usuario:"));
        entryIdUsuario = new JTextField();
        add(entryIdUsuario);

        JButton btnRegistrarUsuario = new JButton("Registrar Usuario");
        btnRegistrarUsuario.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarUsuario();
            }
        });
        add(btnRegistrarUsuario);
        add(new JLabel(""));

        // Widgets para realizar préstamo
        add(new JLabel("Realizar Préstamo"));
        add(new JLabel(""));

        add(new JLabel("ID Libro:"));
        entryIdPrestamoLibro = new JTextField();
        add(entryIdPrestamoLibro);

        add(new JLabel("ID Usuario:"));
        entryIdPrestamoUsuario = new JTextField();
        add(entryIdPrestamoUsuario);

        add(new JLabel("Fecha Préstamo:"));
        entryFechaPrestamo = new JTextField();
        add(entryFechaPrestamo);

        add(new JLabel("Fecha Devolución:"));
        entryFechaDevolucion = new JTextField();
        add(entryFechaDevolucion);

        JButton btnRealizarPrestamo = new JButton("Realizar Préstamo");
        btnRealizarPrestamo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                realizarPrestamo();
            }
        });
        add(btnRealizarPrestamo);
        add(new JLabel(""));

        // Botón para mostrar libros
        JButton btnMostrarLibros = new JButton("Mostrar Libros");
        btnMostrarLibros.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarLibros();
            }
        });
        add(btnMostrarLibros);
        add(new JLabel(""));

        pack();
    }

    private void registrarLibro() {
        Autor autor = new Autor(entryAutorNombre.getText(), entryAutorApellido.getText());
        Categoria categoria = new Categoria(entryCategoria.getText());
        Libro libro = new Libro(entryTitulo.getText(), entryIdLibro.getText(), autor, categoria);
        biblioteca.registrarLibro(libro);
        JOptionPane.showMessageDialog(this, "Libro registrado con éxito");
    }

    private void registrarUsuario() {
        Usuario usuario = new Usuario(entryUsuarioNombre.getText(), entryUsuarioApellido.getText(), entryIdUsuario.getText());
        biblioteca.registrarUsuario(usuario);
        JOptionPane.showMessageDialog(this, "Usuario registrado con éxito");
    }

    private void realizarPrestamo() {
        try {
            Libro libro = biblioteca.getLibros().stream().filter(l -> l.getId().equals(entryIdPrestamoLibro.getText())).findFirst().orElse(null);
            Usuario usuario = biblioteca.getUsuarios().stream().filter(u -> u.getIdUsuario().equals(entryIdPrestamoUsuario.getText())).findFirst().orElse(null);
            if (libro == null || usuario == null) throw new Exception();
            Prestamo prestamo = new Prestamo(libro, usuario, entryFechaPrestamo.getText(), entryFechaDevolucion.getText());
            biblioteca.realizarPrestamo(prestamo);
            JOptionPane.showMessageDialog(this, "Préstamo realizado con éxito");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Libro o Usuario no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void mostrarLibros() {
        String infoLibros = biblioteca.mostrarLibros();
        JOptionPane.showMessageDialog(this, infoLibros.isEmpty() ? "No hay libros registrados" : infoLibros);
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
