package edu.youruniversity.hw1;

import org.junit.Test;
import static org.junit.Assert.*;
// This is an annotation for assigning point values to tests
import com.gradescope.jh61b.grader.GradedTest;

// Import anything else you need to run the tests, such as the students' classes

public class MyTestClass {
    @Test
    @GradedTest(name="Test 1+1", max_score=1)
    public void test_1p1() {
        int x = 1 + 1;
        System.out.println("Tested 1+1, got " + x);
        assertEquals(x, 2);
    }

    @Test
    @GradedTest(name="Test 1+1*2", max_score=1, visibility="after_published")
    public void test_1p1t2() {
        int x = 1 + 1 * 2;
        System.out.println("Tested 1+1*2, got " + x);
        assertEquals(x, 3);
    }
    // Add more tests...
}
