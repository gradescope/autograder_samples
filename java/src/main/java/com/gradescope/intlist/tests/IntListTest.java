package com.gradescope.intlist.tests;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gradescope.jh61b.grader.GradedTest;

import com.gradescope.intlist.IntList;
import com.gradescope.intlist.RefIntList;
import com.gradescope.intlist.AbstractIntList;

public class IntListTest {
    @Test
    @GradedTest(name="Test creating an IntList from varargs", max_score=1)
    public void test_varargs() {
        AbstractIntList test = IntList.createList(1, 2, 4, 8, 16);
        assertEquals(test, RefIntList.createList(1, 2, 4, 8, 16));
    }

    @Test
    @GradedTest(name="Test appending to a list", max_score=1)
    public void test_append() {
        AbstractIntList test = new IntList(RefIntList.createList(1, 2, 4, 8, 16));
        test.append(32);
        assertEquals(test, RefIntList.createList(1, 2, 4, 8, 16, 32));
    }

    @Test
    @GradedTest(name="Test converting a list to a string", max_score=1)
    public void test_to_string() {
        AbstractIntList test = new IntList(RefIntList.createList(1, 2, 4, 8, 16));
        assertEquals(test.toString(), "1 2 4 8 16\n");
    }
}
