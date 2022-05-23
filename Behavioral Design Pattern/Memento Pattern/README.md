# 메멘토 패턴(Memento Pattern)
> 메멘토 패턴은 오브젝트의 상태를 사진처럼 보관하고 필요할 때 꺼내서 그 상태로 되돌릴 수 있는 패턴을 말합니다.  
> 일반적으로 어떤 오브젝트의 히스토리를 관리하고 싶을 때 유용한 패턴(게임에서 저장(SAVE))  

## 메멘토 패턴의 예시
> 예를 들어, 텍스트 에디터를 사용할 때 삭제하기 전 상태로 텍스트를 복원하거나, 깃허브의 리셋기능처럼 어떤 단계(과거)로 되돌릴 수 있다.  
> 메멘토 패턴을 사용하면 어떤 시점의 인스턴스의 상태를 확실하게 기록해서 저장해두면 나중에 인스턴스를 그 시점의 상태로 되돌릴 수 있음  

## 메멘토 패턴 구조
![image](https://user-images.githubusercontent.com/96826443/169759251-27327652-68d7-4d71-8414-3dd1f764dcd0.png)
> Originator : 작성자 역할(자신의 현재 상태를 저장하고 싶을 때 메멘토를 만들어 저장하고 불러오기도 한다.)  
> Memento : Originator 역할의 내부 정보를 정리하고 보관  
> Caretake : 미래의 필요에 대비하여 Memento 역할을 저장  

* Object : 오브젝트를 나타내는 상태(state)가 존재  
> createMemento : 상태(state)에 대한 memento를 만들어주는 함수  
> restore : 메멘토 오브젝트로부터 상태(state)를 복원해주는 함수  

* Memento : 오브젝트의 상태(state)를 그대로 저장하기 때문에 Object와 동일한 state를 property로 갖고있음.


## 메멘토 패턴 예시 코드
```python
import random
from re import M
import time


class Memento:
    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def addFruit(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return self.fruits


class Gamer:

    def __init__(self, money):
        self.money = money
        self.fruits = []
        self.fruitsName = ["사과", "포도", "바나나", "귤"]

    def getMoney(self):
        return self.money

    def getFruit(self):
        fN = len(self.fruitsName)
        fruitName = self.fruitsName[random.randint(0, fN-1)]
        return "맛있는" + fruitName

    def bet(self):

        dice = random.randint(1, 6)

        if dice == 1:
            print("소지금 증가")
        elif dice == 2:
            self.money /= 2
            print("소지금 절반 감소")
        elif dice == 6:
            f = self.getFruit()
            print("과일 " + f + " 를 받았습니다.")
        else:
            print("아무것도 변한 것이 없습니다.")

    def createMemento(self):
        m = Memento(self.money)

        for f in self.fruits:
            m.addFruit(f)

        return m

    def restoreMemento(self, memento):
        self.money = memento.money
        self.fruits = memento.fruits

    def printState(self):
        print("[money: " + str(self.money) + ", fruits: ", end="")

        for f in self.fruits:
            print(", " + f, end="")

        print("]")


def gameRun():
    print("game start")
    gamer = Gamer(100)
    memento = gamer.createMemento()

    for i in range(100):
        print("===game turn===, " + str(i))
        gamer.printState()

        gamer.bet()

        print("소지금이 " + str(gamer.getMoney()) + "원이 되었습니다.")

        # memento 취급 결정
        if gamer.getMoney() > memento.getMoney():
            print("게임을 잘 하고 있으니 현재 상태를 저장")
            memento = gamer.createMemento()

        elif gamer.getMoney() < memento.getMoney()/2:
            print("소지품이 너무 많이 감소해서 이전의 상태로 다시 복원")
            gamer.restoreMemento(memento)

        time.sleep(0.5)
        print()


gameRun()
```

## 코드결과
![image](https://user-images.githubusercontent.com/96826443/169763063-e15bf50a-6f2d-4fee-8d00-9da9dc4845a5.png)
![image](https://user-images.githubusercontent.com/96826443/169763098-f10ce277-1f41-4edb-8e80-a928bf82651a.png)


