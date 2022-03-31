# Facade Pattern
> 프로그램은 시간이 지날수록 많은 클래스가 관계를 맺으며 복잡해지고 커지는 경향이 있습니다.
> 때문에 상호 관련된 많은 클래스를 적절하게 사용해야 하는데,
> 퍼사드 패턴은 이러한 처리를 실행하기 위한 창구 역할을 하는 별도의 인터페이스를 두는 것을 말합니다.
 


* ```Facade``` : 건물의 앞면(정면)을 의미

![image](https://user-images.githubusercontent.com/96826443/160956526-01e6666a-ff17-4297-a057-6e17a53ac489.png)
> Facade Pattern 은 내부의 복잡합은 숨기고 간단한 인터페이스를 제공하는 패턴입니다.
* Client(고객)가 여러 라이브러리와 클래스들을 필요로 할 때, 이들을 조합해서 더 간단한 인터페이스로 제공해주는 클래스를 생각해 볼 수 있습니다.
  * 이를 적용시 고객은 복잡한 클래스/라이브러리에 접근할 필요가 없이 간단한 인터페이스를 제공해주는 Facade Pattern을 이용하여 쉽게 개발할 수 있게됩니다.

## 퍼사드 패턴의 적용
> 로켓을 우주로 발사하는 경우를 생각해보자.
> 우리는 로켓을 우주로 쏘아올려 목적지에 도달할때까지 복잡한 과정을 거쳐야한다.
* 단계1 : 점화, 이륙, 분리
* 단계2 : 점화, 분리
* 단계3: 캡슐점화, 착륙

| Stage1 클래스 | Stage2 클래스 | Capsule 클래스 |
| :---: | :---: | :---: |
| ignite() | ignite() | ignite() |
| eject() | eject() | landing() |
| launch() | | |
> 이러한 경우에 퍼사드 패턴을 적용해 볼 수 있다.

```python
class Rocket:
  def __init__(self):
    self.stage1 = Stage1()
    self.stage2 = Stage2()
    self.capsule = Capsule()
  
  def launch(self): # 단계1 | 단계 2 | 캡슐의 모든 기능 수행 가능
    self.stage1.ignite()
    self.stage1.launch()
    self.stage1.eject()
    self.stage1.comeback()
    self.stage2.ignite()
    self.stage2.eject()
    self.capsule.ignite()
    self.capsule.landing()
    
rocket = Rocket() # 사용자는 여러 부품들 통제할 필요 없이
rocket.launch()   # Rocket 객체만 만들어서 launch 만 하면 되기에 편리하다.
# 결론 : 퍼사드 패턴은 여러 개의 라이브러리, 클래스를 묶어서 간단한 인터페이스를 제공하는 역할

```
* **결론** : 퍼사드 패턴은 여러 개의 라이브러리, 클래스를 묶어서 간단한 인터페이스를 제공하는 역할

## 퍼사드 패턴의 응용
> 딥러닝 프레임워크에 퍼사드 패턴의 적용

```Fashion MNIST```
* 70000개의 28x28 픽셀의 이미지와 10개의 클래스 정답으로 구성된 Data Set


