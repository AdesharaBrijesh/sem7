concate([H1|T1],L2,[H1|T2]):-
       concate(T1,L2,T2).
concate([],L2,L2).


