# Object-Oriented Programming OOP

> `class` Objects: public
>
>
>
>> Python Properties
>>> attributes @property -> decorators
>
> > @classmethod
>
> > Operator Overloading
> > >if you want to overload add sign to add two classes you should define what you want to be added
>
> > Special Method names (`__add__`)

```python

    def __add__(self,other):
        galleons= self.galleons+other.galleons
        sickles= self.sickles+other.sickles
        knuts= self.knuts+other.knuts
        return Vault(galleons,sickles,knuts)
   ```
