'''
testing
'''


def fun1(x):
    print(f'value stored at reference {id(x)} is {x}')
    x = 11
    print(f'value stored at reference {id(x)} is {x}')

def fun2(x):
    x = 'foo'   

y = 10
fun1(y)
print(f'reference in main function is {id(y)} of {y}')
for i in (
    40,dict(foo=1,bar=2),
    {1, 2, 3},
    'bar',
    ['foo', 'bar', 'baz']
):
    fun2(i)
    print(i)
