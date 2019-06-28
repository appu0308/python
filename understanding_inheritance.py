#Program is to display child's father and mother full name with grand father's name.

class gparents: #Defining Super Class
	gfather=' '+input("Enter Grand Father name:") #Here we are prompting user to enter grandfather name to concat with their parent's name
class parents(gparents): #Defined subclass by mentioning gparents in parents class
	def __init__(self,mother,father): #Method to concat father & mother name with the grandfather name
		self.mother=mother+gparents.gfather
		self.father=father+gparents.gfather
child1mother=input("Enter Mother name of child:")
child1father=input("Enter Father name of child:")
child1=parents(child1mother,child1father) #Child1 object creation for child class which inherits gparent class methods and attributes
print("Child1 Mother name is:",child1.mother)
print("Child1 Father name is:",child1.father)
