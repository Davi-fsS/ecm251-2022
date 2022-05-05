public class Tesoura extends Jogada{

    public Tesoura(){
        super(EnumJogadas.PAPEL,EnumJogadas.LAGARTO);    //papel e lagarto
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.TESOURA;
    }

}
