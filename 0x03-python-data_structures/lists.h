#ifndef LISTS_H
#define LISTS_H


#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s  - this is a singly linked list
 * @n: an integer
 * @next: points to the nest node in the list
 * Description: this is a singly linked list node structure
 */

typedef struct listint_s
{
        int n;
        struct listint_s *nest;
}listint_s;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_polindrome(listint_t **head);

#endif /* LISTS_H */
