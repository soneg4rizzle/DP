# State Pattern(상태 패턴)
> OOP에서는 프로그램 대상을 '클래스'로 표현하는데, 이 때 '상태' 자체를 클래스로 표현할 수 있습니다.  
> 상태 패턴 구현은 각 상태에 해당하는 별도의 클래스를 만들고 상태전환을 그 클래스들로부터 진행하는 것을 말합니다.

## 1. State Pattern UML
<img width="631" alt="image" src="https://user-images.githubusercontent.com/96826443/165677782-211501c9-a1d0-4851-b9bf-44a25bc0f1e3.png">

## 2. 상태패턴 적용
```python

# 상태 패턴 적용 안한 코드
class TrafficLight:  # Context
    def __init__(self):
        self.state = GreenLight()
    # prefer enum

    def setState(self, state: str):
        self.state = state

    def speak(self):
        self.state.status()

    def wait(self):
        self.state.changeLight(self)


class State:  # State
    def status(self):
        pass

    def changeLight(self, traffic_light: TrafficLight):
        pass


class GreenLight(State):  # ConcreteState
    def status(self):
        print('green light')

    def changeLight(self, traffic_light: TrafficLight):
        print('wait... the light changed')
        traffic_light.setState(RedLight())


class RedLight(State):  # ConcreteState
    def status(self):
        print('red light')

    def changeLight(self, traffic_light: TrafficLight):
        print('wait... the light changed')
        traffic_light.setState(GreenLight())


t_light = TrafficLight()
t_light.speak()
t_light.wait()
t_light.speak()

```
## 3-1. 상태패턴의 장점
```상태패턴의 컨셉은 "Devide and Conquer"```
> 따라서 각각의 구체적인 상태를 클래스로 표현하여 복잡한 프로그램을 분할하고 간단히 표현 가능  
> 다른 상태로 전환하는 것에 대한 정보가 클래스 내에 정리 되어있고, 어떠한 클래스로 전환하는지는 해당되는 클래스의 코드만 읽으면 가능   

## 3-2. 태패턴의 단점
```Concrete State 간의 의존 관계가 높아진다.```
> 하나의 Concrete State 클래스가 다른 Concrete State 클래스의 역할을 서로 알아야 한다.
> 하나를 삭제/추가 하려고 할 때, 서로 의존 관계가 높은 클래스들 또한 수정해야 한다.
