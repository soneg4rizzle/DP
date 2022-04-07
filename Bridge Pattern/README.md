# Bridge Pattern
> Abstraction과 Implementor를 분리해서 독립적 관계로 만들고 이 사이에 다리를 놓는 역할을 수행한다.  
> 브릿지 패턴을 이용하면 Abstraction만 볼 수 있고, 내부의 실체인 implementor를 숨길 수 있다.
> 외부와 내부를 분리하고 싶을 때 사용할 수 있다.

## #브릿지 패턴의 구조
![image](https://user-images.githubusercontent.com/96826443/162209110-b722b2be-7892-4de5-a290-1c2c550d03f1.png)  
> `Abstraction` : 기능 계층의 최상위 클래스, 구현 부분에 해당하는 클래스 인스턴스를 가지고 해당 인스턴스를 통해 구현부분의 메서드를 호출  
> `Implementor` : Abstraction의 기능을 구현하기 위한 인터페이스
> `RefindAbstraction` : 기능 계층에서 새로운 부분을 확장한 클래스
> `ConcreteImplementor` : 실제 기능을 구현  

## #브릿지 패턴의 사용
![image](https://user-images.githubusercontent.com/96826443/162209417-34171645-f722-4b17-8935-65f7013cbe34.png)  
> `Vehicle` : Abstraction  
> `Animal` : implemetor

## #브릿지 패턴의 예제코드1
```python
class Animal:
    def speak():
        pass

class Cat(Animal):
    def speak(self):
        print("a cat ", end='')

class Dog(Animal):
    def speak(self):
        print("a dog ", end='')

class Vehicle:
    def __init__(self, animal: Animal):
        self.animal = animal

    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        self.animal.speak()
        print('drives a car')

class Boat(Vehicle):
    def start(self):
        self.animal.speak()
        print('sails a boat')

class Airplane(Vehicle):
    def start(self):
        self.animal.speak()
        print('fly an airplane')

cat = Cat()
boat = Boat(cat)
boat.start()

dog = Dog()
car = Car(dog)
car.start()
```
* **output**
```
a cat sails a boat
a dog drives a car
```

## #브릿지 패턴의 예제코드2
```python

class Power:  # implementor class
    def powerUp(self):
        pass

    def powerDown(self):
        pass

class Engine(Power):
    def powerUp(self):
        print('engine power up')

    def powerDown(self):
        print('engine power down')


class Motor(Power):  # abstraction class
    def powerUp(Power):
        print('motor power up')

    def powerDown(Power):
        print('motor power down')

class Car:
    def __init__(self, power: Power):
        self.power = power

    def drive(self):
        self.power.powerUp()

    def stop(self):
        self.power.powerDown()

class Sedan(Car):
    def sedanOnlyFn(self):
        print('sedan only')

sedan = Sedan(Motor())
sedan.drive()
sedan.stop()
sedan.sedanOnlyFn()

```
* **output**
```
a cat sails a boat
a dog drives a car
```


