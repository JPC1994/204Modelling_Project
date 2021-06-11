CONJECTUREPANEL Assignment
PROOF "P, Q, (P∧Q)→R ⊢ R"
INFER P,
     Q,
     (P∧Q)→R 
     ⊢ R 
FORMULAE
0 R,
1 P∧Q,
2 P∧Q→R,
3 Q,
4 P,
5 (P∧Q)→R 
IS
SEQ (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀x.P(x), ∀x.Q(x) ⊢ ∀x.(Q(x)→P(x))"
INFER ∀x.P(x),
     ∀x.Q(x)
     ⊢ ∀x.(Q(x)→P(x))
FORMULAE
0 P(i),
1 Q(i),
2 actual i,
3 ∀x.P(x),
4 P(x),
5 i,
6 x,
7 Q(i)→P(i),
8 ∀x.Q(x),
9 Q(x),
10 Q(x)→P(x)
IS
SEQ ("∀ intro"[i,P,x\5,10,6]) (cut[B,C\1,7]) ("∀ elim"[P,i,x\9,5,6]) (hyp[A\8]) (hyp[A\2]) (cut[B,C\0,7]) ("∀ elim"[P,i,x\4,5,6]) (hyp[A\3]) (hyp[A\2]) ("→ intro"[A,B\1,0]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "P, (P∧¬Q)∨(¬P∧Q) ⊢ ¬Q"
INFER P,
     (P∧¬Q)∨(¬P∧Q)
     ⊢ ¬Q 
FORMULAE
0 ⊥,
1 Q,
2 ¬P,
3 P,
4 ¬Q,
5 ¬P∧Q,
6 P∧¬Q,
7 P∧¬Q∨¬P∧Q,
8 (P∧¬Q)∨(¬P∧Q)
IS
SEQ ("∨ elim"[A,B,C\6,5,4]) (hyp[A\7]) (cut[B,C\4,4]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\3,4]) (hyp[A\6])) (hyp[A\4]) (cut[B,C\1,4]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\2,1]) (hyp[A\5])) (cut[B,C\2,4]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\2,1]) (hyp[A\5])) (cut[B,C\0,4]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("¬ intro"[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "P, R, (P∨Q)∧R→T ⊢ T"
INFER P,
     R,
     (P∨Q)∧R→T 
     ⊢ T 
FORMULAE
0 T,
1 (P∨Q)∧R,
2 (P∨Q)∧R→T,
3 R,
4 P∨Q,
5 P,
6 Q 
IS
SEQ (cut[B,C\4,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\6,5]) (hyp[A\5])) (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
