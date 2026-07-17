import java.util.Scanner;
public class PalindromeChecker {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String text = sc.nextLine();
        String cleanedText = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversedText = new StringBuilder(cleanedText).reverse().toString();
        if (cleanedText.equals(reversedText)){
            System.out.println("The given string is a Palindrome.");
        }else {
            System.out.println("The given string is NOT a Palindrome.");
        }
        sc.close();
    }
}