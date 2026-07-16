import java.util.Scanner;
public class StringReversal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String text = sc.nextLine();
        StringBuilder reversed = new StringBuilder(text);
        reversed.reverse();
        System.err.println("Reversed String = " + reversed);
        sc.close();
    }
}