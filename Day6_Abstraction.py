# ABSTRACT class
# its the process of handling the
# information by hiding

class fruits:
  def taste(self):
      raise NotImplementedError()
  def rich(self):
      raise NotImplementedError()
  def color(self):
      raise NotImplementedError()
class mango(fruits):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return "Golden Yellow"
class orange(fruits):
    def taste(self):
        return "sour"
    def rich(self):
        return "vitamin c"
    def color(self):
        return "orange"
Alphanso = mango()
print("Mango - ",Alphanso.taste(),Alphanso.rich(),Alphanso.color())
Alphanso = orange()
print("Orange - ",Alphanso.taste(),Alphanso.rich(),Alphanso.color())
