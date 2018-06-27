class Person:
	
	def __init__(self,name):
		self.name=name

	def say_hi(self):
		num=12
		print "Hello how are you : %r" %num
		print "Hello my name is" , self.name

	def say_bye(self):
		print """
				
				      >>           >=>       >=>                        
     >>=>          >=>  >>   >=>                        
    >> >=>         >=>     >=>>==> >=>   >=>    >=> >=> 
   >=>  >=>     >=>>=> >=>   >=>    >=> >=>   >=>   >=> 
  >=====>>=>   >>  >=> >=>   >=>      >==>   >=>    >=> 
 >=>      >=>  >>  >=> >=>   >=>       >=>    >=>   >=> 
>=>        >=>  >=>>=> >=>    >=>     >=>      >==>>>==>
                                    >=>                 

		  	  # """
p=Person('Aditya')
p.say_hi()
p.say_bye()

class Person1:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name

p1 = Person1('Aditya Srivastava')
p1.say_hi()