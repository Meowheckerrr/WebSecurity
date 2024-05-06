
#router.py
import os
from view import View

class Router():

    def __init__(self):
        
        self.data = {
            "name": "meowhecker",
            "email": "meowhecker@meow.com"
        }
        self.currentDirPath = os.path.dirname(os.path.abspath(__file__))
        

    def route(self,reqPath):
        
        # Current Path (Avoid File Not Found)
        currentDirPath = os.path.dirname(os.path.abspath(__file__))
        print(currentDirPath)
        
        if reqPath == "/":
            templatePath = os.path.join(self.currentDirPath,"views","index.html")
            return View.render(templatePath,self.data)
        else:
            return self.notFound()

    def notFound(self):
        return "<h1>404 Not Found  ~ Meow</h1>"