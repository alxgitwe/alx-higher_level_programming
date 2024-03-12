#include "lists.h"

/**
 * check_cycle - function
 * @list: list
 * Return: return
 */

int check_cycle(listint_t *list)
{
	listint_t *c = list;
	listint_t *d = list;

	while (d->next && d)
	{
		c = c->next;
		d = d->next->next;
		if (c == d)
			return (1);
	} return (0);

}
