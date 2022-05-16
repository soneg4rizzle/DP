# 전략패턴(Strategy Pattern)
> Open-Closed Principle(확장성O, 수정X) 과 유사한 패턴으로, 런타임 중 알고리즘을 선택할 수 있게 합니다.

## 전략패턴의 구조
![image](https://user-images.githubusercontent.com/96826443/163767059-fa26bb68-0515-43b6-b306-5e3e812af169.png)

## 전략패턴 예제코드
```python
class Animal: # Strategy
    def speak(self):
        pass

class Cat(Animal): # Concrete Strategy
    def speak(self):
        print("meow")

class Lion(Animal): # Concrete Strategy
    def speak(self):
        print("roar")

def makeSpeak(animal: Animal): # Context 1
    animal.speak()

def createAnimal(input_str: str) -> Animal: # Context 2
    if input_str == "cat":
        return Cat()
    elif input_str == "lion":
        return Lion()
    else:
        print('등록되지 않은 개체입니다.')


input_str = input('choose animal : ')

animal = createAnimal(input_str)
makeSpeak(animal)

```
### 역할
* Strategy : 인터페이스/추상 클래스로 외부에서 호출할 수 있는 방법(Animal Class의 speak() 메소드)를 명시한다.
* ConcreteStrategy : 전략패턴에서 명시한 알고리즘을 실제로 구현(Cat, Lion Class의 speak() 메소드)  
* Context : 전략패턴을 이용하는 역할을 수행(createAnimal(argument) 메소드) -> 동적으로 런타임 중 알고리즘을 선택할 수 있게 한다.
