# 컴포지트 패턴(Composite Pattern)
> 컴퓨터의 파일 시스템에서는 디렉토리 안에 또 다른 하위 디렉토리가 존재하고, 그 안에는 또 다른 파일이나 디렉토리가 존재할 수 있다.
> 이처럼 재귀적인 형태를 띄는 구조에서, 폴더와 파일을 같은 종류로 취급하는 것을 통해 트리구조로 간편하게 구성할 수 있다.
* 하나의 객체와 객체가 들어있는 그룹을 같은 타입(동일 인터페이스를 갖는다)으로 취급
* 그룹의 객체들은 리스트 안에 들어가게된다.

## 구조
![image](https://user-images.githubusercontent.com/96826443/163335570-fc681ce8-d9b2-436a-a054-393f73f27cb9.png)
> Leaf : 내용물(파일)을 표시하는 역할(내부에는 다른 것을 추가할 수 없음)
> Composite : 그릇(폴더)을 나타내는 역할, leaf 역할이나 composite 역할 추가 가능
> Component : leaf와 composite의 공통적인 상위클래스로 실현

## 예제코드
```python
class Animal:
    def speak(self): # composite function
        pass


class Cat(Animal): # leaf
    def speak(self):
        print('meow')


class Dog(Animal): # leaf
    def speak(self):
        print('bark')


class AnimalGroup(Animal): # composite
    def __init__(self):
        self.animals = []

    def add(self, animal: Animal):
        self.animals.append(animal)

    def speak(self):
        print('group speaking.')
        for animal in self.animals:
            animal.speak()


cat_group = AnimalGroup()
cat_group
cat_group.add(Cat())
cat_group.add(Cat()
cat_group.add(Cat())

dog_group = AnimalGroup()
dog_group.add(Dog())
dog_group.add(Dog())

zoo = AnimalGroup()
zoo.add(cat_group)
zoo.add(dog_group)

zoo.speak()
```
## 출력결과
![image](https://user-images.githubusercontent.com/96826443/163341530-cdfbd87d-04c2-4121-9eed-779c592b1273.png)
  
## 장점
* Composite Object(폴더) 안에 존재하는 모든 object에 대해서 트리 구조의 형태로 관리가 용이해진다.
* 트리 루트에서 함수(fn) 하나만 호출하면 폴더를 따라가며 하위 내용물들을 모두 접근할 수 있다.
