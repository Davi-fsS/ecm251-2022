public class HeavyLifters extends Integrantes{

    public HeavyLifters(String nome, String email, String turno) {
        super(nome, email,  turno);
        this.funcao = "HeavyLifter";
    }

    @Override
    public void postagens() {
        if(turno.equals("regular")){
            System.out.println("Podem contar conosco!");
        }
        if(turno.equals("extra")){
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
        
    }

}
