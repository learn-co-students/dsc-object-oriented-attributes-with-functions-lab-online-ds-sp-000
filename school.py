class School:
	def __init__(self,name,roster = {}):
		self.name=name
		self.roster=roster

	def add_student(self,name,grade):
		if grade not in self.roster.keys():
			self.roster[grade]=[]
		self.roster[grade].append(name)
	def grade(self,grade):
		return(self.roster[grade])
	def sort_roster(self):
		for i in self.roster.keys():
			self.roster[i].sort()
