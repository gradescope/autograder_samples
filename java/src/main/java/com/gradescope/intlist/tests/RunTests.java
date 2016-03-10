package com.gradescope.intlist.tests;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runner.JUnitCore;

import com.gradescope.intlist.tests.IntListTest;
import com.gradescope.jh61b.grader.GradedTestListenerJSON;

public class RunTests {
    @RunWith(Suite.class)
    @Suite.SuiteClasses({
            IntListTest.class
                })
    private class IntListTestSuite{
    }

    public static void main(String[] args) {
        JUnitCore runner = new JUnitCore();
        runner.addListener(new GradedTestListenerJSON());
        runner.run(IntListTestSuite.class);
    }
}
