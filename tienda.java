package com.mycompany.ejercicio1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

import gestiontienda.Categoria;
import gestiontienda.Cliente;
import gestiontienda.ItemOrden;
import gestiontienda.Orden;
import gestiontienda.Producto;
import gestiontienda.Tienda;

public class Main extends JFrame {
    private Tienda tienda;

    private JTextField entryProductoNombre, entryProductoPrecio;
    private JComboBox<String> comboboxCategoria;
    private JTextField entryClienteNombre, entryClienteApellido, entryIdCliente;
    private JComboBox<String> comboboxCliente, comboboxProducto;
    private JTextField entryCantidad;

    public Main() {
        tienda = new Tienda();

        // Categorías predefinidas
        Categoria categoria1 = new Categoria("Periféricos");
        Categoria categoria2 = new Categoria("Tarjetas de video");
        tienda.getCategorias().add(categoria1);
        tienda.getCategorias().add(categoria2);

        initComponents();
    }

    private void initComponents() {
        setTitle("Sistema de Gestión de Tienda");
        setLayout(new GridLayout(20, 2));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(Color.lightGray);

        // Widgets para registrar productos
        add(new JLabel("Registrar Producto"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryProductoNombre = new JTextField();
        add(entryProductoNombre);

        add(new JLabel("Precio:"));
        entryProductoPrecio = new JTextField();
        add(entryProductoPrecio);

        add(new JLabel("Categoría:"));
        comboboxCategoria = new JComboBox<>();
        for (Categoria categoria : tienda.getCategorias()) {
            comboboxCategoria.addItem(categoria.getNombre());
        }
        add(comboboxCategoria);

        JButton btnRegistrarProducto = new JButton("Registrar Producto");
        btnRegistrarProducto.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarProducto();
            }
        });
        add(btnRegistrarProducto);
        add(new JLabel(""));

        // Widgets para registrar clientes
        add(new JLabel("Registrar Cliente"));
        add(new JLabel(""));

        add(new JLabel("Nombre:"));
        entryClienteNombre = new JTextField();
        add(entryClienteNombre);

        add(new JLabel("Apellido:"));
        entryClienteApellido = new JTextField();
        add(entryClienteApellido);

        add(new JLabel("ID Cliente:"));
        entryIdCliente = new JTextField();
        add(entryIdCliente);

        JButton btnRegistrarCliente = new JButton("Registrar Cliente");
        btnRegistrarCliente.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrarCliente();
            }
        });
        add(btnRegistrarCliente);
        add(new JLabel(""));

        // Widgets para agregar items a orden
        add(new JLabel("Agregar Item a Orden"));
        add(new JLabel(""));

        add(new JLabel("Cliente:"));
        comboboxCliente = new JComboBox<>();
        add(comboboxCliente);

        add(new JLabel("Producto:"));
        comboboxProducto = new JComboBox<>();
        add(comboboxProducto);

        add(new JLabel("Cantidad:"));
        entryCantidad = new JTextField();
        add(entryCantidad);

        JButton btnAgregarItem = new JButton("Agregar Item");
        btnAgregarItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarItemAOrden();
            }
        });
        add(btnAgregarItem);
        add(new JLabel(""));

        // Botones para mostrar información
        JButton btnMostrarProductos = new JButton("Mostrar Productos");
        btnMostrarProductos.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarInfoProductos();
            }
        });
        add(btnMostrarProductos);
        add(new JLabel(""));

        JButton btnMostrarOrdenes = new JButton("Mostrar Órdenes");
        btnMostrarOrdenes.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarInfoOrdenes();
            }
        });
        add(btnMostrarOrdenes);
        add(new JLabel(""));

        pack();
    }

    private void registrarProducto() {
        String nombre = entryProductoNombre.getText();
        double precio = Double.parseDouble(entryProductoPrecio.getText());
        Categoria categoria = tienda.getCategorias().stream()
                .filter(c -> c.getNombre().equals(comboboxCategoria.getSelectedItem()))
                .findFirst()
                .orElse(null);
        if (categoria != null) {
            Producto producto = new Producto(nombre, precio, categoria);
            tienda.registrarProducto(producto);
            comboboxProducto.addItem(producto.getNombre());
            JOptionPane.showMessageDialog(this, "Producto registrado con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Categoría no encontrada", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void registrarCliente() {
        String nombre = entryClienteNombre.getText();
        String apellido = entryClienteApellido.getText();
        String idCliente = entryIdCliente.getText();
        Cliente cliente = new Cliente(nombre, apellido, idCliente);
        tienda.registrarCliente(cliente);
        comboboxCliente.addItem(cliente.getNombre() + " " + cliente.getApellido());
        JOptionPane.showMessageDialog(this, "Cliente registrado con éxito");
    }

    private void agregarItemAOrden() {
        Cliente cliente = tienda.getClientes().stream()
                .filter(c -> (c.getNombre() + " " + c.getApellido()).equals(comboboxCliente.getSelectedItem()))
                .findFirst()
                .orElse(null);
        Producto producto = tienda.getProductos().stream()
                .filter(p -> p.getNombre().equals(comboboxProducto.getSelectedItem()))
                .findFirst()
                .orElse(null);
        if (cliente != null && producto != null) {
            int cantidad = Integer.parseInt(entryCantidad.getText());
            ItemOrden item = new ItemOrden(producto, cantidad);
            Orden orden = tienda.getOrdenes().stream()
                    .filter(o -> o.getCliente().equals(cliente))
                    .findFirst()
                    .orElse(tienda.crearOrden(cliente));
            orden.agregarItem(item);
            JOptionPane.showMessageDialog(this, "Item agregado a la orden con éxito");
        } else {
            JOptionPane.showMessageDialog(this, "Cliente o producto no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void mostrarInfoProductos() {
        String infoProductos = tienda.mostrarProductos();
        JOptionPane.showMessageDialog(this, infoProductos.isEmpty() ? "No hay productos registrados" : infoProductos);
    }

    private void mostrarInfoOrdenes() {
        StringBuilder infoOrdenes = new StringBuilder();
        for (Orden orden : tienda.getOrdenes()) {
            infoOrdenes.append(orden.mostrarInfo()).append("\n\n");
        }
        JOptionPane.showMessageDialog(this, infoOrdenes.length() > 0 ? infoOrdenes.toString() : "No hay órdenes registradas");
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

