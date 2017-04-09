import fizzbuzz.FizzBuzz;
import org.junit.Assert;
import org.junit.Test;

public class FizzBuzzTest {

    private static final String FIZZ = "fizz";
    private static final String BUZZ = "buzz";
    private static final String FIZZBUZZ = "fizz buzz";


    /**
     * ordinary numbers stay the same
     */
    @Test
    public void testOrdinaryNumbers() {
        Assert.assertEquals(1, FizzBuzz.fizzBuzz(1));
        Assert.assertEquals(2, FizzBuzz.fizzBuzz(2));
        Assert.assertEquals(4, FizzBuzz.fizzBuzz(4));

    }

    /**
     * multiples of 3 return fizz
     */
    @Test
    public void testMultiplesThree() {
        Assert.assertEquals(FIZZ, FizzBuzz.fizzBuzz(3));
        Assert.assertEquals(FIZZ, FizzBuzz.fizzBuzz(9));
        Assert.assertEquals(FIZZ, FizzBuzz.fizzBuzz(123));
    }

    /**
     * multiples of 5 return buzz
     */
    @Test
    public void testMultiplesFive() {
        Assert.assertEquals(BUZZ, FizzBuzz.fizzBuzz(5));
        Assert.assertEquals(BUZZ, FizzBuzz.fizzBuzz(20));
        Assert.assertEquals(BUZZ, FizzBuzz.fizzBuzz(200));
    }

    /**
     * multiples of 3 and 5 return fizz buzz
     */
    @Test
    public void testFizzBuzz() {
        Assert.assertEquals(FIZZBUZZ, FizzBuzz.fizzBuzz(15));
        Assert.assertEquals(FIZZBUZZ, FizzBuzz.fizzBuzz(45));
        Assert.assertEquals(FIZZBUZZ, FizzBuzz.fizzBuzz(315));

    }


}
