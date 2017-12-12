#lang racket

(define (max a b)
  (if (> a b) a b)
)

(define (calc-distance x y z)
    (/ (+ (abs x) (abs y) (abs z)) 2)
)

(define (walk steplist x y z max-distance)
    (let ([dist (calc-distance x y z)])
        (if (empty? steplist)
            (list dist max-distance)
            (cond
                [(equal? (first steplist) "s") (walk (rest steplist) x (- y 1) (+ z 1) (max dist max-distance))]
                [(equal? (first steplist) "se") (walk (rest steplist) (+ x 1) (- y 1) z (max dist max-distance))]
                [(equal? (first steplist) "sw") (walk (rest steplist) (- x 1) y (+ z 1) (max dist max-distance))]
                [(equal? (first steplist) "n") (walk (rest steplist) x (+ y 1) (- z 1) (max dist max-distance))]
                [(equal? (first steplist) "ne") (walk (rest steplist) (+ x 1) y (- z 1) (max dist max-distance))]
                [(equal? (first steplist) "nw") (walk (rest steplist) (- x 1 ) (+ y 1) z (max dist max-distance))]
            ) 
        )
    )
)

(define steps (string-split (file->string "day11-input.txt") ","))
(print (walk steps 0 0 0 0))
