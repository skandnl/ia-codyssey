
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


# ---------------------------------------------------------------------------
# 2. 토큰화: 공백 없이 붙어 있어도 연산자·숫자·괄호를 분리 -------------------
# ---------------------------------------------------------------------------

def _tokenize(expr):
    """'4+5*3-2' → ['4', '+', '5', '*', '3', '-', '2']"""
    tokens = []             # 결과 리스트
    num = ''                # 현재 숫자 문자열 누적
    for ch in expr:
        if ch.isdigit() or ch == '.':   # 숫자·소수점 → num에 누적
            num += ch
        elif ch in '+-*/()':            # 연산자·괄호 → 토큰 분리
            if num:
                tokens.append(num)
                num = ''
            tokens.append(ch)
        elif ch.isspace():              # 공백은 무시
            if num:
                tokens.append(num)
                num = ''
        else:
            raise ValueError('Invalid character')
    if num:
        tokens.append(num)
    return tokens


# ---------------------------------------------------------------------------
# 3. 두 숫자와 연산자를 계산하는 도우미 --------------------------------------
# ---------------------------------------------------------------------------

def _apply(left, op, right):
    if op == '+':
        return add(left, right)
    if op == '-':
        return subtract(left, right)
    if op == '*':
        return multiply(left, right)
    if op == '/':
        return divide(left, right)
    raise ValueError('Unknown op')


# ---------------------------------------------------------------------------
# 4. 괄호 없는 리스트 계산 (곱·나눗셈 → 덧·뺄셈) -----------------------------
# ---------------------------------------------------------------------------

def _eval_no_paren(tokens):
    i = 0
    # ① 곱셈·나눗셈 먼저
    while i < len(tokens):
        if tokens[i] in ('*', '/'):
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            value = _apply(left, tokens[i], right)
            tokens[i - 1:i + 2] = [str(value)]
            i = 0
        else:
            i += 1

    # ② 덧셈·뺄셈
    i = 0
    while i < len(tokens):
        if tokens[i] in ('+', '-'):
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            value = _apply(left, tokens[i], right)
            tokens[i - 1:i + 2] = [str(value)]
            i = 0
        else:
            i += 1

    if len(tokens) != 1:
        raise ValueError('Invalid')
    return float(tokens[0])


# ---------------------------------------------------------------------------
# 5. 전체 계산 (괄호 처리 + _eval_no_paren) ----------------------------------
# ---------------------------------------------------------------------------

def calculate(expr):
    tokens = _tokenize(expr)             # 먼저 토큰화

    # ① 괄호부터 해결 (안쪽 → 바깥)
    while '(' in tokens:
        close = tokens.index(')')
        open_ = max(i for i, t in enumerate(tokens[:close]) if t == '(')
        inner = tokens[open_ + 1:close]
        value = _eval_no_paren(inner)
        tokens[open_:close + 1] = [str(value)]

    # ② 괄호 없으면 남은 토큰 계산
    return _eval_no_paren(tokens)


# ---------------------------------------------------------------------------
# 6. CLI 진입점 ---------------------------------------------------------------
# ---------------------------------------------------------------------------

def main():
    try:
        expr = input('Enter expression: ').strip()
        if not expr:
            raise ValueError
        result = calculate(expr)
        print(f'Result: {result}')
    except ZeroDivisionError:
        print('Error: Division by zero.')
    except Exception:
        print('Invalid input.')


if __name__ == '__main__':
    main()
