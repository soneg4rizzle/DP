class Stage1:
    def ignite(self):
        print('1st stage: ignition')

    def launch(self):
        print('1st stage: launching')

    def eject(self):
        print('1st stage: ejection')

    def comeback(self):
        print('1st stage: comback')


class Stage2:
    def ignite(self):
        print('2nd stage: ignition')

    def eject(self):
        print('2nd stage: ejection')


class Capsule:
    def ignite(self):
        print('capsule: ignition')

    def landing(self):
        print('capsule: landing')


# 퍼사드 패턴의 적용
class Rocket:
    def __init__(self):
        self.stage1 = Stage1()
        self.stage2 = Stage2()
        self.capsule = Capsule()

    def launch(self):  # 단계1 | 단계 2 | 캡슐의 모든 기능 수행 가능
        self.stage1.ignite()
        self.stage1.launch()
        self.stage1.eject()
        self.stage1.comeback()
        self.stage2.ignite()
        self.stage2.eject()
        self.capsule.ignite()
        self.capsule.landing()


rocket = Rocket()  # 사용자는 여러 부품들 통제할 필요 없이
rocket.launch()   # Rocket 객체만 만들어서 launch 만 하면 되기에 편리하다.
# 결론 : 퍼사드 패턴은 여러 개의 라이브러리, 클래스를 묶어서 간단한 인터페이스를 제공하는 역할
