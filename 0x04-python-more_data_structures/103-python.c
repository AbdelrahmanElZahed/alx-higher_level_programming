#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++) {
        printf(" %02x", (unsigned char)string[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}
