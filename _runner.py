import line

print(f"Linecode runner\nrunner version:1.0.0\n linecode version :0.1.1\nBy xystudio https://github.com/xystudio889/linecode\n\nPress 'exit' to exit.")

while True:
    code = input(">>> ")
    
    if code in ['exit','quit','exit()','quit()']:
        quit()
    else:
        try:
            exec(code)
        except Exception as e:
            print("Error:",e)