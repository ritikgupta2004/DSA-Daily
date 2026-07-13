public class OperatorPrecedence {
    public static void main(String[] args) {
        
        int result1 = 10 + 5*2;
        int result2 = (10 + 5) * 2;
        int result3 = 20 + 10/2;
        int result4 = 20/5*2;

        System.out.println("Expression 1: 10 + 5*2 = " + result1);
        System.out.println("Expression 2: (10+5)*2 = " + result2);
        System.out.println("Expression 3: 20 + 10/2 = " + result3);
        System.out.println("Expression 4: 20/5*2 = " + result4);
    }
}