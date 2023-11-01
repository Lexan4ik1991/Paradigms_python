sum([], 0).

sum([Head|Tail], Sum) :-
    sum(Tail, TempSum),
    Sum is Head + TempSum.

?- sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Sum), write(Sum).
