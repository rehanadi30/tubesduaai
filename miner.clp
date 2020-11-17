
(deftemplate kotak
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

(defrule buka-kotak
   (ingin-buka-kotak ?x ?y)
   ?lama <- (kotak (location-x ?x) (location-y ?y) (contain -1))
     =>
   (assert (kotak (location-x ?x) (location-y ?y) (contain 2)))		;ganti dengan value sebenernya
   (retract ?lama)
)

(defrule mulai
    =>
   (assert (kotak))
   (assert (ingin-buka-kotak 0 0))
)
