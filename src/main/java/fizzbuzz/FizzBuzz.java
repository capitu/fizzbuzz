package fizzbuzz;

public class FizzBuzz {

    private static final String FIZZ = "fizz";
    private static final String BUZZ = "buzz";
    private static final String FIZZBUZZ = "fizz buzz";


    /**
     * Metodo
     * @param x l'input
     */
    public static Object fizzBuzz(int x) {
        return((x%5 == 0 && x%3 == 0) ? FIZZBUZZ : (x%5 == 0 ? BUZZ : (x%3 == 0 ? FIZZ : x)));

    }
}
