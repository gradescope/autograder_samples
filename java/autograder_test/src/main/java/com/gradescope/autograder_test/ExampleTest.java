package com.gradescope.autograder_test;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gradescope.jh61b.grader.GradedTest;
import com.gradescope.jh61b.grader.GradedTestRunnerJSON;
import com.gradescope.jh61b.grader.GradedTestListenerJSON;
import org.junit.runner.RunWith;
import org.junit.runner.JUnitCore;

// @RunWith(GradedTestRunnerJSON.class)
public class ExampleTest {
  @Test
  @GradedTest(name="Basic JUnit Runner Test", number="1", max_score=1.0)
  public void test_simple1() {
    assertEquals(5, 5);
    System.out.println("Hello");
  }

  public static void main(String[] args) {
    JUnitCore runner = new JUnitCore();
    runner.addListener(new GradedTestListenerJSON());
    runner.run(ExampleTest.class);
  }
}
