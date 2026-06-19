class EnglishCompiler:
    def add_line(self,output,indent_level,statement):
        output.append(("    "* indent_level) + statement)

    def handle_create_variable(self,line,output,indent_level):
        statement = line.replace("create variable","").strip()
        self.add_line(output,indent_level,statement)

    def handle_display(self,line,output,indent_level):
        value = line.replace("display","").strip()
        self.add_line(output,indent_level,f"print({value})")

    def compile(self,source):
        lines  = source.split("\n")
        output = []
        indent_level = 0
        
        for line in lines:
            line = line.strip()

            if not line:
                output.append("")
                continue

            if line.startswith("create variable"):
                self.handle_create_variable(line,output,indent_level)

            elif line.startswith("display"):
                self.handle_display(line,output,indent_level)
            
            elif line.startswith("for loop"):
                parts = line.split()
                variable = parts[2]
                start = parts[4]
                end = parts[6].replace(":" ,"")

                output.append(
                    ("    " * indent_level) + f"for {variable} in range({start},{int(end) + 1}):"
                )
                indent_level += 1
            elif line.startswith("while loop "):
                condition = line[11:]
                output.append(
                    ("    " * indent_level) + f"while {condition}"
                )
                indent_level += 1
            
            elif line == "end loop":
                indent_level -= 1

            elif line.startswith("if "):
                condition = line[3:]
                output.append(
                    ("    " * indent_level) + f"if {condition}"
                )
                indent_level += 1
            
            elif line.startswith("else if "):
                indent_level -= 1

                condition = line[8:]
                output.append(
                    ("    " * indent_level + f"elif {condition}"))
                indent_level += 1
            
            elif line == "else:":
                indent_level -= 1
                output.append(
                    ("    " * indent_level) + "else:"
                )

                indent_level += 1
            
            elif line.startswith("end if"):
                indent_level -= 1
            
            elif "=" in line:
                self.add_line(
                    output,
                    indent_level,
                    line
                )
        return "\n".join(output)
            


