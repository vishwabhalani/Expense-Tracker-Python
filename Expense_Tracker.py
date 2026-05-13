Expenses=[]
def Add_Expense():
	amount=float(input("Enter Amount:"))
	category=input("Enter Category(Food/Travel/Shopping):")
	expense={
	"Amount":amount,
	"Category":category
	}
	Expenses.append(expense)
	print("Expense Added")
	print()
def total_expense():
	total=0
	for i in Expenses:
		total=total+i["Amount"]
	print("Total Expenses:",total)
	print()
def category_wise_expense():
	if len(Expenses)==0:
		print("No Expense Found")
	else:
		food=0
		travel=0
		shopping=0
		for i in Expenses:
			if i["Category"]=="food" or i["Category"]=="Food":
				food=i["Amount"]+food
			elif i["Category"]=="travel" or i["Category"]=="Travel":
				travel=travel+i["Amount"]
			elif i["Category"]=="shopping" or i["Category"]=="Shopping":
				shopping=shopping+i["Amount"]
		if food>0:
			print("Food Expense:",food)
		if travel>0:
			print("Travel Expense:",travel)
		if shopping>0:
			print("Shopping Expense:",shopping)
		print()
def highest_expense():
	if len(Expenses)==0:
		print("No Expense")
	else:
		high=Expenses[0]
		for i in Expenses:
			if i["Amount"]>high["Amount"]:
				high=i["Amount"]
		print("Highest Expense:")
		print("Amount:",high["Amount"])
		print("Category:",high["Category"])
		print()
def budget_check():
	budget=int(input("Enter Your Budget:"))
	total=0
	for i in Expenses:
		total=total+i["Amount"]
	if total<budget:
		print("Budget Exceeded")
	else:
		print("Budget Remaining:",total-budget)
	print()
while(True):
	print("-----Expense Tracker-----")
	print("1.Add Expense")
	print("2.Total Expense")
	print("3.Category wise Expense")
	print("4.Highest Expense")
	print("5.Budget Check")
	print("6.Exit")
	choice=int(input("Enter Your Choice:"))
	if choice==1:
		Add_Expense()
	elif choice==2:
		total_expense()
	elif choice==3:
		category_wise_expense()
	elif choice==4:
		highest_expense()
	elif choice==5:
		budget_check()
	elif choice==6:
		print("Exit.Bye")
		break
	else:
		print("Invalid Choice")
