#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string.
 * @p: The Python object to be checked and printed.
 */
void print_python_string(PyObject *p)
{
	/* Check if the object is a string */
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n[ERROR] Invalid String Object\n");
		return;
	}

	/* If it's a string, get the string value and its length */
	const char *str = PyUnicode_AsUTF8(p);
	Py_ssize_t length = PyUnicode_GetLength(p);

	/* Determine the string type (ASCII or Unicode) */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("[.] string object info\n  type: compact ascii\n  length: %zd\n  value: %s\n", length, str);
	else
		printf("[.] string object info\n  type: compact unicode object\n  length: %zd\n  value: %s\n", length, str);
}
