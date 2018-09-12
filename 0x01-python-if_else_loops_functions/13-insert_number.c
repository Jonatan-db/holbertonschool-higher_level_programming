#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* insert_node - inserts a node to be in order
* @head: so nice. the tip of the long list.
* @number: the number we want tp stick in so deep in the linked list
*
* Description: inserts a node in order and requires the use of a temp node
* Return: the address of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (temp)
	{
		/* for when the next number is smaller than numb */
		if ((temp->n <= number) && (temp->next && (temp->next->n >= number)))
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		/* this is when you add new node to the end */
		else if (temp->n <= number && !(temp->next))
		{
			new->next = NULL;
			temp->next = new;
			return (new);
		}
		/* when the number is small and first */
		else if (temp->n > number)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		temp = temp->next;
	}
	return (NULL);
}
