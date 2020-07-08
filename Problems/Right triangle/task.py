class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if hyp ** 2 == leg_1 ** 2 + leg_2 ** 2:
            self.area = str(round(1 / 2 * leg_1 * leg_2, 1))
        else:
            self.area = "Not right"


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
t = RightTriangle(input_c, input_a, input_b)
print(t.area)
