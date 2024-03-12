#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - function
 * @head: argument
 * @number:int
 * Return: return
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a = *head;
	listint_t *b = malloc(sizeof(listint_t));

	if (!b)
		return (NULL);
	b->next = NULL;
	b->n = number;

	if (b->n < a->n || !a)
	{
		b->next = a;
		return (*head = b);
	}

	while (a)
	{
		if (b->n < a->next->n || !a->next)
		{
			b->next = a->next;
			a->next = b;
			return (a);
		}
		a = a->next;
	}
	return (NULL);



}
