package com.gradescope.intlist;

import com.gradescope.intlist.AbstractIntList;

public class IntList extends AbstractIntList{

    /**
     * Calls the parent constructor
     */
    public IntList(int head){
        super(head);
    }

    /**
     * This copy constructor is needed for test cases; do not touch
     */
    public IntList(AbstractIntList list){
        this(list.head);
        if(list.next != null){
            this.next = new IntList(list.next);
        }
    }
    /**
     * Creates an IntList from a variable number of arguments
     */
    public static AbstractIntList createList(int... a){
        // TODO: Fill me in!
    }

    /**
     * Appends value to the end of the list
     */
    public AbstractIntList append(int value){
        // TODO: Fill me in!
    }

    /**
     * Returns true if the IntList contains the value
     */
    public boolean contains(int value){
        // TODO: Fill me in!
    }

    /**
     * Converts an IntList to a string.
     *
     * The last element should be
     * followed by a newline instead of a space.
     */
    public String toString(){
        // TODO: FIll me in!
    }
}
