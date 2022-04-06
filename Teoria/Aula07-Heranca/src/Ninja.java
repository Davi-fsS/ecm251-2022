import java.util.Arrays;

public class Ninja{
    private String name;               // O ATRIBUTO "PROTECTED" DEIXA ELE EM ABERTO PARA TODOS DA HERANÇA
    private String family;
    private String[] jutsus;

    //ctrl + ponto = inicializar o construtor
    public Ninja(String name, String family, String[] jutsus) {
        this.name = name;
        this.family = family;
        this.jutsus = jutsus;
    }

    public String train(){
        return String.format("%s está treinando!", name);          //essa String.format transforma na sintaxe basica de Python 
    }

    @Override
    public String toString() {
        return "Ninja [family=" + family + ", jutsus=" + Arrays.toString(jutsus) + ", name=" + name + "]";
    }

    public String getName() {
        return name;
    }

    public String getFamily() {
        return family;
    }

    public String[] getJutsus() {
        return jutsus;
    }

}