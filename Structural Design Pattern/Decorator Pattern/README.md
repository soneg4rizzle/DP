# 데코레이터 패턴(Decorator Pattern)
> 데코레이터 패턴이란 주어진 상황이나 용도에 맞게 객체의 기능을 확장시키는 패턴을 말합니다.
> '데코레이터'라는 이름처럼 Object를 꾸며주는 역할을 수행합니다.

![image](https://user-images.githubusercontent.com/96826443/161489754-718748cc-ccc0-46ff-b8d3-450ed39347f8.png)


## 데코레이터 패턴의 적용
* `Component(내용물)` : 실질적 인스턴스를 다루는 클래스로, 주로 ConcreteComponent, Decorator, ConcreteDecorator가 사용하는 공통 기능을 정의합니다.
* `ConcreteComponent(구체적인 내용)` : 컴포넌트 클래스를 상속받고 기본 기능을 구현하는 클래스입니다.
* `Decorator(장식)` : ConcreteDecorator class 들이 공통적으로 사용하는 기능을 정의합니다.
* `ConcreteDecorator(구체적인 장식)` : Decorator class 를 상속받고 부가적으로 기능을 추가하여 사용하는 클래스입니다.
![image](https://user-images.githubusercontent.com/96826443/161487257-b8144a57-f7e0-4fd8-a03f-9d76c4d74cfb.png)


## 데코레이터 패턴의 장단점
> **장점**
> 기존에 있는 기능에서 부가적으로 기능을 추가하고 싶을 때 데코레이터 클래스의 기능을 확장시키는 것으로 유연하게 대처가 가능합니다.
> 데코레이터 패턴에서 사용하는 "위임" 방법은 코드들이 서로 느슨하게 결합하는 상태를 유지하기 때문에 프레임워크의 소스나 오브젝트의 관계를 변형하지 않고도 새로운 오브젝트를 만들 수 있다는 점이 큰 장점입니다.

> **단점** :데코레이터 클래스가 필요 이상으로 늘어나게 된다면 의미없는 객체들이 늘어나게 되고 이로 인해 코드가 불필요하게 복잡해지고 가독성이 떨어지게 됩니다.

## 데코레이터 패턴 예제코드
```python
class Display():  # Component
    def getColumns(self):
        pass

    def getRows(self):
        pass

    def getRowText(self, row):
        pass

    def show(self):
        n = self.getRows()
        for i in range(n):
            print(self.getRowText(i))


class StringDisplay(Display):  # Concrete Component

    def __init__(self, letters):
        self.letters = letters

    def getColumns(self):
        return len(self.letters)

    def getRows(self):
        return 1

    def getRowText(self, row):
        if row == 0:
            return self.letters
        else:
            return -1


class Deco(Display):  # Decorator
    def __init__(self, display: Display):
        self.display = display


class SideBorder(Deco):  # Concrete Decorator 1
    def __init__(self, display, deco):
        super().__init__(display)
        self.borderDeco = deco

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return self.borderDeco + self.display.getRowText(row) + self.borderDeco


class FullBorder(Deco):  # Concrete Decorator 2
    def __init__(self, display):
        super().__init__(display)

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return 1 + self.display.getRows() + 1

    def makeLine(self, deco, count):
        buffer = ""
        for i in range(count):
            buffer += deco
        return buffer

    def getRowText(self, row):
        if row == 0: # 첫 줄과 마지막 줄에 + decoration 
            return "+" + self.makeLine("-", self.display.getColumns()) + "+"
        elif row == (self.display.getRows() + 1):
            return "+" + self.makeLine("-", self.display.getColumns()) + "+"
        else:
            return "|" + self.display.getRowText(row-1) + "|"


# b1 = StringDisplay("hello")
# b2 = SideBorder(b1, "#")
# #b2 = SideBorder(StringDisplay("hello"), "#)
# b3 = FullBorder(b2)
# #b3 = FullBorder(SideBorder(StringDisplay("hello"), "#"))
# b1.show()
# b2.show()
# b3.show()

# b1 = StringDisplay("hello, world")
# b1 = FullBorder(b1)
# b1.show()


a = StringDisplay("hello")
a = FullBorder(a)
# a = FullBoder(StringDisplay("hello"))
a = SideBorder(a, "*")
# a = SideBorder(FullBoder(StringDisplay("hello")), "*")
a = FullBorder(a)
# a = FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*"))
a = FullBorder(a)
# a = FullBorder(FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*")))
a = SideBorder(a, "/")
# a = SideBorder(FullBorder(FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*"))), "/")
a.show()
```

```python
a = StringDisplay("hello")
a = FullBorder(a)
# a = FullBoder(StringDisplay("hello"))
a = SideBorder(a, "*")
# a = SideBorder(FullBoder(StringDisplay("hello")), "*")
a = FullBorder(a)
# a = FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*"))
a = FullBorder(a)
# a = FullBorder(FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*")))
a = SideBorder(a, "/")
# a = SideBorder(FullBorder(FullBorder(SideBorder(FullBoder(StringDisplay("hello")), "*"))), "/")
a.show()
```
```출력결과``` : ![image](https://user-images.githubusercontent.com/96826443/161525849-bf674ac7-8f8b-4057-8f55-a5f2a0fa4a49.png)

## 결론
> 예를 들어, 커피를 만든다고 할 때 카페라떼, 에스프레소, 바나나라떼 등의 커피를 만들기 위해서는 공통재료인 에스프레소를 제외하고 우유, 바나나시럽 등의 많은 재료를 조합해야 합니다.
> 때문에 무엇을 완성하기 위해 많은 재료가 필요할 때 Decorator Pattern을 유용하게 사용할 수 있습니다.
> 데코레이터 디자인 패턴을 적절히 이용하면 필요한 기능을 유연하게 추가할 수 있고 이러한 과정을 통해 객체를 더 목적에 알맞게 설정할 수 있습니다.

## 출처
* [[디자인 패턴] 데코레이터(Decorater) 패턴이란?](https://steady-coding.tistory.com/391)
* [[디자인패턴 : Decorator]](https://refactoring.guru/design-patterns/decorator)
* [[Design Pattern] 데코레이터 패턴(Decorator pattern)에 대하여](https://coding-factory.tistory.com/713)

                  
