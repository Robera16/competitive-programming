class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s)==1:
			return int(s[0])

		s=s.replace(" ","")
		stack=[]
		import math
		val=0
		prev_sym="+"
		for i in range(len(s)):
			if s[i].isdigit():
				val=10*val+int(s[i])  
			else:
				if prev_sym=="*":
					stack[-1]=stack[-1]*val
				elif prev_sym=="/":
					if stack[-1]<0:
						stack[-1]=-(-stack[-1]/val)
					else:
						stack[-1]=stack[-1]/val
				elif prev_sym=="-":
					stack.append(-val)
				else:
					stack.append(val)

				prev_sym=s[i]                
				val=0

		if prev_sym=="*":
			stack[-1]=stack[-1]*val
		elif prev_sym=="/":
			if stack[-1]<0:
				stack[-1]=-(-stack[-1]/val)
			else:
				stack[-1]=stack[-1]/val
		elif prev_sym=="-":
			stack.append(-val)
		else:
			stack.append(val)

		return sum(stack)