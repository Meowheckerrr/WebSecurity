#view.py

class View:

    @staticmethod  # Method, attribute allow directly invoke Without creating  Instance  
    def render(templatePath, data=None): 
        print(data)
        renderContent = ""
        with open(templatePath, 'r') as template:

            templateContent = template.read() # (Strings) 

            if data :
                renderContent = templateContent.format(**data) # Template {name} -> name
            else :
                renderContent = templateContent

        return renderContent