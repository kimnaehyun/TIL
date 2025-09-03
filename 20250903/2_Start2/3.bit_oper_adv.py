# 비트 연산은 어떻게 활용할까?
walk = 1 << 0 # 걷는 상태
attack = 1 << 1 # 공격 상태
jump = 1 << 2 # 점프 상태

character_state = 0

def set_state(state, flag):
    return state | flag

def unset_state(state, flag):
    return state & ~flag


character_state = set_state(character_state, walk)
character_state = unset_state(character_state, walk)