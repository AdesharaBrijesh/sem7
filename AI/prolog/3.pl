vertical(seg(point(X,Y),point(X,Y1))):-
    Y\==Y1.
horizontal(seg(point(X,Y),point(X1,Y))):-
    X\==X1.
oblique(seg(point(X1,Y1),point(X2,Y2))):-
    X1\==X2,
    Y1\==Y2.
