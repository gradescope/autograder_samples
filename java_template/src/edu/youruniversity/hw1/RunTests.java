// Define whatever package name you want
package edu.youruniversity.hw1;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

// Import your test classes here
import edu.youruniversity.hw1.MyTestClass;
// This test listener produces the formatted JSON output for Gradescope
import com.gradescope.jh61b.grader.GradedTestListenerJSON;

// Define a test suite, with the classes that contain the tests you wish to run
@RunWith(Suite.class)
@Suite.SuiteClasses({
        MyTestClass.class
            })
// The main class to be executed; this is the entry point for your tests
public class RunTests {
    public static void main(String[] args) {
        JUnitCore runner = new JUnitCore();
        // Attach a listener for JSON output
        runner.addListener(new GradedTestListenerJSON());
        // Run the test suite defined within this class
        Result r = runner.run(RunTests.class);
    }
}
