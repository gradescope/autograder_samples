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
        IntList head = new IntList(a[0]);
        IntList prev = head;
        for(int i=1; i < a.length; i++){
            prev.next = new IntList(a[i]);
            prev = (IntList) prev.next;
        }
        return head;
    }

    /**
     * Appends value to the end of the list
     */
    public AbstractIntList append(int value){
        if(this.next == null){
            this.next = new IntList(value);
            return this.next;
        }else{
            return this.next.append(value);
        }
    }

    /**
     * Returns true if the IntList contains the value
     */
    public boolean contains(int value){
        if(this.head == value){
            return true;
        }else if(this.next != null){
            return this.next.contains(value);
        }else{
            return false;
        }
    }

    /**
     * Converts an IntList to a string
     */
    public String toString(){
        if(this.next != null){
            return this.head + " " + this.next.toString();
        }else{
            return this.head + "\n";
        }
    }
}
