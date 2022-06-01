import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
        
        //Cria um ArrayList para as Canetas
        ArrayList<Caneta> canetas = new ArrayList<Caneta>();

        //Adiciona uma caneta
        canetas.add(new Caneta("Azul", 0.7));

        canetas.add(new Caneta("Vermelha", 1.0));

        //Tamanho do ArrayList antes
        System.out.println("Size antes: " + canetas.size());

        //Removendo um objeto pelo indice
        canetas.remove(1);

        //Tamanho do ArrayList depois
        System.out.println("Size agora: " + canetas.size());

        //Passar por todos os elementos do array
        for(int i = 0; i < canetas.size() ; i++){
            System.out.println("Cor da caneta: " + canetas.get(i).cor);
        }

        //Metodo 2 
        for (Caneta item : canetas) {                             // pega a instancia do Caneta canetas e 
            System.out.println("Cor da caneta: " + item.cor);     // itera atraves da variavel "item"
        }
    }
}
