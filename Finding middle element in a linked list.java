class Solution
{
    int getMiddle(Node head)
    {
         // Your code here.
        Node slow= head;
        Node fast= head;
        while(fast.next!= null && fast.next.next!=null) {
            slow= slow.next;
            fast= fast.next.next;
        }
        if(fast.next!=null)
            return slow.next.data;
        return slow.data;
    }
}
