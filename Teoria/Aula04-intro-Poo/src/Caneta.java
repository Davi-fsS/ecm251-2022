import javax.swing.event.SwingPropertyChangeSupport;

public class Caneta{

    //Características da caneta - ATRIBUTOS
    String modelo;
    String cor;
    double ponta;
    int carga;

    //Comportamentos da caneta - MÉTODOS
    void escrever(String texto){
        System.out.println(texto);
    }
}