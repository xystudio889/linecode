from line import *

run(
    For(SetV("i", 0),Op(GetV("i"),lt,1000),ChangeV("i", 1, add), {
        If((Op(Op(GetV("i"), mod, 2),eq,0)), {
            Print(GetV("i"))
        })
    })
)