class OperationRequest:
    type: str
    num1: int
    num2: int

    def __init__(self, d=None):
        if d is not None:
            try:
                if "type" in d:
                    self.type = d["type"]
                if "num1" in d:
                    if type(d["num1"]) is int:
                        self.num1 = d["num1"]
                    else:
                        raise
                if "num2" in d:
                    if type(d["num2"]) is int:
                        self.num2 = d["num2"]
                    else:
                        raise Exception("Invalid Number")
            except:
                raise Exception("Invalid Operation Request")