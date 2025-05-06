class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")      
    def __str__(self):
        return f"Animal: {self.name}"
    def __repr__(self): 
        return f"Animal({self.name})"
    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.name == other.name
        return False
    def __hash__(self):
        return hash(self.name)  
    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.name < other.name
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Animal):
            return self.name <= other.name
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Animal):
            return self.name > other.name
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Animal):
            return self.name >= other.name
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, Animal):
            return self.name != other.name
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, Animal):
            return Animal(self.name + other.name)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Animal):
            return Animal(self.name.replace(other.name, ""))
        return NotImplemented       
    def __mul__(self, other):
        if isinstance(other, int):
            return Animal(self.name * other)
        return NotImplemented
    def __truediv__(self, other):
        if isinstance(other, int):
            return Animal(self.name[:len(self.name)//other])
        return NotImplemented
    def __floordiv__(self, other):
        if isinstance(other, int):
            return Animal(self.name[:len(self.name)//other])
        return NotImplemented
    def __mod__(self, other):
        if isinstance(other, int):
            return Animal(self.name[:len(self.name)%other])
        return NotImplemented
    def __pow__(self, other):
        if isinstance(other, int):
            return Animal(self.name * other)
        return NotImplemented
    def __and__(self, other):
        if isinstance(other, Animal):
            return Animal(self.name + other.name)
        return NotImplemented
    def __or__(self, other):
        if isinstance(other, Animal):
            return Animal(self.name + other.name)
        return NotImplemented
    def __xor__(self, other):
        if isinstance(other, Animal):
            return Animal(self.name + other.name)
        return NotImplemented
    def __invert__(self):
        return Animal(self.name[::-1])
    def __call__(self, *args, **kwargs):
        return f"{self.name} called with args: {args} and kwargs: {kwargs}"
    def __enter__(self):
        print(f"{self.name} is being entered")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{self.name} is being exited")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True
    def __sizeof__(self):
        return len(self.name) * 8
    def __del__(self):
        print(f"{self.name} is being deleted")
        del self.name
    def __format__(self, format_spec):  
        return f"{self.name:{format_spec}}"
a1 = Animal("Cat")
a2 = Animal("Dog")

print(a1 + a2)      # Animal: CatDog
print(a1 - a2)      # Animal: Cat (since "Dog" not in "Cat")
print(a1 * 3)       # Animal: CatCatCat
print(a1 / 2)       # Animal: Ca
print(~a1)          # Animal: taC
print(a1())         # Cat called with args: () and kwargs: {}
print(format(a1, '^10'))  # '   Cat    '

with a1:
    print("Inside context")
