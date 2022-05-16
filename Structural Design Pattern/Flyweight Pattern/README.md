# 플라이웨이트 패턴(Flyweight Pattern)
## 목적 : 동일하게 사용되는 요소들을 공유하여 낭비를 없앤다.
* 설계패턴에서는 메모리의 사용량을 가볍게 하기 위한 의미에서 사용된다.
* 객체(Object) 생성 시에 정보를 저장하기 위한 메모리 공간이 할당되는데, 이 때 가능하다면 객체를 공유하는 방법을 통해 메모리의 사용량(Memory consumption)을 줄일 수 있다.

## 예제코드
### ① Flyweight pattern 적용 전
```python
class Dog:
    def __init__(self, name, age, gender, breed, DNA):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.DNA = DNA

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.gender}, {self.breed}, {self.DNA}'
        
choco = Dog('choco', 2, 'male', 'shihTzu', 'ATAGGCTTACCGATGG...')
baduk = Dog('baduk', 2, 'female', 'jinDo', 'ATAGGCTTACCGATGG...')
print(choco)
print(baduk)
```
* 객체를 생성할 때마다 강아지의 이름, 나이, 성별, 종, DNA의 정보를 메모리에 저장해야한다.  
* 따라서 강아지 객체를 많이 생성해야 할 때, 사용하는 메모리의 양이 상당히 많이 요구된다.  

### ② Flyweight pattern 적용 후 
```python
class Dog:
    DNA_Table = {}  # hashMap | {key, DogBreedDNA}

    # staticmethod
    def addDNA(breed, DNA):
        breed_DNA = DogBreedDNA(breed, DNA)
        Dog.DNA_Table[breed] = breed_DNA

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        if (breed not in Dog.DNA_Table):
            raise RuntimeError(f"{breed} is not int DNA_Talbe")

    def __repr__(self):
        return f'{self.name}, {self.age}, {Dog.DNA_Table[self.breed]}'


class DogBreedDNA:
    def __init__(self, breed, DNA):
        self.breed = breed
        self.DNA = DNA

    def __repr__(self):
        return f'{self.DNA}'


Dog.addDNA('shihTzu', 'ATAGGCTTACCGATGG...')
Dog.addDNA('jinDo', 'ATAGGCTTACCGATGG...')

choco = Dog('choco', 2, 'male', 'shihTzu')
baduk = Dog('baduk', 3, 'female', 'jinDo')

print(choco)
print(baduk)
```
* 이 때, 강아지들간의 공통적 속성을 공유하게 되면 메모리 소모량을 획기적으로 줄일 수 있기 때문에  
* flyweight pattern 을 이용하여 많은 양의 객체를 생성할 때 발생되는 메모리를 감소시킬 수 있다.  

## 단점과 장점
* Flyweight pattern 을 사용한다는 것은 인스턴스를 공유한다는 것이므로 만약 공유하던 자원을 변경하게 된다면  
* 이 자원을 사용하던 모든 곳에 영향을 미치게 된다. 따라서 공유정보를 변경하는 것에 신중을 가해야 한다.  
* 공유자원이 변할 때 이를 이용하던 모든 곳에서 변화가 일어난다는 것은 유용할 수도 있고, 문제를 야기 할 수 있기 때문에 목적에 알맞게 사용하는 것이 가장 중요하다.  

## 공유가능한 정보(Intrinsic) vs 공유불가능한 정보(Extrinsic)
* Intrinsic info : 장소나 상황에 관계없이 변하지 않기 때문에 공유할 수 있는 정보
* Extrinsic info : 장소나 상황에 따라 달라지기 때문에 공유할 수 없는 정보

