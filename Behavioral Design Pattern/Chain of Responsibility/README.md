# 역할 사슬 패턴(Chain of Responsibility)
* 책임 떠넘기기
> 여러 개의 객체 중에서 어떤 객체가 요구를 처리할 수 있는지 알 수 없을 때 사용됩니다.  
> 요구가 들어오면 그것을 수신하는 객체가 자신이 처리할 수 없는 경우에 다른 객체에게 해당 요구를 넘기고, 최종적으로 요청을 처리 할 수 있는 객체에 의해 요구가 처리됩니다.  

## Chain-of-Responsibility 구조
![image](https://user-images.githubusercontent.com/96826443/168533251-a90fa0a3-0ea5-45c5-a69e-b47026d8d039.png)
> `Handler(receiver)` : 요청을 처리하기 위해 수신자들이 가져야 할 인터페이스  
> `ConcreteHandler(Concrete Receiver)` : Handler interface 를 구현, 각 객체가 특정 요청에 따라 처리할 수 있는 부분을 구현  
> `Client(sender)` : 수신자(Handler)에게 어떤 처리를 요구

## Chain-of-Responsibility 특징
> 복수의 오브젝트를 사슬(Chain)처럼 연결해두면, 그 오브젝트의 사슬을 차례로 돌아다니면서 목적한 오브젝트를 결정합니다.  
> Responsibility 개념을 갖는 모듈들에 사슬(Chain) 구조를 입히는 패턴입니다.

## COR(chain of responsibility) 코드
```python
class Handler:  # API
    def __init__(self):  # 내부에 다음 핸들러를 가리키는 next_handler가 존재
        self.next_handler = None

    def setNext(self, handler):  # 다음 handler인 nexy_handler 설정
        self.next_handler = handler

    def handle(self, req):  # 요청이 들어오면 실행시키는 함수 / req : 요청에대한 정보
        if self.next_handler:
            return self.next_handler.handle(req)
        print("All handlers failed")
        return None


class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f"processing cash {req['amount']} won")
        else:
            print("CashHandler cannot process")
            super().handle(req)


class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'creditCard':
            print(f"processing creditCard {req['amount']} won")
        else:
            print("CreditCardHandler cannot process")
            super().handle(req)
(

class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debitCard':
            print(f"processing debitCard {req['amount']} won")
        else:
            print("DebitCardHandler cannot process")
            super().handle(req)


class paypalHandler(Handler):
    def handle(self, req):
        if req['method'] == 'paypal':
            print(f"processing paypal {req['amount']} won")
        else:
            print("paypalHandler cannot process")
            super().handle(req)


payment = {
    "method": "paypal",
    "amount": 10000
}

cash_handler = CashHandler()
creditcard_handler = CreditCardHandler()
debitcard_handler = DebitCardHandler()
paypal_handler = paypalHandler()

cash_handler.setNext(creditcard_handler)
creditcard_handler.setNext(debitcard_handler)
debitcard_handler.setNext(paypal_handler)
cash_handler.handle(payment)
```

## 코드 실행 결과
![image](https://user-images.githubusercontent.com/96826443/168536446-b527f3b6-d5f6-4896-850c-6a7b063277ca.png)

## COR 개념 확장
> 요구하는 사람과 요구를 처리하는 사람을 유연하게 연결
* Client는 최초로 만나는 담당자(요구를 처리하는 Concrete Receiver)에게 요청하고, 해당 담당자(콘크리트 리시버)가 처리할 수 없는 일이면 다른 담당자(또 다른 콘크리트 리시버)에게 책임을 전가하며 해당 요구(요청)를 해결할 수 있는 담당자를 탐색해 나갑니다.  
* 만약 COR를 사용하지 않으면, 클라이언트(요구하는 사람)가 자신의 요청사항에 해당하는 담당자의 정보를 알고 있어야 합니다. 때문에 이는 부품으로써의 독립성이 훼손되기 때문에 COR을 이용하여 이를 막을 수 있습니다.  
> COR : 동적으로 사슬의 형태를 변경이 가능  
* 요구를 처리하는 콘크리트핸들러(Concrete Receiver) 역할의 오브젝트 관계가 동적으로 변화하는 상황이 있을 때, 동적으로 이를 재편할 수 있습니다.
> 요구에 대한 처리가 고정적인 경우에는 굳이 COR 패턴을 사용할 필요가 없다.
* COR구조는 유연성은 높을 수 있지만, 처리가 지연된다는 단점도 가지고 있다. 하지만 처리가 지연된다는 단점에도 유연성을 올려준다는 측면에서 더욱 이점으로 다가오기 때문에 합당한 트레이드오프라고 볼 수 있다.
