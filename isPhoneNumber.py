import re
class isPhoneNumber:
  def isPhoneNumber(text):
    phone_pattern = r'[0-9]{3}-\d\d\d-[0-9]{4}'
    return bool(re.search(phone_pattern, text))

if name=="__main__":
  print(str(isPhoneNumber("123-456-7890"))) #TRUE
  print(str(isPhoneNumber("This has a number 450-213-4221"))) #TRUE 
  print(str(isPhoneNumber("123-421-542a"))) #FALSE
