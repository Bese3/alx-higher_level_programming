#include "lists.h"

/**
 * is_palindrome - checks if linked list @head is a palindrome
 * @head: the linked list to be checked if it's a palindrome
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i, list_len = (int) listint_len(*head);
	int *h = malloc(sizeof(int) * list_len); /* Contains all n's in *head*/
	listint_t *head_copy = *head;

	if (!*head || ((*head)->n == 0 && (*head)->next == NULL))
	{
		free(h);
		return (1);
	}

	for (i = 0; i < list_len; i++)
	{
		h[i] = (*head)->n;
		*head = (*head)->next;
	}
	*head = head_copy; /* Return the head of the list back to the first item */

	for (i = 0; i < list_len; i++)
	{
		if (h[i] == h[list_len - 1 - i])
			continue;
		free(h);
		return (0);
	}

	free(h);
	return (1);
}

/**
 * listint_len - length of a list
 * @h:pointer to list element
 * Return: size of list
 */
size_t listint_len(const listint_t *h)
{
	size_t len = 0;

	while (h)
	{
		len++;
		h = h->next;
	}

	return (len);
}
