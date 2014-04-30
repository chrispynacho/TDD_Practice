import sure
from calculator import Calculator


def test_add():
    calc = Calculator()
    
    (4).should.equal(calc.add(2, 2))
    calc.add.when.called_with('two', 'three').should.throw(ValueError)
    calc.add.when.called_with('two', 3).should.throw(ValueError)
    calc.add.when.called_with(2, 'three').should.throw(ValueError)

