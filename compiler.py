class EnglishCompiler:
    def compile(self,source):
        lines  = source.split("\n")
        output = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith("create variable"):
                statement = line.replace(
                    "create variable",""
                ).strip()

                output.append(statement)

            elif line.startswith("display"):
                value = line.replace(
                    "display",
                    ""
                ).strip()
                output.append(
                    f"print({value})"
                )
        
        return "\n".join(output)
            


