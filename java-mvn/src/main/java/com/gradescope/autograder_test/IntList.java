package com.gradescope.autograder_test;

public class IntList{
    int head;
    IntList next;

    public IntList(int head){
        this.head = head;
        this.next = null;
    }

    /**
     * Creates an IntList from a variable number of arguments
     */
    public static IntList createList(int... a){
        IntList head = new IntList(a[0]);
        IntList prev = head;
        for(int i=1; i < a.length; i++){
            prev.next = new IntList(a[i]);
            prev = prev.next;
        }
        return head;
    }

    /**
     * Appends value to the end of the list
     */
    public IntList append(int value){
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
