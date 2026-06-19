from compiler import EnglishCompiler
import subprocess

with open("examples/hello.eng") as f:
    source = f.read()

compiler = EnglishCompiler()

generated_python = compiler.compile(source)


with open("output/output.py","w") as f:
    f.write(generated_python)

subprocess.run(
    ["python3","output/output.py"]
)