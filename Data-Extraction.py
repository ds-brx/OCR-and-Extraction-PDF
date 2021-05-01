import cv2
import numpy as np
import string 
import random
import essential_generators
from essential_generators import DocumentGenerator
import faker
from faker import Faker

img = cv2.imread("Template.jpg")
fake = Faker()
gen = DocumentGenerator()

dates = [(186,565),(186,650),(709,569)]    
def generator(n):
    for i in range(n):
        imtemp = img.copy()
        receipt_num = ''.join(random.choices(string.ascii_uppercase,k = 3)) + '-'+''.join(random.choices(string.digits,k = 3))+ '-'+''.join(random.choices(string.digits,k = 5))
        cv2.putText(imtemp,receipt_num,(186,479),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

        for org in dates:
          res = fake.month_name()+" "+ fake.day_of_month()+", "+fake.year()
          cv2.putText(imtemp,res,org,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

        sentence = gen.sentence()
        sentence = sentence.split(" ")
        sentence = " ".join(sentence[i] for i in range(3))
        cv2.putText(imtemp,sentence,(1233,481),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

        name = fake.name()
        add = fake.address()
        add = " ".join(add.split("?")).splitlines()
        cv2.putText(imtemp,name,(1233,565),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        name1 = fake.name()
        name2 = fake.name()
        name = name1 + ", " + name2
        beneficiary_id = ''.join(random.choices(string.ascii_uppercase,k = 3)) + '-'+''.join(random.choices(string.digits,k = 3))+ '-'+''.join(random.choices(string.digits,k = 5))
        cv2.putText(imtemp,beneficiary_id,(1370,612),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        cv2.putText(imtemp,name,(1233,649),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        cv2.putText(imtemp,add[0],(196,716),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        cv2.putText(imtemp,add[1],(196,756),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        filename = 'template'+str(i)+'.png'
        cv2.imwrite(filename,imtemp)

generator(1)
