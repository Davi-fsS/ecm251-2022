
public class App {
    public static void main(String[] args) throws Exception {
        //Ninja jiraya = new Ninja("Jiraya", "Familia", new String[] {"Corte vertical","Corte Horizontal"});
        //System.out.println("Treinamento"+jiraya.train());
        //System.out.println(jiraya);

        //AcademicStudent naruto = new AcademicStudent("Naruto", "Uzumaki", 
        //new String[]{"Jutsu dos clones da sombra","Rasengan","Chamar Kurama"});

        //System.out.println(naruto.train());   // A GENTE NÃO DECLAROU ESTE MÉTODO EM ACADEMIC STUDENT, HERDOU ISSO DA CLASSE MÃE

        //System.out.println(naruto.play());
        
        Genin ninja = new Genin("Nome", "Konoha", new String[]{"Jutsu1","Jutsu2"}, "Coletar item");
        System.out.println(ninja.goToMission());
        System.out.println(ninja.train());
        System.out.println(ninja.toString());
    }
}
