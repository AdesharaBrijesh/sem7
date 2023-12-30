de(H,[H],[]).
de(X,[X|T1],T1).
de(X,[H|T],[H,T1]):-
    de(X,T,T1).
de(X,[_],_):-
    writef("Element %t is not found",[X]).
