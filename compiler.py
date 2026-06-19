class EnglishCompiler:
    def compile(self,source):
        lines  = source.split("\n")
        output = []
        indent_level = 0
        
        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith("create variable"):
                statement = line.replace(
                    "create variable",""
                ).strip()

                output.append(("    " * indent_level)+statement)

            elif line.startswith("display"):
                value = line.replace(
                    "display",
                    ""
                ).strip()
                output.append(
                    ("    " * indent_level) + f"print({value})"
                )
            
            elif line.startswith("for loop"):
                parts = line.split()
                variable = parts[2]
                start = parts[4]
                end = parts[6].replace(":","")

                output.append(
                    ("    " * indent_level) + f"for {variable} in range({start},{int(end) + 1}):"
                )
                indent_level += 1
            
            elif line == "end loop":
                indent_level -= 1
        
        return "\n".join(output)
            


