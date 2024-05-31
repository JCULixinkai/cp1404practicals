def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == '__main__':
    main()
