c_to_f(C):-
    F is C*9/5+32,
    write(F).
freezing(F):-
    F=<32.
freezing(F):-
    write("It is not freezing").
