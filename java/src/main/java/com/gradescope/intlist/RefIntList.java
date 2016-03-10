package com.gradescope.intlist;

import com.gradescope.intlist.AbstractIntList;

public class RefIntList extends AbstractIntList{

    public RefIntList(int head) {
        super(head);
    }

    /**
     * This copy constructor is needed for test cases; do not touch
     */
    public RefIntList(AbstractIntList list){
        this(list.head);
        if(list.next != null){
            this.next = new RefIntList(list.next);
        }
    }
    /**
     * Creates an IntList from a variable number of arguments
     */
    public static AbstractIntList createList(int... a){
        RefIntList head = new RefIntList(a[0]);
        RefIntList prev = head;
        for(int i=1; i < a.length; i++){
            prev.next = new RefIntList(a[i]);
            prev = (RefIntList) prev.next;
        }
        return head;
    }

    /**
     * Appends value to the end of the list
     */
    public AbstractIntList append(int value){
        if(this.next == null){
            this.next = new RefIntList(value);
            return this.next;
        }else{
            return this.next.append(value);
        }
    }

    /**
     * Returns true if the IntList contains the value
     */
    public boolean contains(int value){
        System.out.println("Reference");
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
     *
     * The last element should be
     * followed by a newline instead of a space.
     */
    public String toString(){
        if(this.next != null){
            return this.head + " " + this.next.toString();
        }else{
            return this.head + "\n";
        }
    }
}
