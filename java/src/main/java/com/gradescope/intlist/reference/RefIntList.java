package com.gradescope.intlist.reference;

import com.gradescope.intlist.AbstractIntList;

public class RefIntList extends AbstractIntList{

    public RefIntList(int head) {
        super(head);
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
