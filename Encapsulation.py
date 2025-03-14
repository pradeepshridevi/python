class pradeep:
  def __init__(self):
    self.pub = "ok"
    self.__prajwl="not ok"
  def rahul_private(self):
    print(self.__prajwl)
obj=pradeep()
print(obj.pub)
obj.rahul_private()
