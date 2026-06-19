from compiler import EnglishCompiler
import subprocess

# step-1 Reading the content inside hello.eng
with open("examples/hello.eng") as f:
    source = f.read()

# step-2 Create an object of the imported EnglishCompler
compiler = EnglishCompiler()

# step-3 the python getting generated here will be collected
generated_python = compiler.compile(source)

# step-4 the collected python will be writed in output.py
with open("output/output.py","w") as f:
    f.write(generated_python)

# step-5(last step) - the program will then give result from the collected python 
subprocess.run(
    ["python3","output/output.py"]
)