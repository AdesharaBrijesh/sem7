disp([H|T]):-
    write("Enter element to search for:"),
    read(N),
    find_ele([H|T],N).
find_ele([H|T],N):-
    H\=[],
    (N=H->writef("%t is a member of list",[N]);find_ele(T,N));
    T=[],
    writef("%t is not a member of list",[N]).

add(X,L,[X|L]).
 
/*concate list*/

concate([H1|T1],L2,[H1|T2]):-
       concate(T1,L2,T2).
concate([],L2,L2).


