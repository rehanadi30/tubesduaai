
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
   ?lama <- (kotak (location-x ?x) (location-y ?y) (contain -1))
   ?akanbuka <- (akan-buka-kotak ?x ?y ?value)
     =>
   (assert (kotak (location-x ?x) (location-y ?y) (contain ?value)))
   (retract ?lama)
   (retract ?akanbuka)
)
