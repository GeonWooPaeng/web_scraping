# 함수에서 무한 argument 사용 
#1. *args(positional argument - 숫자)
# tuple 
# def plus(a,b,*args): 
#   pass 

#ex
#무한 계산기 만들기
# def plus(*args):
#   result = 0 
#   for number in args:
#     result += number 
#   print(result)
  

#2. **kwargs(keyword argument - 문자)
# dictonary
# def plus(a,b,**kwargs): 
#   pass 

# self.color = kwargs.get("color", "black") # color을 받지 못하면 black을 넣어준다.




#객체 지향 
# class Car():
#   #blue print
#   wheels = 4 
#   doors = 4 
#   windows = 4 
#   seats = 4 

# porche = Car() # instance(porche), instantiation(Car뒤의 ()붙은 것)




# class안에 있는 function이 method이다
# 모든 method의 첫번째 argument는 method를 호출하는 instance 자신이다.

#dir(class이름) 는 class안에 있는 모든 것들을 리스트로 보여준다

# __str__ 는 class의 instance를 출력하는 것이다(기본 method)
# __init__는 초기화 method 


# class extend => def p(부모class): #부모 class의 내용 사용할 수 있다.
# method extend(다른 class에서 확장): super()(부모class를 호출하는 함수)사용 => ex) init method확장 => 
# def __init(self, **kwargs):
#   super().__init__(**kwargs)
