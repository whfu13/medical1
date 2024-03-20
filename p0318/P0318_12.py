class Car:
    carCount = 0
    carNo = 0
    color = ""
    door = 0
    tire = 0
    speed = 0
    
    def __init__(self,color="",door=0,tire=0,speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed
        Car.carCount += 1
        self.carNo = Car.carCount
    
    def up_speed(self,smartkey):
        if smartkey == "0x1100":
            self.__speed += 10
        else:
            print("스마트키 다릅니다.")

    def down_speed(self):
        self.__speed -= 10  
        
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed += speed
          
car_list = []
        
c1 = Car()
c1.carNo = 1
c1.color = "white"
c1.door = 5
c1.tire = 4
c1.speed = 0
c1.up_speed("0x1100")
c1.set_speed(30)
print(c1.get_speed())
print(f"c1 : {c1.carNo},{c1.color},{c1.door},{c1.tire},{c1.speed}")

c2 = Car("red",5,4,0)
# print(f"c2 : {c2.carNo},{c2.color},{c2.door},{c2.tire},{c2.speed}")
# c2.up_speed(100)
print(f"c2 : {c2.carNo},{c2.color},{c2.door},{c2.tire},{c2.speed}")

c3 = Car("silver",5,4,0)
# print(f"c3 : {c3.carNo},{c3.color},{c3.door},{c3.tire},{c3.speed}")
# c3.up_speed(70)
print(f"c3 : {c3.carNo},{c3.color},{c3.door},{c3.tire},{c3.speed}")

# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo에는 carCount 숫자를 이용해서 carNo를 넣으시오.
# carNo, color="white",door=5,tire=4,speed
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 -10씩 감소

# c1 - white,5,4,0, => speed 30이 되도록
# c2 - red,5,4,0 = > speed 100
# c3 - silver,5,4,0 => speed 79
# car_list 추가하고

# car_list에 있는 모든 객체의 color,door,tire,speed 모두 출력하시오.
car_list.append(c1)
car_list.append(c2)
car_list.append(c3)
c = Car(c1,c2,c3)
car_list.append(c)
# print("c1 : ", c1.carNo,c1.color,c1.door,c1.tire,c1.speed)
# print("c2 : ", c2.carNo,c2.color,c2.door,c2.tire,c2.speed)
# print("c3 : ", c3.carNo,c3.color,c3.door,c3.tire,c3.speed)
print(car_list)
# print("{},{},{},{},{}".format())