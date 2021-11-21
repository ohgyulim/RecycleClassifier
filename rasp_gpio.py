from classification import Result
import RPi.GPIO as GPIO
import time

a = Result('/home/pi/Desktop/MobileNet_cpu.pt') # a = [label]

servo_pin1 = 14
servo_pin2 = 13
servo_pin3 = 21

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1,GPIO.OUT)
pwm1 = GPIO.PWM(servo_pin1,50)
GPIO.setup(servo_pin2,GPIO.OUT)
pwm2 = GPIO.PWM(servo_pin2,50)

GPIO.setup(servo_pin3,GPIO.OUT)
pwm3 = GPIO.PWM(servo_pin3,50)


#pwm1.start(3.0)


if a[0] == 1: #paper
    pwm1.start(3.0)
    pwm1.ChangeDutyCycle(3.0)
    time.sleep(10.0)
    pwm1.ChangeDutyCycle(12.5)
    time.sleep(1.0)
    
    pwm1.ChangeDutyCycle(0.0)
    pwm1.stop()
    GPIO.cleanup()
     
elif a[0] == 2: #plastic
    pwm2.start(3.0)
    pwm2.ChangeDutyCycle(3.0)
    time.sleep(10.0)
    pwm2.ChangeDutyCycle(12.5)
    time.sleep(1.0)
    pwm2.ChangeDutyCycle(0.0)
    pwm2.stop()
    GPIO.cleanup()

elif a[0] == 0: #0 => can, 1=>paper, 2=>plastic,3 => vinyl
    pwm3.start(3.0)
    pwm3.ChangeDutyCycle(3.0)
    time.sleep(10.0)
    pwm3.ChangeDutyCycle(12.5)
    time.sleep(1.0)
    pwm3.ChangeDutyCycle(0.0)
    pwm3.stop()
    GPIO.cleanup()


triggerPin1 = 17
echoPin1 = 27

triggerPin2 = 20
echoPin2 = 19
pinPiezo = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin1, GPIO.OUT)    # 출력
GPIO.setup(echoPin1, GPIO.IN)        # 입력
GPIO.setup(triggerPin2, GPIO.OUT)    # 출력
GPIO.setup(echoPin2, GPIO.IN)  

def dis(distance):
    Buzz.start(50)
    Buzz.ChangeFrequency(523)
    time.sleep(0.5)
    Buzz.stop()
    time.sleep(0.3)
    

try:
      #구형파 발생
      if a[0] == 0:
         GPIO.output(triggerPin1, GPIO.LOW)  
         time.sleep(0.00001) 
         GPIO.output(triggerPin1, GPIO.HIGH)

      #시간측정
         while GPIO.input(echoPin1) == 0:  # 펄스 발생
            start = time.time()
         while GPIO.input(echoPin1) == 1:  # 펄스 돌아옴
            stop = time.time()

         rtTotime = stop - start                   # 리턴 투 타임 = (end시간 - start시간)

         distance = rtTotime * (34000 / 2 )
         print("distance : %.2f cm" %distance)     # 거리 출력
         time.sleep(0.2)
         
         GPIO.setup(pinPiezo, GPIO.OUT)
         Buzz = GPIO.PWM(pinPiezo, 440)      # 부저센서 초기화
         if(distance<4.0):
             dis(distance)
         

      elif a[0] == 1:
          
         GPIO.output(triggerPin2, GPIO.LOW)  
         time.sleep(0.00001) 
         GPIO.output(triggerPin2, GPIO.HIGH)

      #시간측정
         while GPIO.input(echoPin2) == 0:  # 펄스 발생
            start = time.time()
         while GPIO.input(echoPin2) == 1:  # 펄스 돌아옴
            stop = time.time()

         rtTotime = stop - start                   # 리턴 투 타임 = (end시간 - start시간)

         distance = rtTotime * (34000 / 2 )
         print("distance : %.2f cm" %distance)     # 거리 출력
         time.sleep(0.2)

         GPIO.setup(pinPiezo, GPIO.OUT)
         Buzz = GPIO.PWM(pinPiezo, 440)      # 부저센서 초기화
         if(distance<4.0):
             dis(distance)

      elif a[0] == 2:
         GPIO.output(triggerPin1, GPIO.LOW)  
         time.sleep(0.00001) 
         GPIO.output(triggerPin1, GPIO.HIGH)

      #시간측정
         while GPIO.input(echoPin1) == 0:  # 펄스 발생
            start = time.time()
         while GPIO.input(echoPin1) == 1:  # 펄스 돌아옴
            stop = time.time()

         rtTotime = stop - start                   # 리턴 투 타임 = (end시간 - start시간)

         distance = rtTotime * (34000 / 2 )
         print("distance : %.2f cm" %distance)     # 거리 출력
         time.sleep(0.2)
         
         GPIO.setup(pinPiezo, GPIO.OUT)
         Buzz = GPIO.PWM(pinPiezo, 440)      # 부저센서 초기화
         if(distance<4.0):
             dis(distance)
      
   

except KeyboardInterrupt:
   GPIO.cleanup()