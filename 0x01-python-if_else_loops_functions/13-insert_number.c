#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function in C that inserts a number into a
 * sorted singly linked list
 * @head: head if the list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL)
	new_node->number = number;
	new_node->next = NULL;

	/**
	 * if the list is empty or the new value should
	 * be inserted at the beginning
	 */
	if (head == NULL || (*head)->number > number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	/** Find the correct position to insert the new node */
	current = *head;
	while (current->next != NULL && current->next->number < number)
		current = current->next;

	/** insert the node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
