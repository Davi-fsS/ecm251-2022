public class App {
    public static void main(String[] args) throws Exception {
        Produto cornDog = new Comida(12.5, "CornDog", 5, "Um cachorro quente meio errado", EnumCategoriaComida.COREANA, EnumAlergicos.GLUTEM, EnumPimenta.SUAVE);
        Produto acaiMoleza = new Bebida(10.5, "Açai moleza", 1, "Real fonte de energia", EnumCategoriaBebida.SUCO, EnumTemperatura.FRIO);
        Produto aprendendoJava = new Leitura(40.0, "Aprendendo Java", 1, "Descobrindo a linguagem Java", EnumGeneros.TECNOLOGIA, "Caelum", "Brasil", 170);

        System.out.println("** Preços Regulares **");
        System.out.println(cornDog.getNome()+": R$ "+ cornDog.getPreco());
        System.out.println();
        System.out.println(acaiMoleza.getNome()+": R$ "+acaiMoleza.getPreco());
        System.out.println();
        System.out.println(aprendendoJava.getNome()+": R$ "+aprendendoJava.getPreco());

        System.out.println();

        System.out.println("** Preços Com Desconto **");
        System.out.println(cornDog.getNome()+": R$ "+ precoComDesconto(cornDog));
        System.out.println();
        System.out.println(acaiMoleza.getNome()+": R$ "+precoComDesconto(acaiMoleza));
        System.out.println();

        //Implementar um sistema que verifica cada objeto criado
        //Colocar os objetos em um array e fazer um laço for comparando cada valor do array  == TENTAR

        if(precoComDesconto(aprendendoJava) == aprendendoJava.getPreco()){
            System.out.println("Não houve desconto neste livro, portanto R$: "+precoComDesconto(aprendendoJava));
        }
        else{
            System.out.println(aprendendoJava.getNome()+": R$ "+precoComDesconto(aprendendoJava));
        }
    }

    public static double precoComDesconto(IGerarDesconto produto){
        return produto.gerarDesconto();
    }
}
