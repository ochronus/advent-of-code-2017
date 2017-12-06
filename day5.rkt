#lang racket

(define instructions (map string->number (file->lines "day5-input.txt")))


(define (walk1 instructions pos acc)
  (if (or (>= pos  (length instructions)) (< pos 0))
      (println acc)
      (let ([jump (list-ref instructions pos)])
        (walk1 (list-set instructions pos (+ jump 1)) (+ pos jump) (+ acc 1)))))

(define (walk2 instructions pos acc)
  (if (or (>= pos  (length instructions)) (< pos 0))
      (println acc)
      (let ([jump (list-ref instructions pos)])
        (walk2 (list-set instructions pos
                         (if (>= jump 3)
                             (- jump 1)
                             (+ jump 1))
                         )
                        
               (+ pos jump)
               (+ acc 1)))))

(walk1 instructions 0 0)
(walk2 instructions 0 0)
