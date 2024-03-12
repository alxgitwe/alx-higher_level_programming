#include "lists.h"

/**
 * check_cycle - function
 * @list: list
 * Return: return
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	while (b->next && b)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	} return (0);

}
