from equation import Equation
import turtle
import constants as ct

class Linear(Equation):
    def __init__(self):
        super().__init__()

    def stringify(self, a, c) -> str:
        res_begin = 'f(x) = '

        if a == 0 and c == 0:
            res = res_begin + f'{a}'
        elif a == 0:
            res = res_begin + f'{c}'
        elif c == 0:
            if a == 1:
                res = res_begin + 'x'
            else:
                res = res_begin + f'{a}x'
        else:
            if a < 0 and c < 0:
                res = res_begin + f'{a} ' + '- ' + f'{abs(c)}'
            elif c < 0:
                res = res_begin + f'{a}x ' + '- ' + f'{abs(c)}'
            else:
                res = res_begin + f'{a}x ' + '+ ' + f'{c}'
        
        return res

    def write_func_on_graph(self, a, c):
        t = self.turtle

        t.penup()

        initial_pos = t.position()
        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(self.stringify(a, c)) # fix correct output
        t.setposition(initial_pos)
    
    def evaluate_y(self, x, a, c) -> float:
        return a * x + c
    
    def plot_graph(self, a, c):
        t = self.turtle

        self.write_func_on_graph(a, c)

        t.showturtle()
        t.pencolor('red')
        t.penup()

        for x in self.x_range:
            y = self.evaluate_y(x, a, c)

            if x in self.equation_range and y in self.equation_range:
                t.goto(ct.ZOOM * x, ct.ZOOM * y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()