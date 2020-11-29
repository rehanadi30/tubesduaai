
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

(deftemplate flag
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

(defrule buka-kotak
   ?lama <- (kotak (location-x ?x) (location-y ?y) (contain -1))
   ?akanbuka <- (akan-buka-kotak (location-x ?x) (location-y ?y))
     =>
   (assert (kotak (location-x ?x) (location-y ?y) (contain ?value)))
   (retract ?lama)
   (retract ?akanbuka)
)
