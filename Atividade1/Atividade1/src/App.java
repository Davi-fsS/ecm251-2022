// DAVI FERNANDES SIMÕES SOARES - 20.01099-0

public class App {
    public static void main(String[] args) {

        Usuario davi = new Usuario("Davi", new Moto());
        davi.getTransporte();

        System.out.println("\n");

        davi.TrocaVeiculos(new Carro());
        davi.getTransporte();

        System.out.println("\n");

        davi.TrocaVeiculos(new Patinete());
        davi.getTransporte();

        System.out.println("\n");

        davi.TrocaVeiculos(new Bicicleta());
        davi.getTransporte();

        System.out.println("\n");
    
    }
}
