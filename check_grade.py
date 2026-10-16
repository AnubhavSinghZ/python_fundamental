#Student Grade Calculator

print("__GRADE EVALUATION SYSTEM__")
marks=float(input("Enter your marks(0-100):"))    #taking inpput
if marks>=90:
 grade="A+"
 comment="Exclelent Performance!"
elif marks>=80:
 grade="A"
 comment="Grate Job!"
elif marks>=70:
 grade="B+"
 comment="Good,  Keep it upppp"
elif marks>=60:
 grade="B"
 comment="Satisfactory! Need more efforts"
elif marks>=50:
 grade="B-"
 comment="Bad Result"
elif 0<=marks<50:
 grade="F"
 comment="Failed, don't give up!"
else:
 grade="Invalid"
 comment="Please enter marks between 0 and 100"
print(f"\nGrade:{grade}")

print(f"Teacher's Remark:{comment}")
