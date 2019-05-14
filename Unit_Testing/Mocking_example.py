from mock import Mock

class Foo():
    _fooValue = 123

    def callFoo(self):
        print ("Foo:callFoo_")
    
    def doFoo(self, argValue):
        print("FooLdoFoo:input = ", argValue)

# create the mock object
mockFoo = Mock(spec = Foo)

# accessing the mocked attritbutes
print(mockFoo)

print(mockFoo._fooValue) #mocking the methods

print(mockFoo.callFoo())

# accessing the missing attributes
print(mockFoo._fooBar)
mockFoo.callFooBar()

