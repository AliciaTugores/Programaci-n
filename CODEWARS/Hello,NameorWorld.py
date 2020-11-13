#Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! 
# if name is not given (or passed as an empty String). Assuming that name ies a String and it
#checks for user typos to return a name with a first capital letter (Xxxx).
def hello(name = ''):
    if name == '':
        return "Hello, World!"
    return "Hello, " + (name.lower().capitalize()) + "!"