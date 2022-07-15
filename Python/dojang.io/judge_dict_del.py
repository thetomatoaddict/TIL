keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))

x.pop('delta')

x = {key: value for key, value in x.items() if value != 30}
#딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안 됩니다.
#딕셔너리 표현식에서 if 조건문을 사용하여 삭제할 값을 제외하면 됩니다.

print(x)