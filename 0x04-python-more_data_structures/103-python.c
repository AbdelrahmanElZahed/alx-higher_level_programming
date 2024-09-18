#include <Python.h>
#include <stdio.h>
#include "103-python.h"

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A PyObject representing a Python bytes object.
 *
 * This function checks if the given PyObject is a valid bytes object.
 * If not, it prints an error message. If it is a valid bytes object,
 * it prints the size of the bytes object, the string it represents,
 * and the first up to 10 bytes in hexadecimal format.
 */

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	char *string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: A PyObject representing a Python list object.
 *
 * This function checks if the given PyObject is a valid list object.
 * If it is a valid list object, it prints the size of the list, the
 * number of elements allocated, and the type of each element in the list.
 * If an element is a bytes object, it calls print_python_bytes to print
 * detailed information about that bytes object.
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}
