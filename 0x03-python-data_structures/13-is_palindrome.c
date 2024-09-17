#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer to the head of the list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *first_half;
	listint_t *reversed_second_half;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	second_half = slow;
	reversed_second_half = reverse_list(second_half);
	first_half = *head;
	while (reversed_second_half != NULL)
	{
		if (first_half->n != reversed_second_half->n)
		{
			result = 0;
			break;
		}
		first_half = first_half->next;
		reversed_second_half = reversed_second_half->next;
	}
	return (result);
}
