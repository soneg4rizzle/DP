# 중재자 패턴(Mediator Pattern)
> 중재자 패턴, 조정자 패턴은 소프트웨어 공학에서 어떻게 객체들의 집합이 상호작용하는지를 함축해놓은 객체를 정의한다.  
> 이 패턴은 프로그램의 실행 행위를 변경할 수 있기 때문에 행위 패턴으로 간주된다.  
> 중재자 패턴을 사용하면 객체 간 통신은 중재자 객체 안에 함축된다. 

* 중재자 패턴을 사용하지 않은 경우 : 객체간의 직접적인 커뮤니케이션이 있는 경우  

> ![image](https://user-images.githubusercontent.com/96826443/170615478-e5c4a9cf-6524-43a4-8844-7ee75ac9f1ab.png)
* A, B, C, D의 객체가 존재
* A에서 B, C의 메소드를 직접 호출
* C에서 B, D의 메소드를 직접 호출
> 직접적으로 객체간의 메소드 호출을 하게 되면, 그 구조의 Dependency가 복잡해져 사용한 객체의 클래스를 다른 곳에서 사용할 수 없다.

* 중재자 패턴을 적용한 경우
> ![image](https://user-images.githubusercontent.com/96826443/170615699-10064ba0-2461-41bb-b6d0-b0bd40801afb.png)  
* Mediator 객체를 생성해서 모든 커뮤니케이션이 중재자(Mediator)를 거쳐 이루어지게 한다.
> 객체간의 복잡한 Dependency가 사라지고 객체들의 클래스를 다른 곳에서 사용할 수 있게 된다. 

## 중재자 패턴의 구조
![image](https://user-images.githubusercontent.com/96826443/170615277-1c7577c2-4511-4265-901c-8a65bef06b13.png)
> mediator : 중개인  
> colleage : 회원
> concrete_mediator : colleague에 대한 정보를 알고 있어야 한다.

## 중재자 패턴의 대표적 예시 : 스마트 홈 시스템
> 스마트 시계, 조명, 스피커를 사용하는 경우
> 스마트 시계가 알람이 울리면 -> 스마트 조명ON, 스마트 스피커에서 노래 실행
>  -> 스마트 시계 오브젝트에서 조명, 스피커에 대한 정보를 가지고 각 함수를 호출해야 한다.
> 스마트 조명을 끄면 스피커도 꺼지게 설정
>  -> 조명 오브젝트 안에는 스피커 오브젝트 정보를 가지고 있어야 한다.

## 스마트 시계, 조명, 스피커에 대한 클래스 구조
> ![image](https://user-images.githubusercontent.com/96826443/170616269-7e12d334-1a71-4881-aa6c-2e580bbdad6d.png)
> Mediator class(중재자 클래스) : Notify() : 시그널을 받아서 처리하는 함수  
> HomeMedia class : Mediator 상속받고 Notify() 함수로 들어오는 시그널을 분배하기 위해 clock, light, speaker에 대한 정보를 가지고 있다.  
> Clock, Light, Speaker class : 내부에 중재자(Mediator)를 통해 시그널을 보내기 때문에 Mediator reference를 가지고 있다.  

## 중재자 패턴 예시 코드
```python
from msilib.schema import Media


class Mediator:
    def notify(self, signal: str):
        pass


class Clock:
    def setMediator(self, mediator: Mediator):  # Mediator 설정 함수
        self.mediator = mediator

    def alarm(self):
        print("alarm on")
        self.mediator.notify("AlarmOn")


class Light:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator

    def on(self):
        print("light on")

    def off(self):
        print("light off")
        self.mediator.notify("LightOff")


class Speaker:
    def setMediator(self, mediator: Mediator):
        self.mediator = mediator

    def on(self):
        print("speaker on")

    def off(self):
        print("speaker off")


class HomeMediator(Mediator):
    def __init__(self, clock, light, speaker):
        self.clock = clock
        self.light = light
        self.speaker = speaker

    def notify(self, signal: str):
        if signal == 'AlarmOn':
            self.speaker.on()
            self.light.on()

        elif signal == 'LightOff':
            self.speaker.off()


clock = Clock()
light = Light()
speaker = Speaker()

mediator = HomeMediator(clock, light, speaker)
clock.setMediator(mediator)
light.setMediator(mediator)
speaker.setMediator(mediator)

clock.alarm()

light.off()
```

## 중재자 패턴의 핵심
> 객체간의 신속한 커뮤니케이션을 위해 중재자를 이용하여 객체간의 dependency(의존성)을 낮추는 것에 있다.
