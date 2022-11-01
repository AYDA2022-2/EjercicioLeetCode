

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, puntero: ListNode):
        return self.mergeSort(puntero)

    def mergeSort(self, puntero):

        # condiciones
        if not puntero or not puntero.next:
            return puntero

        l, r = self.listSeparar(puntero)
        l = self.mergeSort(l)
        r = self.mergeSort(r)
        # mezcla
        aux = ListNode(None)
        cur = aux
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = r or l
        return aux.next

    def listSeparar(self, puntero):

        # encontrar la mitad
        mit, lent, rap = puntero, puntero, puntero
        while rap and rap.next:
            mit = lent
            lent = lent.next
            rap = rap.next.next
        # parte izquierda
        mit.next = None
        l = puntero
        # parte derecha
        r = lent
        return r, l