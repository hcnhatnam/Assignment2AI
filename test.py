class abc():
	def __init__(self,x):
		self.x=x
def main():
	a=abc(1)
	b=abc(1)
	print(hash(str(a))==hash(str(b)))
main()