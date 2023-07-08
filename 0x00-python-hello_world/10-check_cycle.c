#include<stdio.h>
#include"lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 *
 * @list: The parameter "list" is a pointer
 * to the head of a linked list of integers.
 *
 * Return: 1 if there is a cycle in the linked
 * list, and 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
listint_t *fast;
listint_t *slow;
fast = slow  = list;
while ((fast != NULL) && (fast->next != NULL) && (fast->next->next != NULL))
{
fast = fast->next->next;
slow = slow->next;
if (fast == slow)
return (1);
}
return (0);
}
