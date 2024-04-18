class Car:
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed # class내부에서만 접근이 가능하게 만듬.
        
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
           
c1 = Car("white",5,4,0)
c1.up_speed("0x1100")
c1.up_speed("0x1111")
c1.set_speed(500)
# 클래스의 변수에 직접적으로 접근이 안됨
# get을 통해서만 접근이 가능
print(c1.get_speed()) 