# 템플릿 메소드 패턴(Template Method Pattern)
> 템플릿 메소드 패턴이란 특정 작업을 처리하는 일부분을 서브 클래스로 캡슐화하여 전체적인 구조는 유지하면서 특정 단계에서 수행하는 내용을 교체하는 패턴입니다.  


## Template Method Pattern
![image](https://user-images.githubusercontent.com/96826443/167381145-85072478-b9bb-4f8b-b474-2701cd0ec750.png)
* 상위클래스에는 템플릿에 해당하는 메소드가 정의되어 있고, 메소드 정의 안에는 추상 메소드가 사용되고 있다.  
* 따라서 상위클래스의 프로그램만 보면 추상 메소드를 어떻게 호출하고 있는지 알 수 있다.  
* 추상 메소드는 하위클래스에서 구체적으로 구현된다.   
 
| 상위클래스 | 하위클래스 |
| :---: | :---: |
| 뼈대 | 구체적 내용 |

## Templaye Method code
```python
class AbstractDisplay:  # 상위클래스
    def open(self):
        pass

    def textPrint(self):
        pass

    def close(self):
        pass

    def display(self):
        self.open()

        for i in range(5):
            self.textPrint()

        self.close()


class CharDisplay(AbstractDisplay):  # 하위클래스
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<", end="")

    def textPrint(self):
        print(self.ch, end="")

    def close(self):
        print(">>")


class StringDisplay(AbstractDisplay):  # 하위클래스
    def __init__(self, string):
        self.string = string
        self.width = len(self.string)

    def open(self):
        self.printLine()

    def textPrint(self):
        print("|" + self.string + "|")

    def close(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(self.width):
            print("-", end="")
        print("+")


cd = CharDisplay("H")
sd1 = StringDisplay("Hello, World!")
sd2 = StringDisplay("Welcome to Korea")
cd.display()
sd1.display()
sd2.display()
```

## 템플릿 메소드 패턴의 특징
* 상위 클래스의 메소드가 기술되어 있으므로, 하위 클래스에서는 이를 따로 기술하지 않아도 된다.  
* 상위 클래스의 소스 프로그램들을 기술하지 않으면 하위 클래스의 구현이 어렵다.  
* 상위 클래스에서 기술을 많이하게 되면 하위 클래스에서의 자유도가 떨어진다.

> 템플릿 메소드 패턴은 상위클래스 타입의 변수에 하위클래스 타입의 인스턴스를 대입해도 동작해야 한다는 점에서 리스코프(Liskov) 치환 원칙을 따라야 한다.



