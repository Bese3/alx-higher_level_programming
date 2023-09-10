#include<stdio.h>
#include"lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome.
 *
 * @head: The head parameter is a pointer
 * to a pointer of type listint_t. It represents the head
 * of a linked list.
 *
 * Return: an integer value. If the given linked list
 * is a palindrome, it will return 1. Otherwise, it
 * will return 0.
 */
int is_palindrome(listint_t **head)
{
listint_t *first_half;
listint_t *prev;
listint_t *curr;
listint_t *next;
listint_t *second_half;
listint_t *slow = *head;
listint_t *fast = *head;
if (head == NULL || *head == NULL)
return (1);

while (fast != NULL && fast->next != NULL && fast->next->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}
first_half = *head;
prev = NULL;
curr  = slow->next;
while (curr != NULL)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}
slow->next = prev;
second_half = slow->next;
while (first_half != NULL && second_half != NULL)
{
if (first_half->n != second_half->n)
{
return (0);
}
first_half = first_half->next;
second_half = second_half->next;
}
return (1);
}
