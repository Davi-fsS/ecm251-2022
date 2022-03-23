import javax.sound.midi.VoiceStatus;

public class Cliente {
    //Atributos
    private String cpf;
    private String nome;
    private String email;
    private Conta conta;      //convenção de chamar um objeto Conta de "conta"

    //Constructor !
    public Cliente(String nome, String cpf, String email, Conta conta){
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        this.conta = conta;
    }

    //Métodos 
    public void visualizarCliente(){
        System.out.println("--Dados do cliente--");
        System.out.println("Nome: "+nome);
        System.out.println("CPF: "+cpf);
        System.out.println("E-mail: "+email);
        System.out.println("Conta: "+conta);
    }

    //Getters

    public String getNome(){
        return nome;
    }

    public String getCpf(){
        return cpf;
    }

    public String getEmail(){
        return email;
    }

    public Conta getConta(){
        return conta;
    }

    //Setters

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setEmail(String email){
        this.email = email;
    }    
}
