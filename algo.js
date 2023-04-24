var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let first = dummy;
    let second = dummy;

    // Move first pointer n nodes ahead of second pointer
    for(let i = 0; i <= n; i++){
        first = first.next;
    }

    // Move both pointers until first pointer reaches the end of the list
    while(first !== null){
        second = second.next;
        first = first.next;
    }

    // Remove the nth node from the end of the list
    second.next = second.next.next;

    return dummy.next;
};
