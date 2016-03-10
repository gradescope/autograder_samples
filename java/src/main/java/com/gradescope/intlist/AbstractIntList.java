package com.gradescope.intlist;

public abstract class AbstractIntList{
    protected int head;
    protected AbstractIntList next;

    public AbstractIntList(int head){
        this.head = head;
        this.next = null;
    }

    /**
     * Appends value to the end of the list
     */
    public abstract AbstractIntList append(int value);

    /**
     * Returns true if the AbstractIntList contains the value
     */
    public abstract boolean contains(int value);

    /**
     * Converts an AbstractIntList to a string
     *
     * The last element should be
     * followed by a newline instead of a space.
     */
    public abstract String toString();

    /**
     * Compares each element of both lists to see if they're the same
     */
    public boolean equals(Object other){
        if (other instanceof AbstractIntList){
            AbstractIntList otherList = (AbstractIntList) other;
            if(this.head == otherList.head){
                if(this.next == null && otherList.next == null){
                    return true;
                }else if(this.next != null && otherList.next != null){
                    return this.next.equals(otherList.next);
                }else{
                    return false;
                }
            }else{
                return false;
            }
        }else{
            return false;
        }
    }
}
