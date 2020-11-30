(deftemplate kotak-terbuka
   (slot location-x
      (type NUMBER)
      (default 0)
   )
   (slot location-y
      (type NUMBER)
      (default 0)
   )
   (slot contain
      (type NUMBER)
      (default -1)
   ) 
)

(deftemplate kotak-flag
   (slot id (default-dynamic (gensym*)))
   (slot location-x
      (type NUMBER)
      (default 0)
   )
   (slot location-y
      (type NUMBER)
      (default 0)
   )
)

(deftemplate kotak-tertutup
   (slot id (default-dynamic (gensym*)))
   (slot location-x
      (type NUMBER)
      (default 0)
   )
   (slot location-y
      (type NUMBER)
      (default 0)
   )
)

(deftemplate akan-buka-kotak
   (slot location-x
      (type NUMBER)
      (default 0)
   )
   (slot location-y
      (type NUMBER)
      (default 0)
   )
)

(deftemplate track-kotak
   (slot location-x
      (type NUMBER)
      (default 0)
   )
   (slot location-y
      (type NUMBER)
      (default 0)
   )
   (multislot surrounding-flags)
   (multislot surrounding-unknown)
)


; --- Facts ---
(deffacts init
   (kotak-terbuka (location-x 1) (location-y 1) (contain 1))
   (kotak-tertutup (location-x 0) (location-y 0))
   (kotak-flag (location-x 0) (location-y 1))
   (kotak-tertutup (location-x 0) (location-y 2))
   (kotak-tertutup (location-x 1) (location-y 0))
   (kotak-tertutup (location-x 1) (location-y 2))
   (kotak-tertutup (location-x 2) (location-y 0))
   (kotak-tertutup (location-x 2) (location-y 1))
   (kotak-tertutup (location-x 2) (location-y 2))
)


; --- Surroundings ---
; Flag all surrounding squares
(deffunction flag-surrounding (?x ?y)
   (do-for-all-facts ((?s kotak-tertutup)) (and (<= (abs (- ?s:location-x ?x)) 1) (<= (abs (- ?s:location-y ?y)) 1)) (assert (kotak-flag (location-x ?s:location-x) (location-y ?s:location-y))))
)

; Reveal all surrounding squares
(deffunction reveal-surrounding (?x ?y)
   (do-for-all-facts ((?s kotak-tertutup)) (and (<= (abs (- ?s:location-x ?x)) 1) (<= (abs (- ?s:location-y ?y)) 1)) (assert (akan-buka-kotak (location-x ?s:location-x) (location-y ?s:location-y))))
)

; --- Trackers ---
(defrule add-flag
   (declare (salience 20))
   ?t <- (track-kotak (location-x ?x1) (location-y ?y1) (surrounding-flags $?s))
   (kotak-flag (id ?id) (location-x ?x2&:(<= (abs (- ?x2 ?x1)) 1)) (location-y ?y2&:(<= (abs (- ?y2 ?y1)) 1)))
   (test (and (not (member$ ?id ?s)) (!= ?x1 ?x2) (!= ?x1 ?x2)))
   =>
   (modify ?t (surrounding-flags ?s ?id))
)

(defrule add-unknown
   (declare (salience 20))
   ?t <- (track-kotak (location-x ?x1) (location-y ?y1) (surrounding-unknown $?s))
   (kotak-tertutup (id ?id) (location-x ?x2&:(<= (abs (- ?x2 ?x1)) 1)) (location-y ?y2&:(<= (abs (- ?y2 ?y1)) 1)))
   (test (and (not (member$ ?id ?s)) (!= ?x1 ?x2) (!= ?x1 ?x2)))
   =>
   (modify ?t (surrounding-unknown ?s ?id))
)

(defrule remove-unknown
   (declare (salience 20))
   ?t <- (track-kotak (location-x ?x1) (location-y ?y1) (surrounding-unknown $?b ?id $?a))
   (not (kotak-tertutup (id ?id) (location-x ?x2) (location-y ?y2)))
   =>
   (modify ?t (surrounding-unknown ?b ?a))
)

(defrule add-tracker
   (declare (salience 30))
   (kotak-terbuka (location-x ?x) (location-y ?y))
   =>
   (assert (track-kotak (location-x ?x) (location-y ?y)))
)

; --- Strategies ---
(defrule flags-eq-number
   (declare (salience 10))
   (kotak-terbuka (location-x ?x) (location-y ?y) (contain ?c))
   (track-kotak (location-x ?x) (location-y ?y) (surrounding-flags $?f))
   (test (= (length$ ?f) ?c))
   =>
   (reveal-surrounding ?x ?y)
)

(defrule squares-eq-number
   (declare (salience 10))
   (kotak-terbuka (location-x ?x) (location-y ?y) (contain ?c))
   (track-kotak (location-x ?x) (location-y ?y) (surrounding-flags $?f) (surrounding-unknown $?u))
   (test (= (+ (length$ ?f) (length$ ?u)) ?c))
   =>
   (flag-surrounding ?x ?y)
)

(defrule strategy11-h
   (track-kotak (location-x ?x1) (location-y ?y) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x2&:(eq (abs (- ?x1 ?x2)) 1)) (location-y ?y) (contain ?c2) (surrounding-flags $?f2))
   (not (exists (kotak-tertutup (location-x ?x3&:(= ?x3 (+ ?x1 (* -1 (- ?x1 ?x2))))) (location-y ?y3&:(< (abs (- ?y3 ?y)) 1)))))
   (test (and (= (- ?c1 (length$ ?f1)) 1) (= (- ?c2 (length$ ?f2)) 1)))
=>
   (bind ?loc (- ?x2 ?x1))
   (do-for-all-facts ((?s kotak-tertutup)) (and (= ?s:location-x (+ ?x1 ?loc)) (<= (abs (- ?s:location-y ?y)) 1)) (assert (akan-buka-kotak (location-x ?s:location-x) (location-y ?s:location-y))))
)

(defrule strategy11-v
   (track-kotak (location-x ?x) (location-y ?y1) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x) (location-y ?y2&:(eq (abs (- ?y1 ?y2)) 1)) (contain ?c2) (surrounding-flags $?f1))
   (not (exists (kotak-tertutup (location-x ?x3&:(< (abs (- ?x3 ?x)) 1)) (location-y ?y3&:(= ?y3 (+ ?y1 (* -1 (- ?y1 ?y2))))))))
   (test (and (= (- ?c1 (length$ ?f1)) 1) (= (- ?c2 (length$ ?f2)) 1)))
=>
   (bind ?loc (- ?x2 ?x1))
   (do-for-all-facts ((?s kotak-tertutup)) (and (= ?s:location-y (+ ?y1 ?loc)) (<= (abs (- ?s:location-x ?x)) 1)) (assert (akan-buka-kotak (location-x ?s:location-x) (location-y ?s:location-y))))
)

(defrule strategy12-h
   (track-kotak (location-x ?x1) (location-y ?y) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x2&:(eq (abs (- ?x1 ?x2)) 1)) (location-y ?y) (contain ?c2) (surrounding-flags $?f1))
   (test (and (= (- ?c1 (length$ ?f1)) 2) 
              (= (- ?c2 (length$ ?f2)) 1)))
   =>

)

(defrule strategy12-v
   (track-kotak (location-x ?x) (location-y ?y1) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x) (location-y ?y2&:(eq (abs (- ?y1 ?y2)) 1)) (contain ?c2) (surrounding-flags $?f1))
   (test (and (= (- ?c1 (length$ ?f1)) 2) 
              (= (- ?c2 (length$ ?f2)) 1)))
   =>

)

(defrule strategy121-h
   (track-kotak (location-x ?x1) (location-y ?y) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x2&:(= (- ?x1 ?x2) 1)) (location-y ?y) (contain ?c2) (surrounding-flags $?f2))
   (track-kotak (location-x ?x3&:(= (- ?x1 ?x3) -1)) (location-y ?y) (contain ?c3) (surrounding-flags $?f3))
   (test (and (= (- ?c1 (length$ ?f1)) 2) 
              (= (- ?c2 (length$ ?f2)) 1)
              (= (- ?c3 (length$ ?f3)) 1)))
   =>
   (do-for-all-facts ((?s kotak-tertutup)) (and (= ?s:location-x ?x1) (<= (abs (- ?s:location-y ?y)) 1)) (assert (akan-buka-kotak (location-x ?s:location-x) (location-y ?s:location-y))))
)

(defrule strategy121-v
   (track-kotak (location-x ?x) (location-y ?y1) (contain ?c1) (surrounding-flags $?f1))
   (track-kotak (location-x ?x) (location-y ?y2&:(= (- ?y1 ?y2) 1)) (contain ?c2) (surrounding-flags $?f2))
   (track-kotak (location-x ?x) (location-y ?y3&:(= (- ?y1 ?y3) -1)) (contain ?c3) (surrounding-flags $?f3))
   (test (and (= (- ?c1 (length$ ?f1)) 2) 
              (= (- ?c2 (length$ ?f2)) 1)
              (= (- ?c3 (length$ ?f3)) 1)))
   =>
   (do-for-all-facts ((?s kotak-tertutup)) (and (<= (abs (- ?s:location-x ?x)) 1) (= ?s:location-y ?y1)) (assert (akan-buka-kotak (location-x ?s:location-x) (location-y ?s:location-y))))
)
