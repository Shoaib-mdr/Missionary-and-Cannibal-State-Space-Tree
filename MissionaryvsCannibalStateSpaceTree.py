import pydot
import time

class State(object):
	def __init__(self,MisLeft,CanLeft,BoatPos, Operation):
		self.MisLeft = MisLeft
		self.CanLeft = CanLeft
		self.BoatPos = BoatPos
		self.MisRight = 3 - MisLeft
		self.CanRight = 3 - CanLeft
		self.parent = None
		self.Operation = Operation

	

	def check_precondition(self):
		if ((self.MisLeft < 0) or (self.MisRight < 0) or (self.CanLeft < 0) or (self.CanRight < 0) or (self.MisLeft > 3) \
		 or (self.MisRight > 3) or (self.CanLeft > 3) or (self.CanRight > 3)):
			return False
		if ((self.MisLeft == 0 or self.MisLeft >= self.CanLeft) and (self.MisRight == 0 or self.MisRight >= self.CanRight)):
			return True
		else:
			return False

	def current_state(self):
		return self.MisLeft, self.CanLeft, self.BoatPos, self.MisRight, self.CanRight


	def print_state(self):
		state="(" + str(self.MisLeft) + ", " + str(self.CanLeft) + ", " + str(self.BoatPos) + ", " + str(self.MisRight) + ", " + str(self.CanRight) + ")"
		return state

	def goal_state(self):
		if ((self.MisLeft == 0) and (self.CanLeft == 0) and (self.BoatPos == 0) and (self.MisRight == 3)\
		and (self.CanRight == 3)):
			return True
		else:
			return False
		

	def next_state(self, current_state):

		next_state_list=list()
		if (self.BoatPos == 1): #The boat is in left side of the river

			#Move 1 missionary and 1 cannibal to right side of the river
			NewState = State(MisLeft = self.MisLeft - 1, CanLeft = self.CanLeft - 1, BoatPos = 0, Operation = "1M1C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 1 Cannibal to right side of the river
			NewState = State(MisLeft = self.MisLeft, CanLeft = self.CanLeft - 1, BoatPos = 0, Operation = "1C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 2 Cannibal to right side of the river
			NewState = State(MisLeft = self.MisLeft, CanLeft = self.CanLeft - 2, BoatPos = 0, Operation ="2C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 1 missionary to right side of the river
			NewState = State(MisLeft = self.MisLeft - 1, CanLeft = self.CanLeft, BoatPos = 0, Operation="1M")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 2 missionary to right side of the river
			NewState = State(MisLeft = self.MisLeft - 2, CanLeft = self.CanLeft, BoatPos = 0, Operation="2M")
			NewState.parent = current_state
			next_state_list.append(NewState)


			#print("1",len(next_state_list))
			return next_state_list

		else: # The boat is in the right side of the river
			

			#Move 1 missionary and 1 cannibal to left side of the river
			NewState = State(MisLeft = self.MisLeft + 1, CanLeft = self.CanLeft + 1, BoatPos = 1, Operation="1M1C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 1 Cannibal to left side of the river
			NewState = State(MisLeft = self.MisLeft, CanLeft = self.CanLeft + 1, BoatPos = 1, Operation="1C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 2 Cannibal to left side of the river
			NewState = State(MisLeft = self.MisLeft, CanLeft = self.CanLeft + 2, BoatPos = 1, Operation="2C")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 1 missionary to left side of the river
			NewState = State(MisLeft = self.MisLeft + 1, CanLeft = self.CanLeft, BoatPos = 1, Operation="1M")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#Move 2 missionary to left side of the river
			NewState = State(MisLeft = self.MisLeft + 2, CanLeft = self.CanLeft, BoatPos = 1, Operation="2M")
			NewState.parent = current_state
			next_state_list.append(NewState)

			#print("0",len(next_state_list))
			return next_state_list

		



		'''
class Stack(object):
     def __init__(self, items):
         self.items = items

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def stacklist(self):
     	 return self.items
     	

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items) '''



class Main(object):
	def __init__(self):
		self.InitialState = State(MisLeft=3,CanLeft=3,BoatPos=1, Operation = "0")
		self.G = pydot.Dot(graph_type="digraph", rankdir="same")

		ChildrenStates = list()

	def LegendGenerate(self):
		node=pydot.Node("                                                          State Space Tree of Missionary and Cannibal Problem in DEPTH WISE SEARCH", shape='none', fillcolor='yellow', fontsize='20')
		self.G.add_node(node)



		node1=pydot.Node("                                                                    LEGEND", shape='none', fillcolor='yellow', fontsize='20')
		self.G.add_node(node1)

		Assignmentnode= pydot.Node("Assignment#1 Shoaib Manandhar(26) and Bidhan Rai (38)", shape="none", fontsize="20")
		self.G.add_node(Assignmentnode)

		



		edge=pydot.Edge(node,node1,style='invis')
		self.G.add_edge(edge)

		nodestart=pydot.Node("     ", shape='none', fillcolor='yellow', fontsize='20')
		self.G.add_node(nodestart)
		InitialStateNode=pydot.Node("Initial State",style='filled', fillcolor='Green')
		self.G.add_node(InitialStateNode)

		patternode=pydot.Node("SOLUTION PATTERN = (LeftMissionary,  LeftCannibal,  BoatPosition,  RightMissionary,  RightCannibal)", shape='none',fontsize='20')
		self.G.add_node(patternode)
		self.G.add_edge(pydot.Edge(InitialStateNode,patternode,style='invis'))
		self.G.add_edge(pydot.Edge(patternode,Assignmentnode,style='invis'))



		edge=pydot.Edge(nodestart,InitialStateNode,style='invis')
		self.G.add_edge(edge)

		


		GoalStateNode=pydot.Node("Goal State",style='filled', fillcolor='Pink')
		self.G.add_node(GoalStateNode)
		edge=pydot.Edge(nodestart,GoalStateNode,style='invis')
		self.G.add_edge(edge)


		ExploringNode=pydot.Node("Exploring Node",style='filled', fillcolor='yellow')
		self.G.add_node(ExploringNode)
		edge=pydot.Edge(nodestart,ExploringNode,style='invis')
		self.G.add_edge(edge)

		KilledNode=pydot.Node("Killed Node",style='filled', fillcolor='Red')
		self.G.add_node(KilledNode)
		edge=pydot.Edge(nodestart,KilledNode,style='invis')
		self.G.add_edge(edge)


	

		
		

	def depth_wise_search(self):
		if (self.InitialState.goal_state()):
			return self.InitialState
		#Stackss=[]
		Stacks = []
		Stacks2 = []
		VisitedState = []
		Stacks.insert(0,self.InitialState)
		nodes=self.InitialState.print_state()
		print(nodes)
		
		node=pydot.Node(nodes,style="filled", fillcolor="green")
		self.G.add_node(node)


		print(self.InitialState.current_state())
		
		
		#print(Stacks.size())
		while Stacks:
		#for i in range (0,13):
			CurrentState = Stacks.pop(0)
			if CurrentState.check_precondition():
				if CurrentState.parent!=None:
					node=pydot.Node(CurrentState.print_state(), style = 'filled', fillcolor='yellow')
					self.G.add_node(node)
					edge=pydot.Edge(CurrentState.parent.print_state(),CurrentState.print_state(),label=CurrentState.Operation)
					self.G.add_edge(edge)

				print("Current State : ", CurrentState.current_state(), end=" : ")
				print("Goal State : ", CurrentState.goal_state())
				if (CurrentState.goal_state()):
					node=pydot.Node(CurrentState.print_state(),style='filled', fillcolor='Pink')
					self.G.add_node(node)
					return CurrentState

				VisitedState.insert(0,CurrentState)
				

				ChildrenStates = CurrentState.next_state(CurrentState) 
			
				for child in ChildrenStates:
					#print(child.current_state())
					#print(VisitedState[0].current_state())
					count=0
					for EachVisitedState in VisitedState:
						if (child.current_state() == EachVisitedState.current_state()):
							count=count + 1
					for EachStateInStacks in Stacks:
						if (child.current_state() == EachStateInStacks.current_state()):
							count = count + 1
					if count==0:
						Stacks.insert(0,child)
						'''
						if child.check_precondition():
							#node=pydot.Node(child.print_state(), style = 'filled', fillcolor='green')
							#self.G.add_node(node)
							#edge=pydot.Edge(child.parent.print_state(),child.print_state())
							#self.G.add_edge(edge)
							Stacks.insert(0,child)

						if not child.check_precondition():
							
							node=pydot.Node(child.print_state(), style = 'filled', fillcolor='red')
							self.G.add_node(node)
							edge=pydot.Edge(child.parent.print_state(),child.print_state())
							self.G.add_edge(edge)
							Stacks2.insert(0, child)'''
			elif not CurrentState.check_precondition():
				if CurrentState.parent!=None:
					node=pydot.Node(CurrentState.print_state(), style = 'filled', fillcolor='red')
					self.G.add_node(node)
					edge=pydot.Edge(CurrentState.parent.print_state(),CurrentState.print_state(), label=CurrentState.Operation)
					self.G.add_edge(edge)
					VisitedState.insert(0,CurrentState)


				



						#print(child.current_state(), end="    ")


					
					#print(len(Stacks))
			print("STACKS LIST")
			a=len(Stacks)
			for i in range(0,a):
				print(Stacks[i].current_state())
			print("VisitedState")
			
			b=len(VisitedState)
			for i in range (0,b):
				print(VisitedState[i].current_state())
			
			


				
		return "No SOLUTION" 
		




start=time.time()
obj=Main()
print(obj.InitialState.MisLeft)
print(obj.depth_wise_search())
obj.LegendGenerate()


obj.G.write_png('sol1.png')
end=time.time()
print("Time Complexity : ", end-start)




