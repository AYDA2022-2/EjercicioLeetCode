# EjercicioLeetCode.

*148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

<p align="center"><img src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" height="350px"></p>

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

<p align="center"><img src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" height="350px"></p>

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

## Ejercicio.

[Ejercicio](https://leetcode.com/problems/sort-list/) 

## Vídeo.
[Vídeo](https://www.youtube.com/watch?v=g5yfYazaLdM) 

## Conclusiones.
•	Puede resultar un algoritmo sencillo, si se sabe cómo utilizar la ordenación por mezcla. Todo lo que tenemos que hacer es dividir nuestra lista en dos partes, ordenar la primera mitad, luego ordenar la segunda mitad y finalmente fusionar estas dos partes.                                                                         
•	La complejidad temporal es O(n log n), porque es la complejidad clásica de la ordenación por fusión.                                                                  
•La complejidad espacial es O(log n), porque utilicé una recursión que puede ser log n de profundidad.





