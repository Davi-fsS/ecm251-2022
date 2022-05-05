public class Pedra extends Jogada{

    public Pedra() {
        super(EnumJogadas.TESOURA,EnumJogadas.LAGARTO);  //tesoura e lagarto
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PEDRA;
    }
}
