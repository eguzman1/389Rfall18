package projects.tavl;

/* These imports bind with jUnit4 (four). Since this is the approach that you have used in 131 and 132, and we are absolutely
 * certain that submit.cs works well with it, we kindly ask that you stick with it for our projects. It's easy: just copy
 * and paste the following imports, and then you can write your tests the way that you have been used to.
 */
import org.junit.Test;
import java.util.Random;
import static org.junit.Assert.*;

/**
 * <p><tt>StudentTests</tt> is an example class that contains some basic jUnit tests that you can write. It is <b>very important</b>
 * that you write your own tests! </p>
 * @author --- YOUR NAME HERE! -----
 * @see ThreadedAVLTree
 */
public class StudentTests {

    private ThreadedAVLTree<Integer> tree = new ThreadedAVLTree<>(); // Any other Comparable type will do.
    private static final long SEED=47; // To allow for reproducibility of your test cases.
    private static Random r = new Random(SEED); // Or don't provide a seed for full pseudo-randomness (but you lose the reproducibility)
    private static final int UPPER_BOUND = 1000; // Upper bound of integers to generate.
    private static final int NUM_INTS = 2000; // Number of integers to generate in stress tests.

    // Note that if NUM_INTS > UPPER_BOUND, by pigeonhole principle, you *WILL* generate duplicate integers through calls to Random::nextInt(). For
    // example, if you want to generate ints between 1 and 10 inclusive uniformly at random and you perform this experiment 11 times, you are guaranteed
    // to repeat the insertion of an integer between 1 and 10 at least twice.


    /**
     * Tests if an empty tree behaves as it should based on the docs.
     */
    @Test
    public void testEmptyTree(){

        // assertTrue is overloaded, which means that we can call it with just one argument (a boolean condition
        // that must be met), or two: a String which should be human-readable and describes what went wrong,
        // followed by our familiar condition. This version is more verbal and gives you more information
        // about what went wrong. This is how we structure our tests on submit.cs so that you have a lot more information
        // about where your tests are failing: replicate this behavior yourselves and save some time!
        assertTrue("After creation, the tree should be empty.", tree.isEmpty());


        // assertNull(String message, Object obj) is equivalent to assertEquals(message, null, obj) or
        // assertTrue(message, obj==null). It's just more indicative of why it's used.
        assertNull("After creation, the tree's root should be null.", tree.getRoot());

        // Notice how the three-argument version of assertEquals() works: The first argument is a String,
        // which should be human-readable and describes what went wrong, the second is the exact value we expected,
        // while the third one is the value that we got! Remember: (message, expected, actual). *NOT*
        // (message, actual, expected).
        assertEquals("After creation, the tree's height should be -1.", -1, tree.height());
    }

    @Test
    public void testsimpleAdditions() {

        // Insert the first integer
        attemptInsertion(10); // Definition of this utility is below.
        assertFalse("After a single insertion, the tree should no longer be considered empty!", tree.isEmpty());
        assertEquals("After a single insertion, the tree's root should be equal to the element inserted.", new Integer(10),
                tree.getRoot());
        assertEquals("After a single insertion, the tree's height should be 0.", 0, tree.height());

        // The second integer will be the root's left child, and should *not* trigger rotations.
        attemptInsertion(5);
        assertFalse("After two insertions, the tree should still not be considered empty!", tree.isEmpty());
        assertEquals("After two insertions, the tree's root should still be equal to the element previously inserted.", new Integer(10),
                tree.getRoot());
        assertEquals("After two insertions, the tree's height should be 1.", 1, tree.height());

        // Let's insert a right child for the root. This should also *not* trigger rotations.
        attemptInsertion(15);
        assertFalse("After a third insertion that should not trigger a re-balancing, the tree should still not be considered empty!", tree.isEmpty());
        assertEquals("After a third insertion that should not trigger a re-balancing, the tree's root should still be equal to the element " +
                        "first inserted.", new Integer(10), tree.getRoot());
        assertEquals("After a third insertion that should not trigger a re-balancing, the tree's height should still be 1.", 1,
                tree.height());
    }

    /* This utility tries to insert an integer into the tree and reports any Throwables caught. */
    private void attemptInsertion(int intToInsert){
        try {
            tree.insert(intToInsert);
        }  catch (Throwable t) {
            fail("Insertion of " + intToInsert + ":" + format(t));
        }
    }

    /* A utility that receives a Throwable and returns a String with useful information mined from the thrown Throwable instance. */
    private static String format(Throwable t){
        return "Caught a " + t.getClass()+ " with message: " + t.getMessage() + ".";
    }

    /**
     * This test inserts many random integers and checks for any Throwable instances thrown.
     */
    @Test
    public void stressTestForInsertions(){
        int randInt = -1; // Just an initializer value so that the catch block can see the variable from its scope.
        for(int ignored = 0; ignored < NUM_INTS; ignored++){
            attemptInsertion(r.nextInt(UPPER_BOUND));
        }
    }
}
