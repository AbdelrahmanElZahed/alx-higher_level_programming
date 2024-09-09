#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	while (rabbit != NULL && rabbit->next != NULL)
	{
		/* Move turtle by 1 step */
		turtle = turtle->next;
		/* Move rsbbit by 2 steps */
		rabbit = rabbit->next->next;
		/* If they meet, there is a cycle */
		if (turtle == rabbit)
			return (1);
	}
	/* If rabbit reaches the end, there is no cycle */
	return (0);
}

