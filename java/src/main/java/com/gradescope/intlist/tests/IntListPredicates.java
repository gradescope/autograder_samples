package com.gradescope.intlist.tests;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gradescope.jh61b.grader.GradedTest;

import com.gradescope.intlist.IntList;
import com.gradescope.intlist.RefIntList;
import com.gradescope.intlist.AbstractIntList;

public class IntListPredicates {
    @Test
    @GradedTest(name="Test Intlist.contains", max_score=1)
    public void test_contains() {
        AbstractIntList test = RefIntList.createList(1, 2, 4, 8, 16);
        IntList studentList = new IntList(test);
        assertTrue(studentList.contains(4));
    }

    @Test
    @GradedTest(name="Test Intlist.contains for nonexistant item", max_score=1)
    public void test_contains_missing() {
        AbstractIntList test = RefIntList.createList(1, 2, 4, 8, 16);
        IntList studentList = new IntList(test);
        assertFalse(studentList.contains(5));
    }
}
