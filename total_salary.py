import re

def total_salary(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
        numbers = [int(match) for match in re.findall(r'\b\d+\b', content)]
        total = sum(numbers)
        line_count = len(content.splitlines())
        answer = (total, total/line_count)

        print(f'Загальна сума заробітної плати: {answer[0]} Середня заробітна плата: {answer[1]}')
    except FileNotFoundError:
        print(f"File '{path}' not found ")
    except Exception as e:
        print(f"An error occured {str(e)}")

total_salary('test.txt')

