"""Drop Drop"""

def main():
    """Input"""
    grade = float(input())
    if grade >= 0.00 and grade <= 4.00:
        if grade >= 2.00:
            print("I'm so happy.")
        elif grade >= 1.00:
            print("%.2f" %(4.00-grade))
        elif grade >= 0:
            print("I'm so sad.")
main()
