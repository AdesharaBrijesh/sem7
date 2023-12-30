print("Welcome To ChatBot")
print("Developed By Dharmay Sureja")
print("Feel Free To ask questions Like below")
print("How are You")
print("Do You like AI")
print("What is your name")
print("Are you on Social Media")
print("How do you work?")
print("Exit")
while True:
	question=input("Enter One questions from List Above : ")
	question=question.lower()
	if question in['how are you']:
		print("I am absoluetly fine")
	elif question in ['do you like ai']:
		print("Obviously! Who doesn't Love AI?")
	elif question in ['what is your name']:
		print("My Name is ChatBot but you can call me Chatty")
	elif question in ['are you on social media']:
		print("No I prefert to stay away from that things")
	elif question in ['how do you work']:
		print("I am backed with IF.. Else.. Statements ")
	elif question in ['exit']:
		print("Stay Home Stay SAFE!! ")
		break
	else:
		print("I think i don't Understand That")
		
	
