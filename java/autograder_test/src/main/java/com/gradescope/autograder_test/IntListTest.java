package com.gradescope.autograder_test;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gradescope.jh61b.grader.GradedTest;
import com.gradescope.jh61b.grader.GradedTestRunnerJSON;
import com.gradescope.jh61b.grader.GradedTestListenerJSON;
import org.junit.runner.RunWith;
import org.junit.runner.JUnitCore;

import com.gradescope.autograder_test.IntList;

// @RunWith(GradedTestRunnerJSON.class)
public class IntListTest {
    @Test
    @GradedTest(name="Test creating an IntList from varargs", max_score=1)
    public void test_varargs() {
        IntList test = IntList.createList(1, 2, 4, 8, 16);
        assertEquals(test.toString(), "1 2 4 8 16\n");
    }

    @Test
    @GradedTest(name="Test appending to a list", max_score=1)
    public void test_append() {
        IntList test = IntList.createList(1, 2, 4, 8, 16);
        test.append(32);
        assertEquals(test.toString(), "1 2 4 8 16 32\n");
    }

    public static void main(String[] args) {
        JUnitCore runner = new JUnitCore();
        runner.addListener(new GradedTestListenerJSON());
        runner.run(IntListTest.class);
    }
}
