#include "Python.h"
#include "stdio.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: the list object from Python whose elements and length will be printed
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %d\n", (int) PyList_Size(p));
	printf("[*] Allocated = %d\n", (int) PyByteArray_Size(p));

	for(i = 0; i < (int) PyList_Size(p); i++)
	{
		if (PyLong_Check(PyList_GetItem(p, i)))
			printf("Element %d: int\n", i);
		else if (PyFloat_Check(PyList_GetItem(p, i)))
			printf("Element %d: float\n", i);
		else if (PyUnicode_Check(PyList_GetItem(p, i)))
			printf("Element %d: str\n", i);
		else if (PyList_Check(PyList_GetItem(p, i)))
			printf("Element %d: list\n", i);
		else if (PyTuple_Check(PyList_GetItem(p, i)))
			printf("Element %d: tuple\n", i);
	}
}
