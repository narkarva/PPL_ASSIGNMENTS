(format t "Enter positive number~%")
(defvar n (read))
(defun fact (n)
  (if  (= n 0)
    1
    (* n (fact (- n 1)))
  )
)
(if (< n 0)
  (format t "Factorial of negative number doesn't exist")
  (progn 
  	(defvar result (fact n))
  	(format t "Factorial of given number = ~d" result)
  )
)

