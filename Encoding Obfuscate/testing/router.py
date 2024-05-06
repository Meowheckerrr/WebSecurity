
#router.py
import os
from view import View

class Router():

    def __init__(self):
        
        self.data = {
            "name": "<svg onload=&#x70;&#x72;&#x6f;&#x6d;&#x70;&#x74;()>",
            "email": "meowhecker@meow.com"
        }
        self.currentDirPath = os.path.dirname(os.path.abspath(__file__))
        

    def route(self,reqPath):
        
        # Current Path (Avoid File Not Found)
        currentDirPath = os.path.dirname(os.path.abspath(__file__))
       
        if reqPath == "/":
            templatePath = os.path.join(self.currentDirPath,"views","index.html")
            return View.render(templatePath,self.data)
        elif reqPath == "/test":
            templatePath = os.path.join(self.currentDirPath,"views","test.html")
            return View.render(templatePath)
        else:
            return self.notFound()

    def notFound(self):
        return "<h1>404 Not Found  ~ Meow</h1>"