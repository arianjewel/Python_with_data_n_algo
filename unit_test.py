def average(l):
    if not l:
        return None

    return sum(l)/len(l)

def test_average():
    #assert average([1,2,3,4,5])==3,"Your Excepted value is wrong"
    test_cases=[
    {
        "name":"simple case 1",
        "input":[1,2,3],
        "excepted":2
    },
    {
        "name":"simple case 2",
        "input":[1,2,3,4],
        "excepted":2.5
    },
    {
        "name":"list with 1 item",
        "input":[100],
        "excepted":100
    },
    {
        "name":"empty list",
        "input":[],
        "excepted":None
    }
    ]
    for case in test_cases:
        assert average(case["input"])==case["excepted"],case["name"]
