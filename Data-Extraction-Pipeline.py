import numpy as np
import pandas as pd
import pytesseract
import cv2

call = 0
receipt_list = []
case_list = []
recieved_date_list = []
priority_date_list = []
petitioner_list = []
beneficiary_list = []
address_list = []

def get_region(y1,y2,x1,x2,img):
  crop_img = img[y1:y2, x1:x2]
  text = pytesseract.image_to_string(crop_img).rstrip()
  li = text.split("\n")
  return li

def get_receipt(img):
   # get receipt
  li = []
  li = get_region(412,489, 182,1221,img)
  receipt_num = li[2]
  receipt_num = "-".join(receipt_num.split("—-"))
  receipt_num = "-".join(receipt_num.split("-—"))
  return receipt_num

def get_case_type(img):
    # get case type
  li = []
  li = get_region(411,489, 1226,2311,img)
  for j in li:
    if j!= " " and j!= "" and j!= "Case Type":
      case_type = j
  return case_type

def get_received_date(img):
    # get received date
  li = []
  li = get_region(495,573,182,699,img)
  received_date = li[2]
  return received_date

def get_priority_date(img):
    # get priority date
  li = []
  li = get_region(495,573,702,1219,img)
  for j in li:
    if j!= " " and j!= "" and j!= "Priority Date":
      priority_date = j
  return priority_date

def get_petitioner(img):
    # get petitioner 
  li = []
  li = get_region(495,573,1227,2310,img)
  for j in li:
    if j!= " " and j!= "" and j!= "Petitioner":
      petitioner = j
  return petitioner

def get_notice_date(img):
    # get notice date
  li = []
  li = get_region(578,656,183,701,img)
  notice_date = li[1]
  return notice_date

def get_beneficiary(img):
    # get beneficiary
  li = []
  li = get_region(578,656,1227,2312,img)
  beneficiary = li[0].split(" ")[1] + " " + " ".join(li[1].split(", "))
  beneficiary = "-".join(beneficiary.split("—-"))
  beneficiary = "-".join(beneficiary.split("-—"))
  return beneficiary

def get_address(img):
    #get address
  li = []
  li = get_region(664,849,183,1350,img)
  address = li[2]+' '+ li[3]
  return address

def get_data(img):
  receipt_num = get_receipt(img)
  case_type = get_case_type(img)
  recieved_date = get_received_date(img)
  priority_date = get_priority_date(img)
  petitioner = get_petitioner(img)
  beneficiary = get_beneficiary(img)
  address = get_address(img)
  return receipt_num,case_type,recieved_date,priority_date,petitioner,beneficiary,address


for i in range(50):
    call = i
    img = cv2.imread("img/template"+str(i)+".png")
    receipt_num,case_type,recieved_date,priority_date,petitioner,beneficiary,address = get_data(img)
    receipt_list.append(receipt_num)
    case_list.append(case_type)
    recieved_date_list.append(recieved_date)
    priority_date_list.append(priority_date)
    petitioner_list.append(petitioner)
    beneficiary_list.append(beneficiary)
    address_list.append(address)


d = {'receipt number' : receipt_list,
  'case type' : case_list,
  'recieved date' : recieved_date_list,
  'priority date' : priority_date_list,
  'petitioner' : petitioner_list,
  'beneficiary' : beneficiary_list,
  'address' : address_list}


df = pd.DataFrame(data=d)
df.to_csv('extracted_data.csv')
print(df)
