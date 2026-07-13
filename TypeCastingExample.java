public class TypeCastingExample {
    public static void main(String[] args) {
        
        double decimalNumber = 25.89;
        
        int integerNumber = (int) decimalNumber;

        System.out.println("Original Double Value : " + decimalNumber);
        System.out.println("After Casting to int : " + integerNumber);

        System.out.println();

        int age =21;

        double convertedAge = age;

        System.out.println("Original int Value : " + age);
        System.out.println("After Casting to double : " + convertedAge);
    }
}