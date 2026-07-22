import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LambdaExpressionExample {
    public static void main(String[] args) {

        List<String> names = new ArrayList<>();

        names.add("Ritik");
        names.add("Aman");
        names.add("Neha");
        names.add("Priya");
        names.add("Karan");

        Collections.sort(names, (a, b) -> a.compareTo(b));

        System.out.println("Sorted List:");

        for (String name : names)
            System.out.println(name);
    }
}