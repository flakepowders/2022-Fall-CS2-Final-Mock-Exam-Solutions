class Person(object):
	def __init__(self, number, school):
		self.school = school  # "KSA" or "KAIST"
		self.number = number
		self.prefList = None  # preference list (of student numbers.)
		self.partner = None  # Person object. None if free
		self.numProposal = 0  # used only if self is KSA student.

	def isFree(self):
		return self.partner == None
		
	def connect(self, p):
		assert type(p) == Person
		assert self.isFree() and p.isFree()
		self.partner = p
		p.partner = self
		
	def breakUp(self):
		assert not self.isFree()
		assert self.partner.partner == self
		self.partner.partner = None
		self.partner = None
		
	def prefer(self, p):  # whether or not self prefer p to current partner
		assert type(p) == Person
		assert not self.isFree()
		i = self.prefList.index(self.partner)
		j = self.prefList.index(p)
		return j < i

	def ksaToContact(self):  # used only if self is KSA student
		assert self.school == "KSA"
		assert self.numProposal < len(self.prefList)
		w = self.prefList[self.numProposal]
		self.numProposal += 1
		return w

##############################################################

def structClass(ksa_students):
	n = len(ksa_students)
	ksa = [None]*n
	kaist = [None]*n
	for i in range(n):
		ksa[i] = Person(i+1, "KSA")
		kaist[i] = Person(i+1, "KAIST")
	
	for i in range(n):
		ksa_pref = ksa_students[i]
		ksa[i].prefList = []
		for j in ksa_pref:
			ksa[i].prefList.append(kaist[j-1])

		kaist_pref = [i]
		diff = n-i-1
		if diff > i:
			for j in range(i):
				kaist_pref.append(i+j+1)
				kaist_pref.append(i-j-1)
			for j in range(2*i+1, n):
				kaist_pref.append(j)
		else:
			for j in range(diff):
				kaist_pref.append(i+j+1)
				kaist_pref.append(i-j-1)
			for j in range(i-diff-1, -1, -1):
				kaist_pref.append(j)
		kaist_pref = kaist_pref[::-1]
		kaist[i].prefList = []
		for j in kaist_pref:
			kaist[i].prefList.append(ksa[j])
	return ksa, kaist

##############################################################

def findMatch(ksa, kaist):
	assert len(ksa) == len(kaist)
	n = len(ksa)

	numFreeKSA = n  # initially, every student has no partner
	while numFreeKSA > 0:
		# search for a free KSA student
		# (it is already proved that the order of selecting free ksa student does not affect correctness/output of the algorithm)
		for i in range(n):
			ksa_student = ksa[i]
			if ksa_student.isFree():
				break
		assert ksa_student.isFree()
		
		# kaist student that ksa student is about to contact to
		kaist_student = ksa_student.ksaToContact()

		if kaist_student.isFree():  # if kaist student is free
			kaist_student.connect(ksa_student)  # connect them
			numFreeKSA -= 1
		elif kaist_student.prefer(ksa_student):
			kaist_student.breakUp()	# break up kaist student and their current partner
			kaist_student.connect(ksa_student)
		else:
			# rejects
			# do nothing
			pass

##############################################################

def matching(ksa_students):
	ksa, kaist = structClass(ksa_students)
	assert len(ksa) == len(kaist)
	findMatch(ksa, kaist)
	n = len(ksa)
	result = []
	for i in range(n):
		result.append(ksa[i].partner.number)
	return result
