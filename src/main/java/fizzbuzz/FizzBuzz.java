package fizzbuzz;

public class FizzBuzz {

    public static final String FIZZ = "fizz";
    public static final String BUZZ = "buzz";
    public static final String FIZZBUZZ = "fizz buzz";


    /**
     * Metodo
     * @param x l'input
     */
    public static Object fizzBuzz(int x) {
        return((x%5 == 0 && x%3 == 0) ? FIZZBUZZ : (x%5 == 0 ? BUZZ : (x%3 == 0 ? FIZZ : x)));

    }
}
