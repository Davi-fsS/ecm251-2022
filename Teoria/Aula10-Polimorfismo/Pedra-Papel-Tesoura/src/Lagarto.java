public class Lagarto extends Jogada{

    public Lagarto(){
        super(EnumJogadas.SPOCK, EnumJogadas.PAPEL);   //spock e papel
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.LAGARTO;
    }
}
