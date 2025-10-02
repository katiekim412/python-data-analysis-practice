def BMI():
    wgt = float(input('체중을 kg으로 입력하세요: '))
    hgt = float(input('키를 cm로 입력하세요: '))
    bmi = wgt/(hgt/100) **2
    if bmi >= 25:
        result = '비만'
    elif bmi >= 23:
        result = '과체중'
    elif bmi >= 18:
        result = '정상'
    else:
        result = '저체중'
    return f'귀하의 체질량지수는 {bmi:.1f} 이고, 진달결과는 [{result}]입니다.'

def printArgs(*args):
    for i in args:
        print(i)
        
def printKwargs(**kwargs) :
    for k, v in kwargs.items():
        print(f'{k}: {v}')