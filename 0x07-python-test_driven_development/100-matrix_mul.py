#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if i is not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if j is not isinstance(j, list):
            raise TypeError("m_b must be a list of lists")
        