#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - function that checks if a singly linked list has a
 * cycle in it
 * @list: singly linked list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;/** moves one node at a time */
		fast = fast->next->next;/** moves two nodes at a time */

		if (slow == fast)
			return (1);
	}
	return (0);
}
