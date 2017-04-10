package fizzbuzz;

public class UseFizzBuzzCase {

    private static int DEFAULT_START = 1;
    private static int DEFAULT_END = 100;
    private static int start;
    private static int end;


    public static void main(String[] args) {

        if (args.length > 1) {
            try {
                start = Integer.valueOf(args[0]);
                end = Integer.valueOf(args[1]);
            } catch (NumberFormatException e) {
                setDefaults();
                e.printStackTrace();
            }
        } else {
            setDefaults();
        }
        for (int i = start; i < end + 1; i++) {
            System.out.println("Input: " + i + ", output: " + FizzBuzz.fizzBuzz(i));
        }
    }

    private static void setDefaults() {
        start = DEFAULT_START;
        end = DEFAULT_END;
    }
}
