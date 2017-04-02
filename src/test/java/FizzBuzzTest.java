import fizzbuzz.FizzBuzz;
import org.junit.Test;
import org.junit.Assert;

public class FizzBuzzTest {

    @Test
    public void testFizzBuzz() {

        //ordinary numbers stay the same
        Assert.assertEquals(1, FizzBuzz.fizzBuzz(1));
        Assert.assertEquals(2, FizzBuzz.fizzBuzz(2));
        Assert.assertEquals(4, FizzBuzz.fizzBuzz(4));

        //multiples of 3 return fizz
        Assert.assertEquals(FizzBuzz.FIZZ, FizzBuzz.fizzBuzz(3));
        Assert.assertEquals(FizzBuzz.FIZZ, FizzBuzz.fizzBuzz(9));
        Assert.assertEquals(FizzBuzz.FIZZ, FizzBuzz.fizzBuzz(123));

        //multiples of 5 return buzz
        Assert.assertEquals(FizzBuzz.BUZZ, FizzBuzz.fizzBuzz(5));
        Assert.assertEquals(FizzBuzz.BUZZ, FizzBuzz.fizzBuzz(20));
        Assert.assertEquals(FizzBuzz.BUZZ, FizzBuzz.fizzBuzz(200));

        //multiples of 3 and 5 return fizz buzz
        Assert.assertEquals(FizzBuzz.FIZZBUZZ, FizzBuzz.fizzBuzz(15));
        Assert.assertEquals(FizzBuzz.FIZZBUZZ, FizzBuzz.fizzBuzz(45));
        Assert.assertEquals(FizzBuzz.FIZZBUZZ, FizzBuzz.fizzBuzz(315));

    }
}
