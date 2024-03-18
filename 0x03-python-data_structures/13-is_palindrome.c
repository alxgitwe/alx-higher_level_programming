#include "lists.h"

/**
 * plndrm - function
 *
 * @head: struct
 *
 * @endlst: struct
 *
 * Return: return
 */
int plndrm(listint_t **head, listint_t *endlst)
{
        if (endlst == NULL)
                return (1);
        if ((*head)->n == endlst->n && plndrm(head, endlst->next))
        {
                *head = (*head)->next;
                return (1);
        }
        return (0);


}

/**
 * is_palindrome - function
 *
 * @head: struct
 *
 * Return: return
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);
	return (plndrm(head, *head));
}
