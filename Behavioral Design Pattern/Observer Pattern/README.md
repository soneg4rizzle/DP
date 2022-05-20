# 옵저버 패턴(Observer Pattern)
> 옵저버 패턴은 객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다.

## 옵저버패턴 구조
![image](https://user-images.githubusercontent.com/96826443/169458410-28aaabac-dba5-47b1-86f2-917ad4f4f048.png)
![image](https://user-images.githubusercontent.com/96826443/169458916-56cb4e2b-7b21-40e2-89f8-6013c3beff5b.png)
* Observer Class : 이벤트를 감시하는 Observer, notify 메소드는 관찰 대상이 발행한 메시지 이외에, 옵서버 자신이 생성한 인자값을 전달할 수도 있다.
* Subject Class : 새로운 옵저버를 목록에 등록하거나 제거한다.

## 옵저버패턴의 사용 이유
> 이벤트가 일어났는지 특정 시간 단위로 계속해서 확인해야 하는데, 이러한 방법(polling)은 불필요한 자원의 낭비가 발생한다.(오버헤드 증가)  
> 옵저버패턴이란, 어떤 이벤트가 발생했을 때, observer들이 바로 반응하는 패턴을 의미한다.

## 옵저버패턴 예제코드
```python
import random
import time


class Observer:  # 관찰자를 표현하는 인터페이스
    def notify(self, generator):
        pass


class NumberGenerator:

    def __init__(self):
        self.observers = []

    def addObserver(self, observer):  # add observer
        self.observers.append(observer)

    def deleteObserver(self, observer):  # delete observer
        self.observers.remove(observer)

    def notifyObserver(self):  # display
        for obs in self.observers:
            obs.notify(self)

    def getNumber(self):
        pass

    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.number = 0

    def getNumber(self):
        return self.number

    def execute(self):
        for i in range(20):
            self.number = random.randint(1, 50)
            self.notifyObserver()


class DigitObserver(Observer):
    def notify(self, generator):
        print("DigitObserver: ", generator.getNumber())
        time.sleep(1)


class GraphObserver(Observer):
    def notify(self, generator):
        print("GraphObserver: ", end=" ")
        count = generator.getNumber()

        for i in range(count):
            print("*", end="")
        print()

        time.sleep(1)


generator = RandomNumberGenerator()
observer1 = DigitObserver()
observer2 = GraphObserver()

generator.addObserver(observer1)
generator.addObserver(observer2)
generator.execute()

```

## 개념확장
> 상태를 가지고 있는 ConcreteSubject 역할과 상태변화를 전달받는 ConcreteObserver 역할이 존재하는데 이 두 역할을 연결하는 것이 API에 해당하는 Subjcet, Observer이다.  
> ConcreteSubjcet class는 자신을 관찰하는 Observer가 무엇인지는 몰라도 상관없고, 관찰자들이 동일한 API를 구현하고 있다는 것을 알고 있음  
> 등록된 Observer들에 대해서 notify 메소드를 호출하는 것으로 내용을 알 수 있음

* 옵저버의 알림순서
> 구체관찰자 클래스를 설계할때 notify 메소드가 호출되는 순서가 변하더라도 문제가 일어나지 않도록 해야한다.
