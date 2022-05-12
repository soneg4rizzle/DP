# Command Pattern
> 클래스가 Task를 실행할 때, 자신의 클래스나 다른 클래스의 메소드를 호출하는 패턴 (명령을 추상화하여 객체로 다루는 패턴)
* 실행하는 Task를 메소드 호출이라는 동적인 처리로 표현하느 것이 아니라, 명령을 나타내는 클래스의 인스턴스로 표현이 가능합니다.   
* 명령의 집합을 저장해놓고 저장된 명령을 실행할 수 있고, 여러 명령 집합을 새로운 명령으로 재이용 할 수 있습니다.  

## Command Pattern UML
![image](https://user-images.githubusercontent.com/96826443/168035392-f9ded28e-fecf-49de-9d38-e6b8ae87a843.png)
* Command : 명령의 인터페이스(API)를 정의하는 역할 
* Concrete Command : 커맨드 역할의 인터페이스를 실제로 구현하는 역할
* Invoker : 명령의 행동을 개시하는 역할(호출자)
* Receiver : 커맨드 역할이 명령을 실행할 때 대상이 되는 역할, [명령을 받아들이는 수신자]

## Command Pattern 예제 코드
```python
from typing import List


class Command:  # API ( Command Interface )
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, print_str: str):
        self.print_str = print_str

    def execute(self):
        print(f"from print command : {self.print_str}")


first_command = PrintCommand("first command")
second_command = PrintCommand("second command")

first_command.execute()
second_command.execute()
print("\n")


class Dog:  # Receiver
    def sit(self):
        print("The dog sat dit down")

    def stay(self):
        print("The dog is staying")


class DogCommand(Command):  # Command Class( Command Interface 상속 )
    # prefer enums
    def __init__(self, dog: Dog, commands: List[str]):
        self.dog = dog
        self.commands = commands

    def execute(self):
        for command in self.commands:
            if command == 'sit':
                self.dog.sit()
            elif command == 'stay':
                self.dog.stay()


baduk = Dog()
dog_command = DogCommand(baduk, ['stay', 'sit', 'sit'])
dog_command.execute()
print("\n")


class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command: Command):
        self.command_list.append(command)

    def runCommands(self):
        for command in self.command_list:
            command.execute()


invoker = Invoker()
invoker.addCommand(first_command)
invoker.addCommand(dog_command)
invoker.addCommand(second_command)
invoker.runCommands()

```
## 출력결과
<img width="205" alt="image" src="https://user-images.githubusercontent.com/96826443/168042317-937da4b1-d15d-451e-a78b-6e3eefa33db8.png">
