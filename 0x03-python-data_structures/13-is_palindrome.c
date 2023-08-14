#include "lists.h"
#include <stddef.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function that reverses the listint_t list
 * @head: ptr to the start node
 * Return: ptr to  the head of the reversed listint_t
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks for palindrome in a list
 * @head: pointer to the head in a list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reverse, *mid;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	reverse = reverse_listint(&tmp);
	mid = reverse;

	tmp = *head;
	while (reverse)
	{
		if (tmp->n != reverse->n)
			return (0);
		tmp = tmp->next;
		reverse = reverse->next;
	}
	reverse_listint(&mid);
	return (1);
}
