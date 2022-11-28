#include "lists.h"

/*
 * check_cycle - checks if there's a cycle in the linked list that's passed in
 * @list: the list to be checked if there's a cycle in it
 *
 * Return: 1 if there's a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	int i, j;
	listint_t *copy = list, *temp;

	for (i = 0; copy != NULL; i++)
	{
		j = 0;
		temp = list;
		while (j < i)
		{
			if (copy == temp)
				return (1);
			temp = temp->next;
			j++;
		}
		copy = copy->next;
	}

	return (0);
}
