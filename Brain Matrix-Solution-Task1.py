import time
def deposit():
    try:
        global data
        money=int(input("Enter the amount you want to deposit : "))
        actual=data["money"]
        total_amount=actual+money
        print(total_amount)
    except ValueError:
        print("Enter a number only not Alphabets")
def withdraw ():
    try:
        global data
        print("Only 500 rupees notes available here.....")
        money=int(input("Enter the amount you withdraw: "))
        print("Please wait while processing the amount...")
        time.sleep(2)
        if(money==500):
            if(data["money"]>=money):
                total_amount=data["money"]-money
            else:
                print("Insufficient Balance")
        else:
            print("Invalid please Enter a 500 rupees notes only") 
    except ValueError:
        print("Enter the number only not alphabets")
def balancecheck():
    global data
    print("The account balance is \n\t\t{}".format(data["money"]))
    print("Thanks for checking the balance")
def statment():
    global data
    print("="*40)
    print("The 5 transaction is here....")
    print("="*40)
    print("upi-id/5967: ₹+50 credit")
    print("upi-id/5407: ₹-500 debit")  
    print("upi-id/5767: ₹-50  credit")
    print("upi-id/5067: ₹+40 credit")
    print("="*40)
    print("The available balance is :{} ".format(data["money"]))
def deposit1():
    try:
        global data
        money=int(input("वह राशि दर्ज करें जिसे आप जमा करना चाहते हैं : "))
        actual=data["money"]
        total_amount=actual+money
        print(total_amount)
    except ValueError:
        print("केवल संख्या दर्ज करें, अक्षर नहीं")
def withdraw2():
    try:
        global data
        print("यहां मिलेंगे सिर्फ 500 रुपये के नोट.....")
        money=int(input("आपके द्वारा निकाली गई राशि दर्ज करें: "))
        if(money==500):
            if(data["money"]>=money):
                total_amount=data["money"]-money
            else:
                print("अपर्याप्त शेषराशि..")
        else:
            print("अमान्य, कृपया केवल 500 रुपये का नोट दर्ज करें..") 
    except ValueError:
        print("केवल संख्या दर्ज करें, अक्षर नहीं")
def balancecheck3():
    global data
    print("कृपया प्रसंस्करण के दौरान प्रतीक्षा करें...")
    time.sleep(2)
    print("खाता शेष है\n\t\t{}".format(data["money"]))
    print("शेष राशि जाँचने के लिए धन्यवाद")
def statment4():
    global data
    print("="*40)
    print("5 लेन-देन यहाँ है....")
    print("="*40)
    print("कृपया प्रसंस्करण के दौरान प्रतीक्षा करें...")
    time.sleep(2)
    print("upi-id/5967: ₹+50 श्रेय")
    print("upi-id/5407: ₹-500 खर्चे में लिखना")  
    print("upi-id/5767: ₹-50  श्रेय ")
    print("upi-id/5067: ₹+40 श्रेय")
    print("="*40)
    print("उपलब्ध शेष है :{} ".format(data["money"]))    
data={"pin":1234,"money":1000}
print("Welcome to the ATM Machine...\n")
time.sleep(1)
print("Please Insert your card in Correct Way..\n")
print("Please wait it is processing...\n")
print("""Please Select your language please...
\t1)English \n\t2)Hindi""")
try:
        language=int(input("Enter Your Choose : "))
        if(language==1):
            pin=int(input("Please Enter Your 4-digits Pin-no: "))
            print("please wait while processing.....")
            time.sleep(2)
            if(pin==data["pin"]):
                print("="*40)
                print("\t1.Deposit")
                print("\t2.Withdraw")
                print("\t3.Balance-Check")
                print("\t4.Statment-Recepit")
                print("\t5.Exit")
                print("="*40)
                time.sleep(1)
                try:
                    n=int(input("Enter the choice : "))
                    match(n):
                        case 1:
                            deposit()
                        case 2:
                            withdraw()
                        case 3:
                            balancecheck()
                        case 4:
                            statment()
                        case 5:
                            print("Thanks for using visit again......")        
                except ValueError:
                    print("Please Enter the number only not a Alphabets")   
        elif(language==2):
            pin=int(input("कृपया 4 अंकों का पिन नंबर दर्ज करें: "))
            if(pin==data["pin"]):
                print("="*40)
                print("\t1.जमा")
                print("\t2.निकालना")
                print("\t3.संतुलन-जांच")
                print("\t4.वक्तव्य-रसीद")
                print("\t5.बाहर निकलना")
                print("="*40)
                print("कृपया प्रसंस्करण के दौरान प्रतीक्षा करें...")
                time.sleep(2)
                try:
                    n=int(input("अपनी पसंद दर्ज करें: "))
                    match(n):
                        case 1:
                            deposit1()
                        case 2:
                            withdraw2()
                        case 3:
                            balancecheck3()
                        case 4:
                            statment4()
                        case 5:
                            print("पुनः विज़िट का उपयोग करने के लिए धन्यवाद......")        
                except ValueError:
                    print("कृपया केवल संख्या दर्ज करें, अक्षर नहीं..")  
            else:
                print("You Entered incorrect pin Try again....")    
except ValueError:
    print("Please Enter Number only not Alphabets or alphanumeric")
       