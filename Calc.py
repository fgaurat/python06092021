


from DivBy12Exception import DivBy12Exception


class Calc:

    def division(self,a,b):
        if b==12:
            # err = Exception('Division par 12')
            # raise err
            # raise Exception('Division par 12')
            raise DivBy12Exception()
        return a/b
