package fizzbuzz;

public class FizzBuzz {

    private static final String FIZZ = "fizz";
    private static final String BUZZ = "buzz";
    private static final String FIZZBUZZ = "fizz buzz";


    /**
     * Metodo
     * @param x
     */
    public static Object fizzBuzz(int x) {
        return((x%5 == 0 && x%3 == 0) ? FIZZBUZZ : (x%5 == 0 ? FIZZ : (x%3 == 0 ? BUZZ : x)));

    }
}
