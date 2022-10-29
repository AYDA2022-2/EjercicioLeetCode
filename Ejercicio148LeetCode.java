class Solution {
    public ListNode sortList(ListNode puntero) {
        //caso Base 
        if(puntero == null || puntero.next == null) return puntero;
        
        //separando por la mitad de la lista 
        ListNode l1 = puntero, l2 = separarMitad(puntero);
        
        //ordenando la izquierda de la lista
        l1 = sortList(l1);
        
        //ordenando la derecha de la lista
        l2 = sortList(l2);
        
        //Mezclar todas las listas
        ListNode aux = new ListNode(), res = aux;
        
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                res.next = l1;
                l1 = l1.next;
            }else{
                res.next = l2;
                l2 = l2.next;
            }
            res = res.next;
        }
        
        if(l2 != null) {
            res.next = l2;
        }else{
            res.next = l1;
        }
        //Returna el puntero del nodo
        return aux.next;
    }
    private ListNode separarMitad(ListNode puntero){
        ListNode ln = puntero, lm = puntero, pre = null;
        while(lm != null && lm.next != null){
            pre = ln;
            ln = ln.next;
            lm = lm.next.next;
        }
        pre.next = null;
        return ln;
    }
}