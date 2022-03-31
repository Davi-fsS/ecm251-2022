public class Usuarios {
    public String nome;
    private String senha;
    private String email;
    private Conta conta;

    public Usuarios(String nome,String senha, String email, Conta conta){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.conta = conta;
    }

    public void getNome(){
        System.out.println(this.nome);
    }

    public void getSenha(){
        System.out.println(this.senha);
    }

    public void getEmail(){
        System.out.println(this.email);
    }

    public void getConta(){
        System.out.println(this.conta);
    }

}
